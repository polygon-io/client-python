from .base import BaseClient
from typing import Optional, Any, Dict, Union, Iterator
from .models import Trade, LastTrade, CryptoTrade, Sort, Order
from urllib3 import HTTPResponse
from datetime import datetime, date

from .models.request import RequestOptionBuilder


class TradesClient(BaseClient):
    def list_trades(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[Trade], HTTPResponse]:
        
        url = f"/v3/trades/{ticker}"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_trades, locals()),
            raw=raw,
            deserializer=Trade.from_dict,
            options=options,
        )

    def get_last_trade(
        self,
        ticker: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[LastTrade, HTTPResponse]:
       
        url = f"/v2/last/trade/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_last_trade, locals()),
            result_key="results",
            deserializer=LastTrade.from_dict,
            raw=raw,
            options=options,
        )

    def get_last_crypto_trade(
        self,
        from_: str,
        to: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[CryptoTrade, HTTPResponse]:
       
        url = f"/v1/last/crypto/{from_}/{to}"

        return self._get(
            path=url,
            params=self._get_params(self.get_last_crypto_trade, locals()),
            result_key="last",
            deserializer=CryptoTrade.from_dict,
            raw=raw,
            options=options,
        )
