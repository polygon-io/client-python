import os
from enum import Enum
from typing import Optional, Union, List
from .models import Feed, Market
import websockets
import json

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
        max_reconnects: int = 5,
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
        self.subscriptions = set(subscriptions)
        self.max_reconnects = max_reconnects

    # https://websockets.readthedocs.io/en/stable/reference/client.html#opening-a-connection
    async def connect(self, processor):
        reconnects = 0
        if self.verbose:
            print('connect', self.url)
        async for s in websockets.connect(self.url):
            try:
                if self.verbose:
                    print('authing')
                await s.send(json.dumps({"action":"auth","params":self.api_key}))
                msg = await s.recv()
                if self.verbose:
                    print('authed', msg)
                subs = ','.join(self.subscriptions)
                if self.verbose:
                    print('subbing', subs)
                await s.send(json.dumps({"action":"subscribe","params":subs}))
                msg = await s.recv()
                if self.verbose:
                    print('subbed', msg)
                async for msg in s:
                    await processor(msg)
            except websockets.ConnectionClosed:
                if self.verbose:
                    print('connection closed')
                reconnects += 1
                if reconnects > self.max_reconnects:
                    return
                continue
    
    def subscribe(self, *subscriptions: str):
        for s in subscriptions:
            self.subscriptions.add(s)

    def unsubscribe(self, *subscriptions: str):
        for s in subscriptions:
            self.subscriptions.discard(s)


    def unsubscribe_all(self):
        self.subscriptions = set()
