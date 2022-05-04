import os
from enum import Enum
from typing import Optional, Union, List, Set
from typing import Optional, Union, List
from .models import (
    Feed,
    Market,
    EquityAgg,
    CurrencyAgg,
    EquityTrade,
    CryptoTrade,
    EquityQuote,
    ForexQuote,
    CryptoQuote,
    Imbalance,
    LimitUpLimitDown,
    Level2Book,
)
import websockets
import json
import inspect
import asyncio

env_key = "POLYGON_API_KEY"


def parse_single(data):
    event_type = data["ev"]
    if event_type == "A":
        return EquityAgg.from_dict(data)
    elif event_type == "AM":
        return EquityAgg.from_dict(data)
    elif event_type == "CA":
        return CurrencyAgg.from_dict(data)
    elif event_type == "XA":
        return CurrencyAgg.from_dict(data)
    elif event_type == "T":
        return EquityTrade.from_dict(data)
    elif event_type == "XT":
        return CryptoTrade.from_dict(data)
    elif event_type == "Q":
        return EquityQuote.from_dict(data)
    elif event_type == "C":
        return ForexQuote.from_dict(data)
    elif event_type == "XQ":
        return CryptoQuote.from_dict(data)
    elif event_type == "NOI":
        return Imbalance.from_dict(data)
    elif event_type == "LULD":
        return LimitUpLimitDown.from_dict(data)
    elif event_type == "XL2":
        return Level2Book.from_dict(data)
    return None


def parse(msg):
    res = []
    for m in msg:
        parsed = parse_single(m)
        if parsed is None:
            print("bad message", m)
        else:
            res.append(parsed)
    return res


class WebsocketBaseClient:
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(env_key),
        feed: Union[str, Feed] = Feed.RealTime,
        market: Union[str, Market] = Market.Stocks,
        raw: bool = False,
        verbose: bool = False,
        subscriptions: List[str] = [],
        max_reconnects: Optional[int] = 5,
        secure: bool = True,
        **kwargs,
    ):
        if api_key is None:
            raise Exception(
                f"Must specify env var {env_key} or pass api_key in constructor"
            )
        self.api_key = api_key
        self.feed = feed
        self.market = market
        self.raw = raw
        self.verbose = verbose
        self.websocket_cfg = kwargs
        if isinstance(feed, Enum):
            feed = feed.value
        if isinstance(market, Enum):
            market = market.value
        self.url = f"ws{'s' if secure else ''}://{feed}/{market}"
        self.subscribed = False
        self.subs: Set[str] = set()
        self.max_reconnects = max_reconnects
        self.websocket = None
        self.scheduled_subs = set(subscriptions)
        self.schedule_resub = True

    # https://websockets.readthedocs.io/en/stable/reference/client.html#opening-a-connection
    async def connect(self, processor, close_timeout=1, **kwargs):
        reconnects = 0
        isasync = inspect.iscoroutinefunction(processor)
        if self.verbose:
            print("connect", self.url)
        async for s in websockets.connect(
            self.url, close_timeout=close_timeout, **kwargs
        ):
            self.websocket = s
            try:
                msg = await s.recv()
                if self.verbose:
                    print("connected", msg)
                if self.verbose:
                    print("authing")
                await s.send(json.dumps({"action": "auth", "params": self.api_key}))
                msg = await s.recv()
                if self.verbose:
                    print("authed", msg)
                while True:
                    if self.schedule_resub:
                        print("reconciling", self.subs, self.scheduled_subs)
                        new_subs = self.scheduled_subs.difference(self.subs)
                        await self._subscribe(new_subs)
                        old_subs = self.subs.difference(self.scheduled_subs)
                        await self._unsubscribe(old_subs)
                        self.subs = self.scheduled_subs
                        self.subs = set(self.scheduled_subs)
                        self.schedule_resub = False

                    msg = await s.recv()
                    msgJson = json.loads(msg)
                    if msgJson[0]["ev"] == "status" and self.verbose:
                        print("status", msgJson[0]["message"])
                        continue
                    if not self.raw:
                        msg = parse(msgJson)

                    if isasync:
                        await processor(msg, s)
                    else:
                        processor(msg, s)
            except websockets.ConnectionClosedOK:
                if self.verbose:
                    print("connection closed (OK)")
                return
            except websockets.ConnectionClosedError:
                if self.verbose:
                    print("connection closed (error)")
                reconnects += 1
                if self.max_reconnects is not None and reconnects > self.max_reconnects:
                    return
                continue

    async def _subscribe(self, topics):
        if self.websocket is None or len(topics) == 0:
            return
        topics = ",".join(topics)
        if self.verbose:
            print("subbing", topics)
        await self.websocket.send(json.dumps({"action": "subscribe", "params": topics}))

    async def _unsubscribe(self, topics):
        if self.websocket is None or len(topics) == 0:
            return
        subs = ",".join(topics)
        if self.verbose:
            print("unsubbing", topics)
        await self.websocket.send(json.dumps({"action": "unsubscribe", "params": subs}))

    @staticmethod
    def _parse_subscription(s: str):
        s = s.strip()
        split = s.split(".")
        if len(split) != 2:
            print("invalid subscription", s)
            return [None, None]

        return split

    def subscribe(self, *subscriptions: str):
        for s in subscriptions:
            topic, sym = self._parse_subscription(s)
            if topic == None:
                continue
            if self.verbose:
                print("add", s)
            self.scheduled_subs.add(s)
            # If user subs to X.*, remove other X.\w+
            if sym == "*":
                for t in list(self.subs):
                    if t.startswith(topic):
                        self.scheduled_subs.discard(t)

        self.schedule_resub = True

    def unsubscribe(self, *subscriptions: str):
        for s in subscriptions:
            topic, sym = self._parse_subscription(s)
            if topic == None:
                continue
            if self.verbose:
                print("discard", s)
            self.scheduled_subs.discard(s)

            # If user unsubs to X.*, remove other X.\w+
            if sym == "*":
                for t in list(self.subs):
                    if t.startswith(topic):
                        self.scheduled_subs.discard(t)

        self.schedule_resub = True

    def unsubscribe_all(self):
        self.scheduled_subs = set()
        self.schedule_resub = True

    async def close(self):
        if self.verbose:
            print("closing")

        if self.websocket:
            await self.websocket.close()
            self.websocket = None
        else:
            print("no websocket open to close")
