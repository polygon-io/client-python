import asyncio
from polygon import WebSocketClient
from polygon.websocket.models import Market, Feed, WebSocketMessage
# import logging
# logging.basicConfig(
#     format="%(asctime)s %(message)s",
#     level=logging.DEBUG,
# )

count = 0
c = WebSocketClient(market=Market.Stocks, feed=Feed.RealTime)
c.subscribe('T.AAPL')

async def handle_msg(msg: WebSocketMessage):
    global count, c
    print(count, msg)
    count += 1

async def timeout():
    await asyncio.sleep(1)
    print('unsubscribe_all')
    c.unsubscribe_all()
    await asyncio.sleep(1)
    print('close')
    await c.close()

async def main():
    await asyncio.gather(
        c.connect(handle_msg),
        timeout()
    )

asyncio.run(main())

