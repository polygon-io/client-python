from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import Agg, Sort

# https://polygon.io/docs/stocks
class AggsClient(BaseClient):
    def get_aggs(self,
        ticker: str,
        multiplier: int,
        timespan: str,
        # "from" is a keyword in python https://www.w3schools.com/python/python_ref_keywords.asp
        from_: str,
        to: str,
        adjusted: Optional[bool]=None,
        sort: Optional[Union[str, Sort]]=None,
        limit: Optional[int]=None,
        params: Optional[Dict[str, Any]]=None,
        raw: bool=False
    ) -> List[Agg]:
        """
        Get aggregate bars for a ticker over a given date range in custom time window sizes.

        :param ticker: The ticker symbol.
        :param multiplier: The size of the timespan multiplier.
        :param timespan: The size of the time window.
        :param _from: The start of the aggregate time window.
        :param to: The end of the aggregate time window.
        :param adjusted: Whether or not the results are adjusted for splits. By default, results are adjusted. Set this to false to get results that are NOT adjusted for splits.
        :param sort: Sort the results by timestamp. asc will return results in ascending order (oldest at the top), desc will return results in descending order (newest at the top).The end of the aggregate time window.
        :param limit: Limits the number of base aggregates queried to create the aggregate results. Max 50000 and Default 5000. Read more about how limit is used to calculate aggregate results in our article on Aggregate Data API Improvements.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: List of aggregates
        :rtype: List[Agg]
        """
        url = f"/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_}/{to}"

        return self._get(path=url, params=self._get_params(self.get_aggs, locals()), resultKey="results", deserializer=Agg.from_dict, raw=raw)

