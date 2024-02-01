import asyncio
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, Union
from polygon import RESTClient, WebSocketClient
from polygon.websocket.models import Market, Feed


class ApiCallHandler:
    def __init__(self):
        self.api_call_queue = asyncio.Queue()
        self.executor = ThreadPoolExecutor()  # Thread pool for running synchronous code
        self.client = RESTClient()  # Assumes POLYGON_API_KEY is set in the environment

    async def enqueue_api_call(self, options_ticker):
        await self.api_call_queue.put(options_ticker)

    async def start_processing_api_calls(self):
        while True:
            options_ticker = await self.api_call_queue.get()
            try:
                # TODO:
                # Here, you can process the rest api requets as needed
                # Example: Get the options contract for this
                contract = await asyncio.get_running_loop().run_in_executor(
                    self.executor, self.get_options_contract, options_ticker
                )
                print(contract)  # Or process the contract data as needed
            except Exception as e:
                logging.error(f"Error processing API call for {options_ticker}: {e}")
            finally:
                self.api_call_queue.task_done()

    def get_options_contract(self, options_ticker):
        return self.client.get_options_contract(options_ticker)


class MessageHandler:
    def __init__(self, api_call_handler):
        self.handler_queue = asyncio.Queue()
        self.api_call_handler = api_call_handler

    async def add(self, message_response: Optional[Union[str, bytes]]) -> None:
        await self.handler_queue.put(message_response)

    async def start_handling(self) -> None:
        while True:
            message_response = await self.handler_queue.get()
            logging.info(f"Received message: {message_response}")
            try:
                # TODO:
                # Here, you can process the websocket messages as needed
                # Example: Extract ticker symbol and enqueue REST API call
                # to get the options contract for this trade (non-blocking)
                for trade in message_response:
                    ticker = self.extract_symbol(trade.symbol)
                    if ticker == "NVDA":
                        asyncio.create_task(
                            self.api_call_handler.enqueue_api_call(trade.symbol)
                        )
            except Exception as e:
                logging.error(f"Error handling message: {e}")
            finally:
                self.handler_queue.task_done()

    def extract_symbol(self, input_string):
        match = re.search(r"O:([A-Z]+)", input_string)
        if match:
            return match.group(1)
        else:
            return None


class MyClient:
    def __init__(self, feed, market, subscriptions):
        api_key = os.getenv("POLYGON_API_KEY")
        self.polygon_websocket_client = WebSocketClient(
            api_key=api_key,
            feed=feed,
            market=market,
            verbose=True,
            subscriptions=subscriptions,
        )
        self.api_call_handler = ApiCallHandler()
        self.message_handler = MessageHandler(self.api_call_handler)

    async def start_event_stream(self):
        try:
            await asyncio.gather(
                self.polygon_websocket_client.connect(self.message_handler.add),
                self.message_handler.start_handling(),
                self.api_call_handler.start_processing_api_calls(),
            )
        except Exception as e:
            logging.error(f"Error in event stream: {e}")


async def main():
    logging.basicConfig(level=logging.INFO)
    my_client = MyClient(
        feed=Feed.RealTime, market=Market.Options, subscriptions=["T.*"]
    )
    await my_client.start_event_stream()


# Entry point for the asyncio program
asyncio.run(main())
