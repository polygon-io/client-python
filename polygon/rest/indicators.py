from polygon.rest.models.common import SeriesType
from polygon.rest.models.indicators import SingleIndicatorResults, MACDIndicatorResults
from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import Order
from urllib3 import HTTPResponse
from datetime import datetime, date


class IndicatorsClient(BaseClient):
    def get_sma(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        multiplier: Optional[int] = None,
        timespan: Optional[str] = None,
        window: Optional[int] = None,
        adjusted: Optional[bool] = None,
        expand_underlying: Optional[bool] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        series_type: Optional[Union[str, SeriesType]] = None,
        raw: bool = False,
    ) -> Union[SingleIndicatorResults, HTTPResponse]:
        """
        Get SMA values for a given ticker over a given range with the specified parameters.

        :param ticker: The ticker symbol.
        :param multiplier: The size of the timespan multiplier used to create underlying aggregates.
        :param timespan: The size of the underlying aggregate time window.
        :param timestamp: Either a date with the format YYYY-MM-DD or a millisecond timestamp.
        :param timestamp_lt: Timestamp less than
        :param timestamp_lte: Timestamp less than or equal to
        :param timestamp_gt: Timestamp greater than
        :param timestamp_gte: Timestamp greater than or equal to
        :param adjusted: Whether or not the underlying aggregates are adjusted for splits. By default, the aggregates used to calculate this indicator are adjusted. Set this to false to get results that are NOT adjusted for splits.
        :param Order: Sort the results by timestamp. asc will return results in ascending order (oldest at the top), desc will return results in descending order (newest at the top).The end of the aggregate time window.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: List of aggregates
        """

        url = f"/v1/indicators/sma/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_sma, locals()),
            result_key="results",
            deserializer=SingleIndicatorResults.from_dict,
            raw=raw,
        )



    