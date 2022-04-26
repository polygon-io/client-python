from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import MarketHoliday, MarketStatus
from urllib3 import HTTPResponse

# https://polygon.io/docs/stocks
class MarketsClient(BaseClient):
    def list_market_holidays(
        self,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False
    ) -> Union[List[MarketHoliday], HTTPResponse]:
        """
        Get upcoming market holidays and their open/close times.

        :param params: Any additional query params
        :param raw: Return HTTPResponse object instead of results object
        :return: List of quotes
        :rtype: List[Quote]
        """
        url = "/v1/marketstatus/upcoming"

        return self._get(path=url, params=params, deserializer=MarketHoliday.from_dict, raw=raw)

    def get_market_status(
        self,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False
    ) -> Union[MarketStatus, HTTPResponse]:
        """
        Get the current trading status of the exchanges and overall financial markets.

        :param params: Any additional query params
        :param raw: Return HTTPResponse object instead of results object
        :return: List of quotes
        :rtype: List[Quote]
        """
        url = "/v1/marketstatus/now"

        return self._get(path=url, params=params, deserializer=MarketStatus.from_dict, raw=raw)
    

    