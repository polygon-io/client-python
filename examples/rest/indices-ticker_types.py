from typing import Optional, Union, List
from urllib3 import HTTPResponse
from polygon import RESTClient
from polygon.rest.models import (
    TickerTypes,
)

# docs
# https://polygon.io/docs/indices/get_v3_reference_tickers_types
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-types

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

types: Optional[Union[List[TickerTypes], HTTPResponse]] = None

try:
    types = client.get_ticker_types("indices")
except TypeError as e:
    if "not NoneType" in str(e):
        print("None found")
        types = None
    else:
        raise

if types is not None:
    print(types)
