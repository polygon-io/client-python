from .base import BaseClient
from typing import Optional, Any, Dict, List, Union, Iterator
from .models import (
    TickerSnapshot,
    Direction,
    OptionContractSnapshot,
    SnapshotMarketType,
    SnapshotTickerFullBook,
    UniversalSnapshot,
    IndicesSnapshot,
    Sort,
    Order,
)
from urllib3 import HTTPResponse

from .models.request import RequestOptionBuilder


def get_locale(market_type: Union[SnapshotMarketType, str]):
    if market_type == SnapshotMarketType.STOCKS.value:
        return "us"

    return "global"


class SnapshotClient(BaseClient):
    def list_universal_snapshots(
        self,
        type: Optional[Union[str, SnapshotMarketType]] = None,
        ticker_any_of: Optional[List[str]] = None,
        order: Optional[Union[str, Order]] = None,
        limit: Optional[int] = 10,
        sort: Optional[Union[str, Sort]] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[UniversalSnapshot], HTTPResponse]:
        """
        Get snapshots for assets of all types
        - https://polygon.io/docs/stocks/get_v3_snapshot
        - https://polygon.io/docs/options/get_v3_snapshot
        - https://polygon.io/docs/indices/get_v3_snapshot
        - https://polygon.io/docs/forex/get_v3_snapshot
        - https://polygon.io/docs/crypto/get_v3_snapshot

        """
        url = f"/v3/snapshot"
        return self._paginate(
            path=url,
            params=self._get_params(self.list_universal_snapshots, locals()),
            result_key="results",
            deserializer=UniversalSnapshot.from_dict,
            raw=raw,
            options=options,
        )

    def get_snapshot_all(
        self,
        market_type: Union[str, SnapshotMarketType],
        tickers: Optional[Union[str, List[str]]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        include_otc: Optional[bool] = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[List[TickerSnapshot], HTTPResponse]:
        
        
        locale = get_locale(market_type)
        url = f"/v2/snapshot/locale/{locale}/markets/{market_type}/tickers"
        if type(tickers) is list:
            tickers = ",".join(tickers)
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_all, locals()),
            deserializer=TickerSnapshot.from_dict,
            raw=raw,
            result_key="tickers",
            options=options,
        )

    def get_snapshot_direction(
        self,
        market_type: Union[str, SnapshotMarketType],
        direction: Union[str, Direction],
        params: Optional[Dict[str, Any]] = None,
        include_otc: Optional[bool] = False,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[List[TickerSnapshot], HTTPResponse]:
       
        locale = get_locale(market_type)
        url = f"/v2/snapshot/locale/{locale}/markets/{market_type}/{direction}"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_direction, locals()),
            result_key="tickers",
            deserializer=TickerSnapshot.from_dict,
            raw=raw,
            options=options,
        )

    def get_snapshot_ticker(
        self,
        market_type: Union[str, SnapshotMarketType],
        ticker: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[TickerSnapshot, HTTPResponse]:
        
        locale = get_locale(market_type)
        url = f"/v2/snapshot/locale/{locale}/markets/{market_type}/tickers/{ticker}"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_ticker, locals()),
            result_key="ticker",
            deserializer=TickerSnapshot.from_dict,
            raw=raw,
            options=options,
        )

    def get_snapshot_option(
        self,
        underlying_asset: str,
        option_contract: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[OptionContractSnapshot, HTTPResponse]:
        
        url = f"/v3/snapshot/options/{underlying_asset}/{option_contract}"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_option, locals()),
            result_key="results",
            deserializer=OptionContractSnapshot.from_dict,
            raw=raw,
            options=options,
        )

    def list_snapshot_options_chain(
        self,
        underlying_asset: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[OptionContractSnapshot], HTTPResponse]:
        
        url = f"/v3/snapshot/options/{underlying_asset}"
        return self._paginate(
            path=url,
            params=self._get_params(self.list_snapshot_options_chain, locals()),
            result_key="results",
            deserializer=OptionContractSnapshot.from_dict,
            raw=raw,
            options=options,
        )

    def get_snapshot_crypto_book(
        self,
        ticker: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[SnapshotTickerFullBook, HTTPResponse]:
        
        url = f"/v2/snapshot/locale/global/markets/crypto/tickers/{ticker}/book"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_crypto_book, locals()),
            result_key="data",
            deserializer=SnapshotTickerFullBook.from_dict,
            raw=raw,
            options=options,
        )

    def get_snapshot_indices(
        self,
        ticker_any_of: Optional[Union[str, List[str]]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[List[IndicesSnapshot], HTTPResponse]:
        url = f"/v3/snapshot/indices"

        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_indices, locals()),
            deserializer=IndicesSnapshot.from_dict,
            raw=raw,
            result_key="results",
            options=options,
        )
