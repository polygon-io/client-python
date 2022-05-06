Getting Started
===============

Requirements:
  - `Polygon.io API key <https://polygon.io/dashboard/api-keys>`_
  - `Python >= 3.7 <https://www.python.org/downloads/>`_
  - `This package <https://pypi.org/project/polygon-api-client/>`_

.. code-block:: shell

    pip install polygon-api-client

HTTP client usage
-----------------

.. automethod:: polygon.RESTClient.__init__

You can pass your API key via the environment variable :code:`POLYGON_API_KEY` or as the first parameter to the :code:`RESTClient` constructor:

.. code-block:: python

  from polygon import RESTClient

  client = RESTClient() # POLYGON_API_KEY is used
  client = RESTClient("api_key") # api_key is used

For non-paginated endpoints call :code:`get_*`:

.. code-block:: python

  aggs = client.get_aggs("AAPL", 1, "day", "2022-04-01", "2022-04-04")
  print(aggs)

For paginated endpoints call :code:`list_*` and use the provided iterator:

.. code-block:: python

  trades = []
  for t in client.list_trades("AAA", timestamp="2022-04-20", limit=5, sort=Sort.ASC)
      trades.append(t)
  print(trades)

.. note::
  The number of network requests made by the iterator depends on the value of the parameter :code:`limit`.
  :code:`limit` specifies how many results should be returned per network request. 
  You can see each network request by passing :code:`verbose = True` to the client. 

For endpoints that have a set of parameters you can use the provided :doc:`enums </Enums>`.

.. code-block:: python

  from polygon.rest.models import Sort

  client.list_trades(..., sort=Sort.ASC)

To handle the raw `urllib3 response <https://urllib3.readthedocs.io/en/stable/reference/urllib3.response.html?highlight=response#response) yourself, pass `raw=True>`_ yourself pass :code:`raw=True`:

.. code-block:: python

  aggs = client.get_aggs("AAPL", 1, "day", "2022-04-01", "2022-04-04", raw=True)
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

If it is a paginated :code:`list_*` response it's up to you to handle the "next_url" iteration:

.. code-block:: python

  trades = client.list_trades("AAA", timestamp="2022-04-20", limit=5)
  print(aggs.data)
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


Websocket client usage
----------------------

.. code-block:: python

  from polygon import WebSocketClient
  from polygon.websocket.models import Market, Feed, WebSocketMessage
  from typing import List
  import asyncio

  client = WebSocketClient(market=Market.Stocks, feed=Feed.RealTime) # Uses POLYGON_API_KEY env var. Can optionally supply your key.

.. note::
  Raises :code:`AuthError` if invalid API key is provided.

  client.subscribe('T.AAPL')

  async def handle_msg(msg: List[WebSocketMessage]):
    print(msg)

  asyncio.run(client.connect(handle_msg))

