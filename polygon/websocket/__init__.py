import os
from enum import Enum
from typing import Optional, Union, List, Set, Callable, Awaitable
import json
import inspect
import ssl
import certifi
from multiprocessing import AuthenticationError
from .models import *
from websockets.client import connect, WebSocketClientProtocol
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from websockets.typing import Data

env_key = "POLYGON_API_KEY"

class WebSocketClient:
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
        """
        Initialize a Polygon WebSocketClient.

        :param api_key: Your API keYour API key.
        :param feed: The feed to subscribe to (default RealTime)
        :param raw: The market to subscribe to (default Stocks)
        :param verbose: Whether to print client and server status messages.
        :param subscriptions: List of subscription parameters.
        :param max_reconnects: How many times to reconnect on network outage before ending .connect event loop.
        :return: A client.
        """
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
        self.websocket: Optional[WebSocketClientProtocol] = None
        self.scheduled_subs = set(subscriptions)
        self.schedule_resub = True

    # https://websockets.readthedocs.io/en/stable/reference/client.html#opening-a-connection
    async def connect(
        self,
        processor: Callable[[Union[List[WebSocketMessage], Data]], Optional[Awaitable]],
        close_timeout: int = 1,
        **kwargs,
    ):
        """
        Connect to websocket server and run `processor(msg)` on every new `msg`.

        :param processor: The callback to process messages.
        :param close_timeout: How long to wait for handshake when calling .close.
        """
        reconnects = 0
        isasync = inspect.iscoroutinefunction(processor)
        if self.verbose:
            print("connect:", self.url)
        # darwin needs some extra <3
        ssl_context = None
        if self.url.startswith("wss://"):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            ssl_context.load_verify_locations(certifi.where())

        async for s in connect(
            self.url, close_timeout=close_timeout, ssl=ssl_context, **kwargs
        ):
            self.websocket = s
            try:
                msg = await s.recv()
                if self.verbose:
                    print("connected:", msg)
                if self.verbose:
                    print("authing:")
                await s.send(json.dumps({"action": "auth", "params": self.api_key}))
                auth_msg = await s.recv()
                auth_msg_parsed = json.loads(auth_msg)
                if self.verbose:
                    print("authed:", auth_msg)
                try:
                    if auth_msg_parsed[0]["status"] == "auth_failed":
                        raise AuthenticationError(auth_msg_parsed[0]["message"])
                except (AuthenticationError):
                    exit("Authentication Failed. Exiting...")
                while True:
                    if self.schedule_resub:
                        if self.verbose:
                            print("reconciling:", self.subs, self.scheduled_subs)
                        new_subs = self.scheduled_subs.difference(self.subs)
                        await self._subscribe(new_subs)
                        old_subs = self.subs.difference(self.scheduled_subs)
                        await self._unsubscribe(old_subs)
                        self.subs = self.scheduled_subs
                        self.subs = set(self.scheduled_subs)
                        self.schedule_resub = False

                    cmsg: Union[List[WebSocketMessage], Data] = await s.recv()
                    # we know cmsg is Data
                    msgJson = json.loads(cmsg)  # type: ignore
                    for m in msgJson:
                        if m["ev"] == "status":
                            if self.verbose:
                                print("status:", m["message"])
                            continue
                    if not self.raw:
                        cmsg = parse(msgJson)

                    if len(cmsg) > 0:
                        if isasync:
                            # we know processor is Awaitable
                            await processor(cmsg)  # type: ignore
                        else:
                            processor(cmsg)
            except ConnectionClosedOK:
                if self.verbose:
                    print("connection closed (OK)")
                return
            except ConnectionClosedError:
                if self.verbose:
                    print("connection closed (error)")
                reconnects += 1
                if self.max_reconnects is not None and reconnects > self.max_reconnects:
                    return
                continue

    async def _subscribe(self, topics: Union[List[str], Set[str]]):
        if self.websocket is None or len(topics) == 0:
            return
        subs = ",".join(topics)
        if self.verbose:
            print("subbing:", subs)
        await self.websocket.send(json.dumps({"action": "subscribe", "params": subs}))

    async def _unsubscribe(self, topics: Union[List[str], Set[str]]):
        if self.websocket is None or len(topics) == 0:
            return
        subs = ",".join(topics)
        if self.verbose:
            print("unsubbing:", subs)
        await self.websocket.send(json.dumps({"action": "unsubscribe", "params": subs}))

    @staticmethod
    def _parse_subscription(s: str):
        s = s.strip()
        split = s.split(".")
        if len(split) != 2:
            print("invalid subscription:", s)
            return [None, None]

        return split

    def subscribe(self, *subscriptions: str):
        """
        Subscribe to given subscriptions.

        :param subscriptions: Subscriptions (args)
        """
        for s in subscriptions:
            topic, sym = self._parse_subscription(s)
            if topic == None:
                continue
            if self.verbose:
                print("add:", s)
            self.scheduled_subs.add(s)
            # If user subs to X.*, remove other X.\w+
            if sym == "*":
                for t in list(self.subs):
                    if t.startswith(topic):
                        self.scheduled_subs.discard(t)

        self.schedule_resub = True

    def unsubscribe(self, *subscriptions: str):
        """
        Unsubscribe from given subscriptions.

        :param subscriptions: Subscriptions (args)
        """
        for s in subscriptions:
            topic, sym = self._parse_subscription(s)
            if topic == None:
                continue
            if self.verbose:
                print("discard:", s)
            self.scheduled_subs.discard(s)

            # If user unsubs to X.*, remove other X.\w+
            if sym == "*":
                for t in list(self.subs):
                    if t.startswith(topic):
                        self.scheduled_subs.discard(t)

        self.schedule_resub = True

    def unsubscribe_all(self):
        """
        Unsubscribe from all subscriptions.
        """
        self.scheduled_subs = set()
        self.schedule_resub = True

    async def close(self):
        """
        Close the websocket connection.
        """
        if self.verbose:
            print("closing:")

        if self.websocket:
            await self.websocket.close()
            self.websocket = None
        else:
            print("no websocket open to close")
