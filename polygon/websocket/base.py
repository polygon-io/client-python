import os
from enum import Enum
from typing import Optional, Union, List
from .models import Feed, Market
import websockets
import json
import inspect
import asyncio

env_key = "POLYGON_API_KEY"


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
        **kwargs
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
        self.url = f"wss://{feed}/{market}"
        self.subscribed = False
        self.subs = set()
        self.max_reconnects = max_reconnects
        self.websocket = None
        self.scheduled_subs = set(subscriptions)
        self.schedule_resub = True
        print('subscriptions', subscriptions)
        print('scheduled_subs', subscriptions)

    # https://websockets.readthedocs.io/en/stable/reference/client.html#opening-a-connection
    async def connect_loop(self, processor, close_timeout=1, **kwargs):
        reconnects = 0
        isasync = inspect.iscoroutinefunction(processor)
        if self.verbose:
            print('connect', self.url)
        async for s in websockets.connect(self.url, close_timeout=close_timeout, **kwargs):
            self.websocket = s
            try:
                msg = await s.recv()
                if self.verbose:
                    print('connected', msg)
                if self.verbose:
                    print('authing')
                await s.send(json.dumps({"action":"auth","params":self.api_key}))
                msg = await s.recv()
                if self.verbose:
                    print('authed', msg)
                while True:
                    if self.schedule_resub:
                        print('reconciling', self.subs, self.scheduled_subs)
                        new_subs = self.scheduled_subs.difference(self.subs)
                        await self._subscribe(new_subs)
                        old_subs = self.subs.difference(self.scheduled_subs)
                        await self._unsubscribe(old_subs)
                        self.subs = self.scheduled_subs
                        print('reconciled')
                        self.schedule_resub = False

                    msg = await s.recv()
                    msgJson = json.loads(msg)
                    if msgJson[0]['ev'] == 'status' and self.verbose:
                        print('status', msgJson[0]['message'])
                        continue

                    if not self.raw:
                        msg = parse(msgJson)
                    if isasync:
                        await processor(msg, s)
                    else:
                        processor(msg, s)
            except websockets.ConnectionClosed:
                if self.verbose:
                    print('connection closed')
                reconnects += 1
                if self.max_reconnects is not None and reconnects > self.max_reconnects:
                    return
                continue

    async def connect(self, processor):
        self.loop_task = asyncio.create_task(self.connect_loop(processor))

    async def _subscribe(self, topics):
        if self.websocket is None or len(topics) == 0:
            return
        topics = ','.join(topics)
        if self.verbose:
            print('subbing', topics)
        await self.websocket.send(json.dumps({"action":"subscribe","params":topics}))
        #msg = await self.websocket.recv()
        #if self.verbose:
        #    print('subbed', msg)

    async def _unsubscribe(self, topics):
        if self.websocket is None or len(topics) == 0:
            return
        subs = ','.join(topics)
        if self.verbose:
            print('unsubbing', topics)
        await self.websocket.send(json.dumps({"action":"unsubscribe","params":subs}))
        #msg = await self.websocket.recv()
        #if self.verbose:
        #    print('unsubbed', msg)

    def subscribe(self, *subscriptions: str):
        for s in subscriptions:
            print('add', s)
            self.scheduled_subs.add(s)
        self.schedule_resub = True

    def unsubscribe(self, *subscriptions: str):
        for s in subscriptions:
            print('discard', s)
            self.scheduled_subs.discard(s)
        self.schedule_resub = True

    def unsubscribe_all(self):
        self.scheduled_subs = set()
        self.schedule_resub = True

    async def close(self):
        if self.verbose:
            print('closing')

        if self.loop_task:
            self.loop_task.cancel()
            self.loop_task = None
        else:
            print('no loop_task to cancel')

        if self.websocket:
            await self.websocket.close()
            self.websocket = None
        else:
            print('no websocket open to close')
