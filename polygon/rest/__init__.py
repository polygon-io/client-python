from .aggs import AggsClient
from .futures import FuturesClient
from .benzinga import BenzingaClient
from .economy import EconomyClient
from .tmx import TmxClient
from .trades import TradesClient
from .quotes import QuotesClient
from .snapshot import SnapshotClient
from .indicators import IndicatorsClient
from .summaries import SummariesClient
from .reference import (
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
    ContractsClient,
)
from .vX import VXClient
from .fundamentals import FundamentalsClient
from typing import Optional, Any
import os

BASE = "https://api.polygon.io"
ENV_KEY = "POLYGON_API_KEY"


class RESTClient(
    AggsClient,
    FuturesClient,
    BenzingaClient,
    EconomyClient,
    TmxClient,
    TradesClient,
    QuotesClient,
    SnapshotClient,
    MarketsClient,
    TickersClient,
    SplitsClient,
    DividendsClient,
    ConditionsClient,
    ExchangesClient,
    ContractsClient,
    IndicatorsClient,
    SummariesClient,
    FundamentalsClient,
):
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(ENV_KEY),
        connect_timeout: float = 10.0,
        read_timeout: float = 10.0,
        num_pools: int = 10,
        retries: int = 3,
        base: str = BASE,
        pagination: bool = True,
        verbose: bool = False,
        trace: bool = False,
        custom_json: Optional[Any] = None,
    ):
        super().__init__(
            api_key=api_key,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            num_pools=num_pools,
            retries=retries,
            base=base,
            pagination=pagination,
            verbose=verbose,
            trace=trace,
            custom_json=custom_json,
        )
        # Deprecated - use self.fundamentals instead
        self.vx = VXClient(
            api_key=api_key,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            num_pools=num_pools,
            retries=retries,
            base=base,
            pagination=pagination,
            verbose=verbose,
            trace=trace,
            custom_json=custom_json,
        )
