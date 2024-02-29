from .base import BaseClient
from typing import Optional, Any, Dict, Union, Iterator
from .models import StockFinancial, Timeframe, Sort, Order
from urllib3 import HTTPResponse
from datetime import datetime, date

from .models.request import RequestOptionBuilder


class VXClient(BaseClient):
    def list_stock_financials(
        self,
        ticker: Optional[str] = None,
        cik: Optional[str] = None,
        company_name: Optional[str] = None,
        company_name_search: Optional[str] = None,
        sic: Optional[str] = None,
        filing_date: Optional[Union[str, int, datetime, date]] = None,
        filing_date_lt: Optional[Union[str, int, datetime, date]] = None,
        filing_date_lte: Optional[Union[str, int, datetime, date]] = None,
        filing_date_gt: Optional[Union[str, int, datetime, date]] = None,
        filing_date_gte: Optional[Union[str, int, datetime, date]] = None,
        period_of_report_date: Optional[Union[str, int, datetime, date]] = None,
        period_of_report_date_lt: Optional[Union[str, int, datetime, date]] = None,
        period_of_report_date_lte: Optional[Union[str, int, datetime, date]] = None,
        period_of_report_date_gt: Optional[Union[str, int, datetime, date]] = None,
        period_of_report_date_gte: Optional[Union[str, int, datetime, date]] = None,
        timeframe: Optional[Union[str, Timeframe]] = None,
        include_sources: Optional[bool] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[StockFinancial], HTTPResponse]:
        
        url = "/vX/reference/financials"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_stock_financials, locals()),
            raw=raw,
            deserializer=StockFinancial.from_dict,
            options=options,
        )
