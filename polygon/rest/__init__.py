from .aggs import AggsClient
from .trades import TradesClient
from .quotes import QuotesClient
from .reference import MarketsClient, TickersClient


class RESTClient(AggsClient, TradesClient, QuotesClient, MarketsClient, TickersClient):
    pass
