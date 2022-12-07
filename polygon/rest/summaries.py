from polygon.rest.models.summaries import (
    SummaryResult
)
from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import Order
from urllib3 import HTTPResponse
from datetime import datetime, date


class SummariesClient(BaseClient):
    def get_summaries(
        self,
        ticker_any_of: list[str],
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[SummaryResult, HTTPResponse]:
        """
        GetSummaries retrieves summaries for the ticker list with the given params.
        For more details see https://polygon.io/docs/stocks/get_v1_summaries.

        :param ticker_any_of: The ticker symbol
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: SummaryResults
        """

        url = f"/v1/summaries/"
        ticker_any_of = ','.join(ticker_any_of)
        return self._paginate(
            path=url,
            params=self._get_params(self.get_summaries, locals()),
            deserializer=SummaryResult.from_dict,
            raw=raw,
        )


