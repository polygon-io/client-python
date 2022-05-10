from polygon import WebSocketClient
from typing import Union
import json

c = WebSocketClient(subscriptions=["T.*"], raw=True)


def handle_msg(msgs: Union[str, bytes]):
    print(json.loads(msgs))


c.run(handle_msg)
