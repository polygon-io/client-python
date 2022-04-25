from .aggs import AggsClient
from .trades import TradesClient

class RESTClient(AggsClient, TradesClient):
    pass

