from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse

client = RESTClient()

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        "AAPL",
        1,
        "day",
        "2022-04-01",
        "2022-04-04",
        raw=True,
    ),
)
print(aggs.geturl())
# https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2022-04-01/2022-04-04
print(aggs.status)
# 200
print(aggs.data)
# b'{
#    "ticker": "AAPL",
#    "queryCount": 2,
#    "resultsCount": 2,
#    "adjusted": true,
#    "results": [
#      {
#        "v": 78251328,
#        "vw": 173.4143,
#        "o": 174.03,
#        "c": 174.31,
#        "h": 174.88,
#        "l": 171.94,
#        "t": 1648785600000,
#        "n": 661160
#      },
#      {
#        "v": 76545983,
#        "vw": 177.4855,
#        "o": 174.57,
#        "c": 178.44,
#        "h": 178.49,
#        "l": 174.44,
#        "t": 1649044800000,
#        "n": 630374
#      }
#    ],
#    "status": "OK",
#    "request_id": "d8882a9d5194978819777f49c44b09c6",
#    "count": 2
#  }'
