import os
import json
import datetime
import asyncio
import uvloop
import logging
from polygon_streamer import PolygonStreamer

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class StocksStreamer(PolygonStreamer):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	async def callback(self, message_str):
		try:
			def mapper(message):
				if message["ev"] == "T":
					return {
						"event_type": message["ev"],
						"timestamp": datetime.datetime.fromtimestamp(message["t"] / 1000),
						"id": message["x"],
						"symbol": message["sym"],
						"price": message["p"],
						"size": message["s"],
						"conditions": message["c"]
					}
				else:
					return message

			return print([mapper(message) for message in json.loads(message_str)])

		except Exception as e:
			logging.error("{}".format(e.args))


def main():
	polygon_api_key = os.environ.get("polygon_api_key", "my-api-key")
	cluster = "/stocks"
	symbols_str = "T.*"
	streamer = StocksStreamer(api_key=polygon_api_key, cluster=cluster, symbols_str=symbols_str)
	streamer.start()


if __name__ == '__main__':
	main()
