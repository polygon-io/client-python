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

.. literalinclude:: ../../examples/rest/simple-get.py

For paginated endpoints call :code:`list_*` and use the provided iterator:

.. literalinclude:: ../../examples/rest/simple-list.py

.. note::
  The number of network requests made by the iterator depends on the value of the parameter :code:`limit`.
  :code:`limit` specifies how many results should be returned per network request. 
  You can see each network request by passing :code:`verbose = True` to the client. 

For endpoints that have a set of parameters you can use the provided :doc:`enums </Enums>`.

.. code-block:: python

  from polygon.rest.models import Sort

  client.list_trades(..., sort=Sort.ASC)

To handle the raw `urllib3 response <https://urllib3.readthedocs.io/en/stable/reference/urllib3.response.html?highlight=response#response) yourself, pass `raw=True>`_ yourself pass :code:`raw=True`:

.. literalinclude:: ../../examples/rest/raw-get.py

If it is a paginated :code:`list_*` response it's up to you to handle the "next_url" iteration:

.. literalinclude:: ../../examples/rest/raw-list.py

WebSocket client usage
----------------------

.. automethod:: polygon.WebSocketClient.__init__

The simplest way to use the websocket client is to just provide a callback:

.. literalinclude:: ../../examples/websocket/simple.py

.. note::
  Raises :code:`AuthError` if invalid API key is provided.

If you want to capture state you can use a global variable inside the callback.
Alternatively, you can wrap a class method in a closure.

.. literalinclude:: ../../examples/websocket/aggs.py

Under the hood our client uses an asynchronous runtime. To manage the runtime
yourself (including unsubscribing and subscribing) you can use asyncio and the
:code:`.connect` method:

.. literalinclude:: ../../examples/websocket/async.py

To handle raw messages yourself pass `raw=True`:

.. literalinclude:: ../../examples/websocket/raw.py

