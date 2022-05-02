import asyncio
from polygon import WebSocketClient

async def processor(msg):
    print('got msg', msg)

async def hello():
    print('making client')
    c = WebSocketClient(verbose=True)
    print('subscribe')
    c.subscribe(Topic.Trades, 'AAPL')
    print('connect')
    await c.connect(processor)

asyncio.run(hello())

