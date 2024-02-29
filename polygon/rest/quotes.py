from .base import BaseClient
from typing import Optional, Any, Dict, Union, Iterator
from .models import (
    Quote,
    LastQuote,
    LastForexQuote,
    RealTimeCurrencyConversion,
    Sort,
    Order,
    Precision,
)
from urllib3 import HTTPResponse
from datetime import datetime, date

from .models.request import RequestOptionBuilder


# https://polygon.io/docs/stocks
class QuotesClient(BaseClient):
    def list_quotes(
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
    ) -> Union[Iterator[Quote], HTTPResponse]:
    
        url = f"/v3/quotes/{ticker}"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_quotes, locals()),
            raw=raw,
            deserializer=Quote.from_dict,
            options=options,
        )

    def get_last_quote(
        self,
        ticker: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[LastQuote, HTTPResponse]:
        
        url = f"/v2/last/nbbo/{ticker}"

        return self._get(
            path=url,
            params=params,
            result_key="results",
            deserializer=LastQuote.from_dict,
            raw=raw,
            options=options,
        )

    def get_last_forex_quote(
        self,
        from_: str,
        to: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[LastForexQuote, HTTPResponse]:
        
        url = f"/v1/last_quote/currencies/{from_}/{to}"

        return self._get(
            path=url,
            params=params,
            deserializer=LastForexQuote.from_dict,
            raw=raw,
            options=options,
        )

    def get_real_time_currency_conversion(
        self,
        from_: str,
        to: str,
        amount: Optional[float] = None,
        precision: Union[int, Precision] = 2,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[RealTimeCurrencyConversion, HTTPResponse]:
        
        url = f"/v1/conversion/{from_}/{to}"

        return self._get(
            path=url,
            params=self._get_params(self.get_real_time_currency_conversion, locals()),
            deserializer=RealTimeCurrencyConversion.from_dict,
            raw=raw,
            options=options,
        )
