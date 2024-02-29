from polygon.rest.models.common import SeriesType
from polygon.rest.models.indicators import (
    SMAIndicatorResults,
    EMAIndicatorResults,
    RSIIndicatorResults,
    MACDIndicatorResults,
)
from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import Order
from urllib3 import HTTPResponse
from datetime import datetime, date

from .models.request import RequestOptionBuilder


class IndicatorsClient(BaseClient):
    def get_sma(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        timespan: Optional[str] = None,
        window: Optional[int] = None,
        adjusted: Optional[bool] = None,
        expand_underlying: Optional[bool] = None,
        order: Optional[Union[str, Order]] = None,
        limit: Optional[int] = None,
        params: Optional[Dict[str, Any]] = None,
        series_type: Optional[Union[str, SeriesType]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[SMAIndicatorResults, HTTPResponse]:
        url = f"/v1/indicators/sma/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_sma, locals()),
            result_key="results",
            deserializer=SMAIndicatorResults.from_dict,
            raw=raw,
            options=options,
        )

    def get_ema(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        timespan: Optional[str] = None,
        window: Optional[int] = None,
        adjusted: Optional[bool] = None,
        expand_underlying: Optional[bool] = None,
        order: Optional[Union[str, Order]] = None,
        limit: Optional[int] = None,
        params: Optional[Dict[str, Any]] = None,
        series_type: Optional[Union[str, SeriesType]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[EMAIndicatorResults, HTTPResponse]:

        url = f"/v1/indicators/ema/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_ema, locals()),
            result_key="results",
            deserializer=EMAIndicatorResults.from_dict,
            raw=raw,
            options=options,
        )

    def get_rsi(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        timespan: Optional[str] = None,
        window: Optional[int] = None,
        adjusted: Optional[bool] = None,
        expand_underlying: Optional[bool] = None,
        order: Optional[Union[str, Order]] = None,
        limit: Optional[int] = None,
        params: Optional[Dict[str, Any]] = None,
        series_type: Optional[Union[str, SeriesType]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[RSIIndicatorResults, HTTPResponse]:
        url = f"/v1/indicators/rsi/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_rsi, locals()),
            result_key="results",
            deserializer=RSIIndicatorResults.from_dict,
            raw=raw,
            options=options,
        )

    def get_macd(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        timespan: Optional[str] = None,
        short_window: Optional[int] = None,
        long_window: Optional[int] = None,
        signal_window: Optional[int] = None,
        adjusted: Optional[bool] = None,
        expand_underlying: Optional[bool] = None,
        order: Optional[Union[str, Order]] = None,
        limit: Optional[int] = None,
        params: Optional[Dict[str, Any]] = None,
        series_type: Optional[Union[str, SeriesType]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[MACDIndicatorResults, HTTPResponse]:

        url = f"/v1/indicators/macd/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_macd, locals()),
            result_key="results",
            deserializer=MACDIndicatorResults.from_dict,
            raw=raw,
            options=options,
        )
