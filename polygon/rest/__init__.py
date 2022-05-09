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
from .vX import VXClient
from typing import Optional
import os


base = "https://api.polygon.io"
env_key = "POLYGON_API_KEY"


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
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(env_key),
        connect_timeout: float = 10.0,
        read_timeout: float = 10.0,
        num_pools: int = 10,
        retries: int = 3,
        base: str = base,
        verbose: bool = False,
    ):
        super().__init__(
            api_key=api_key,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            num_pools=num_pools,
            retries=retries,
            base=base,
            verbose=verbose,
        )
        self.vX = VXClient(
            api_key=api_key,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            num_pools=num_pools,
            retries=retries,
            base=base,
            verbose=verbose,
        )
