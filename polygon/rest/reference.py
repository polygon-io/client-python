from polygon.rest.models.markets import MarketHoliday
from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import MarketHoliday
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
    

    