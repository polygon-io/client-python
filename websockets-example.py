from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, EquityTrade
from typing import List
# import logging
# logging.basicConfig(
#     format="%(asctime)s %(message)s",
#     level=logging.DEBUG,
# )

c = WebSocketClient(subscriptions=['T.*'])

# Sync
# def handle_msg(msgs: List[WebSocketMessage]):
#     for m in msgs:
#         print(m)
# 
# c.run(handle_msg)

# Sync aggs
# class MessageHandler:
#     count = 0
# 
#     def handle_msg(self, msgs: List[WebSocketMessage]):
#         for m in msgs:
#             if type(m) == EquityTrade:
#                 print(self.count, m)
#                 self.count += 1
# 
# h = MessageHandler()
# 
# def handle_msg(msgs: List[WebSocketMessage]):
#     h.handle_msg(msgs)
# 
# c.run(handle_msg)

# Async
# import asyncio
# async def handle_msg(msgs: List[WebSocketMessage]):
#     for m in msgs:
#         print(m)
# 
# async def timeout():
#     await asyncio.sleep(1)
#     print('unsubscribe_all')
#     c.unsubscribe_all()
#     await asyncio.sleep(1)
#     print('close')
#     await c.close()
# 
# async def main():
#     await asyncio.gather(
#         c.connect(handle_msg),
#         timeout()
#     )
# 
# asyncio.run(main())

# Raw
# import json
# from typing import Union
# 
# c = WebSocketClient(subscriptions=['T.*'], raw=True)
# 
# def handle_msg(msgs: Union[str, bytes]):
# 		print(json.loads(msgs))
# 
# c.run(handle_msg)
