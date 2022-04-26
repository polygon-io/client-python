from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import Quote, LastQuote, Sort, Order
from urllib3 import HTTPResponse

# https://polygon.io/docs/stocks
class QuotesClient(BaseClient):
    def list_quotes(
        self,
        ticker: str,
        timestamp: Optional[str] = None,
        timestamp_lt: Optional[str] = None,
        timestamp_lte: Optional[str] = None,
        timestamp_gt: Optional[str] = None,
        timestamp_gte: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False
    ) -> Union[List[Quote], HTTPResponse]:
        """
        Get quotes for a ticker symbol in a given time range.

        :param ticker: The ticker symbol to get quotes for.
        :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
        :param timestamp_lt: Timestamp less than
        :param timestamp_lte: Timestamp less than or equal to
        :param timestamp_gt: Timestamp greater than
        :param timestamp_gte: Timestamp greater than or equal to
        :param limit: Limit the number of results returned, default is 10 and max is 50000.
        :param sort: Sort field used for ordering.
        :param order: Order results based on the sort field.
        :param params: Any additional query params
        :param raw: Return HTTPResponse object instead of results object
        :return: List of quotes
        :rtype: List[Quote]
        """
        url = f"/v3/quotes/{ticker}"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_quotes, locals()),
            raw=raw,
            deserializer=Quote.from_dict,
        )
    
    def get_last_quote(
        self,
        ticker: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False
    ) -> Union[LastQuote, HTTPResponse]:
        """
        Get the most recent NBBO (Quote) tick for a given stock.

        :param ticker: The ticker symbol of the stock/equity.
        :param params: Any additional query params
        :param raw: Return HTTPResponse object instead of results object
        :return: Last Quote
        :rtype: LastQuote
        """
        url = f"/v2/last/nbbo/{ticker}"

        return self._get(path=url, params=params, deserializer=LastQuote.from_dict, raw=raw)

    