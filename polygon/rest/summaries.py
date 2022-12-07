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


class SummariesClient(BaseClient):
    def get_summaries(
        self,
        ticker_any_of: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[SMAIndicatorResults, HTTPResponse]:
        """
        GetSummaries retrieves summaries for the ticker list with the given params.
        For more details see https://polygon.io/docs/stocks/get_v1_summaries.

        :param ticker_any_of: The ticker symbol
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :return: SummaryResults
        """

        url = f"/v1/summaries/"

        return self._get(
            path=url,
            params=self._get_params(self.get_sma, locals()),
            result_key="results",
            deserializer=SMAIndicatorResults.from_dict,
            raw=raw,
        )


