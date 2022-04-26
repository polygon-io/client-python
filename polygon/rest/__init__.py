from .aggs import AggsClient
from .trades import TradesClient
from .quotes import QuotesClient


class RESTClient(AggsClient, TradesClient, QuotesClient):
    pass
