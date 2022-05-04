from polygon.rest.models import Condition
from base_ws import BaseTest
import asyncio

count = 0


async def processor(msg, _):
    global count, c
    print(count)
    count += 1


class ConditionsTest(BaseTest):
    async def test_sub(self):
        self.c.subscribe("T.AAPL")
        loop = asyncio.get_event_loop()
        loop.create_task(self.c.connect(processor))
        await asyncio.sleep(30)
        print("unsubscribe_all")
        self.c.unsubscribe_all()
        print("subscribe T.*")
        self.c.subscribe("T.*")
        await asyncio.sleep(3)
        print("unsubscribe T.*")
        self.c.unsubscribe("T.*")
