from polygon import WebSocketClient
import unittest
import asyncio
from mock_server import run_mock_server, port

unittest.util._MAX_LENGTH = 30000  # type: ignore


# https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase
class BaseTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        print("setup")
        self.maxDiff = None
        self.c = WebSocketClient(feed=f"localhost:{port}", verbose=True, secure=False)
        loop = asyncio.get_event_loop()
        loop.create_task(run_mock_server())

    async def asyncTearDown(self):
        print("teardown")
        await self.c.close()
