from .aggs import AggsClient
from .trades import TradesClient
from .quotes import QuotesClient
from .reference import MarketsClient


class RESTClient(AggsClient, TradesClient, QuotesClient, MarketsClient):
    pass
