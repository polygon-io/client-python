import json
import asyncio
import uvloop
import websockets
import logging

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class PolygonStreamer(object):
	""" https://polygon.io/sockets
	"""
	url = "wss://socket.polygon.io"

	def __init__(self, api_key: str, cluster: str, symbols_str: str, number_workers: int=50, timeout: int=5):
		if cluster not in ("/stocks", "/forex", "/crypto"):
			raise ValueError("invalid cluster type")

		self._api_key = api_key
		self._cluster = cluster
		self._symbols_str = symbols_str
		self._number_workers = number_workers
		self._timeout = timeout
		self.queue = asyncio.Queue()

	async def connect(self):
		while True:
			async with websockets.connect(self.url + self._cluster, max_queue=4 * 2**10,) as websocket:
				await websocket.send(json.dumps({"action": "auth", "params": self._api_key}))
				await websocket.send(json.dumps({"action": "subscribe", "params": self._symbols_str}))
				logging.info("connected: {}".format(websocket.remote_address))
				while(True):
					try:
						message_str = await asyncio.wait_for(websocket.recv(), timeout=self._timeout)
						# await self.queue.put(message_str)
						self.queue.put_nowait(message_str)
					except asyncio.TimeoutError:
						logging.warn("timeout error - no data in {} seconds, pinging connection".format(self._timeout))
						pong_waiter = await asyncio.wait_for(websocket.ping(data="keepalive"), timeout=self._timeout)
						await asyncio.wait_for(pong_waiter, timeout=2 * self._timeout)
						logging.warn('ping/pong received, keeping connection alive...')
					except Exception as e:
						error_message = "resetting connection: {}".format(e.args)
						logging.error(error_message)
						raise Exception(error_message)

	async def callback(self, message_str):
		raise NotImplementedError

	async def message_handler(self):
		while True:
			message_str = await self.queue.get()
			await self.callback(message_str)
			queue_size = self.queue.qsize()
			if queue_size > 100:
				logging.warn("queue size: {}".format(queue_size))
			self.queue.task_done()

	def start(self):
		tasks = []
		tasks.append(self.connect())
		for i in range(self._number_workers):
			tasks.append(self.message_handler())
		self.loop = asyncio.get_event_loop()
		self.loop.run_until_complete(asyncio.gather(*tasks))
