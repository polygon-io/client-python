import asyncio
from polygon import WebSocketClient
import logging
logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
)

count = 0
c = WebSocketClient(verbose=True, raw=True, subscriptions=['T.AAPL'])

async def processor(msg, _):
    global count, c
    print(count, msg)
    count += 1

async def timeout():
    await asyncio.sleep(3)
    print('unsubscribe_all')
    #c.unsubscribe_all()
    c.unsubscribe('T.*')
    await asyncio.sleep(3)
    print('close')
    await c.close()

async def main():
    await asyncio.gather(
        c.connect(processor),
        timeout()
    )

asyncio.run(main())

