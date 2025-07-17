from typing import Optional, Any, Dict, List, Union, Iterator
from urllib3 import HTTPResponse
from datetime import datetime, date

from .base import BaseClient
from .models.economy import (
    FedInflation,
    TreasuryYield,
)
from .models.common import Sort, Order
from .models.request import RequestOptionBuilder


class EconomyClient(BaseClient):
    """
    Client for the Fed REST Endpoints
    (aligned with the paths from /fed/v1/...)
    """

    def list_treasury_yields(
        self,
        date: Optional[str] = None,
        date_any_of: Optional[str] = None,
        date_gt: Optional[str] = None,
        date_gte: Optional[str] = None,
        date_lt: Optional[str] = None,
        date_lte: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[List[TreasuryYield], HTTPResponse]:
        """
        Retrieve treasury yield data.

        :param date: Calendar date of the yield observation (YYYY-MM-DD).
        :param date_any_of: Filter equal to any of the values.
        :param date_gt: Filter for dates greater than the provided date.
        :param date_gte: Filter for dates greater than or equal to the provided date.
        :param date_lt: Filter for dates less than the provided date.
        :param date_lte: Filter for dates less than or equal to the provided date.
        :param limit: Limit the number of results returned. Default 100, max 50000.
        :param sort: Field to sort by (e.g., "date"). Default "date".
        :param order: Order results based on the sort field ("asc" or "desc"). Default "desc".
        :param params: Additional query parameters.
        :param raw: Return raw HTTPResponse object if True, else return List[TreasuryYield].
        :param options: RequestOptionBuilder for additional headers or params.
        :return: A list of TreasuryYield objects or HTTPResponse if raw=True.
        """
        url = "/fed/v1/treasury-yields"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_treasury_yields, locals()),
            deserializer=TreasuryYield.from_dict,
            raw=raw,
            result_key="results",
            options=options,
        )

    def list_inflation(
        self,
        date: Optional[Union[str, date]] = None,
        date_any_of: Optional[str] = None,
        date_gt: Optional[Union[str, date]] = None,
        date_gte: Optional[Union[str, date]] = None,
        date_lt: Optional[Union[str, date]] = None,
        date_lte: Optional[Union[str, date]] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FedInflation], HTTPResponse]:
        """
        Endpoint: GET /fed/v1/inflation
        """
        url = "/fed/v1/inflation"
        return self._paginate(
            path=url,
            params=self._get_params(self.list_inflation, locals()),
            raw=raw,
            deserializer=FedInflation.from_dict,
            options=options,
        )
