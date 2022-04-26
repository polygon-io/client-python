from .base import BaseClient
from typing import Optional, Any, Dict, List, Union, Iterator
from .models import MarketHoliday, MarketStatus, Ticker, Sort, Order
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

class TickersClient(BaseClient):
    def list_tickers(
        self,
        ticker: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        type: Optional[str] = None,
        market: Optional[str] = None,
        exchange: Optional[str] = None,
        cusip: Optional[int] = None,
        cik: Optional[int] = None,
        date: Optional[str] = None,
        active: Optional[bool] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[Iterator[Ticker], HTTPResponse]:
        """
        Query all ticker symbols which are supported by Polygon.io. This API currently includes Stocks/Equities, Crypto, and Forex.

        :param ticker: Specify a ticker symbol. Defaults to empty string which queries all tickers.
        :param ticker_lt: Timestamp less than
        :param ticker_lte: Ticker less than or equal to
        :param ticker_gt: Ticker greater than
        :param ticker_gte: Ticker greater than or equal to
        :param type: Specify the type of the tickers. Find the types that we support via our Ticker Types API. Defaults to empty string which queries all types.
        :param market: Filter by market type. By default all markets are included.
        :param exchange: Specify the primary exchange of the asset in the ISO code format. Find more information about the ISO codes at the ISO org website. Defaults to empty string which queries all exchanges.
        :param cusip: Specify the CUSIP code of the asset you want to search for. Find more information about CUSIP codes at their website. Defaults to empty string which queries all CUSIPs.
        :param cik: Specify the CIK of the asset you want to search for. Find more information about CIK codes at their website. Defaults to empty string which queries all CIKs.
        :param date: Specify a point in time to retrieve tickers available on that date. Defaults to the most recent available date.
        :param search: Search for terms within the ticker and/or company name.
        :param active: Specify if the tickers returned should be actively traded on the queried date. Default is true.
        :param limit: Limit the size of the response, default is 100 and max is 1000.
        :param sort: The field to sort the results on. Default is ticker. If the search query parameter is present, sort is ignored and results are ordered by relevance.
        :param order: The order to sort the results on. Default is asc (ascending).
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: List of tickers
        :rtype: List[Ticker]
        """
        url = "/v3/reference/tickers"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_tickers, locals()),
            raw=raw,
            deserializer=Ticker.from_dict,
        )