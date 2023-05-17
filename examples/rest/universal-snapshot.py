from typing import cast, Iterator, Union

from urllib3 import HTTPResponse

from polygon import RESTClient
from polygon.rest.models import UniversalSnapshot, SnapshotMarketType

# docs
# https://polygon.io/docs/stocks/get_v3_snapshot
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used


def print_snapshots(iterator: Union[Iterator[UniversalSnapshot], HTTPResponse]):
    snapshots = [s for s in iterator]

    print(f"count: {len(snapshots)}")

    for item in snapshots:
        print(item)


# it = client.list_asset_snapshots() # all tickers for all assets types in lexicographical order

it = client.list_asset_snapshots(
    ticker_any_of=[
        "AAPL",
        "O:AAPL230519C00055000",
        "DOES_NOT_EXIST",
        "X:1INCHUSD",
        "C:AEDAUD",
    ]
)
print_snapshots(it)

it = client.list_asset_snapshots(
    market_type=SnapshotMarketType.STOCKS, ticker_gt="A", ticker_lt="AAPL"
)
print_snapshots(it)

it = client.list_asset_snapshots(
    market_type=SnapshotMarketType.STOCKS, ticker_gte="AAPL", ticker_lte="ABB"
)
print_snapshots(it)
