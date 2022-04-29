from .aggs import AggsClient
from .trades import TradesClient
from .quotes import QuotesClient
from .snapshot import SnapshotClient
from .reference import (
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
)


class RESTClient(
    AggsClient,
    TradesClient,
    QuotesClient,
    SnapshotClient,
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
):
    pass
