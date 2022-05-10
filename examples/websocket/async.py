from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List
import asyncio

c = WebSocketClient(subscriptions=["T.*"])


async def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


async def timeout():
    await asyncio.sleep(1)
    print("unsubscribe_all")
    c.unsubscribe_all()
    await asyncio.sleep(1)
    print("close")
    await c.close()


async def main():
    await asyncio.gather(c.connect(handle_msg), timeout())


asyncio.run(main())
