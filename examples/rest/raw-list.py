from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse

client = RESTClient(verbose=True)

trades = cast(
    HTTPResponse,
    client.list_trades(ticker="AAA", timestamp="2022-04-20", limit=5, raw=True),
)
print(trades.data)
# b'{
#  "results": [
#    {
#      "conditions": [
#        15
#      ],
#      "exchange": 11,
#      "id": "52983575627601",
#      "participant_timestamp": 1650499200029279200,
#      "price": 24.875,
#      "sequence_number": 1591291,
#      "sip_timestamp": 1650499200029316600,
#      "size": 100,
#      "tape": 1
#    },
#    {
#      "conditions": [
#        38,
#        41
#      ],
#      "exchange": 11,
#      "id": "52983575627600",
#      "participant_timestamp": 1650499200029279200,
#      "price": 24.875,
#      "sequence_number": 1591290,
#      "sip_timestamp": 1650499200029316600,
#      "tape": 1
#    },
#    {
#      "conditions": [
#        15
#      ],
#      "exchange": 11,
#      "id": "52983575622470",
#      "participant_timestamp": 1650493800003024000,
#      "price": 24.875,
#      "sequence_number": 1571279,
#      "sip_timestamp": 1650493800003645400,
#      "size": 100,
#      "tape": 1
#    },
#    {
#      "conditions": [
#        38,
#        41
#      ],
#      "exchange": 11,
#      "id": "52983575622469",
#      "participant_timestamp": 1650493800003024000,
#      "price": 24.875,
#      "sequence_number": 1571276,
#      "sip_timestamp": 1650493800003635500,
#      "tape": 1
#    },
#    {
#      "conditions": [
#        15
#      ],
#      "exchange": 11,
#      "id": "52983575556178",
#      "participant_timestamp": 1650485400002987800,
#      "price": 24.875,
#      "sequence_number": 1536223,
#      "sip_timestamp": 1650485400003870000,
#      "size": 100,
#      "tape": 1
#    }
#  ],
#  "status": "OK",
#  "request_id": "618bb99e7a632ed9f55454a541404b44",
#  "next_url": "https://api.polygon.io/v3/trades/AAA?cursor=YXA9NSZhcz0mbGltaXQ9NSZvcmRlcj1kZXNjJnNvcnQ9dGltZXN0YW1wJnRpbWVzdGFtcC5ndGU9MjAyMi0wNC0yMFQwNCUzQTAwJTNBMDBaJnRpbWVzdGFtcC5sdGU9MjAyMi0wNC0yMFQyMCUzQTEwJTNBMDAuMDAzODY5OTUyWg"
# }'
