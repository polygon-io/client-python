from .base import BaseClient
from typing import Optional, Any, Dict, List, Union, Iterator
from .models import (
    BalanceSheet,
    CashFlowStatement,
    IncomeStatement,
    FinancialRatios,
    ShortInterest,
    ShortVolume,
    Sort,
    Order,
)
from urllib3 import HTTPResponse
from datetime import datetime, date
from .models.request import RequestOptionBuilder


class FundamentalsClient(BaseClient):
    """
    Client for accessing Polygon's new fundamentals endpoints.
    This replaces the deprecated VXClient for financial data.
    """

    def list_balance_sheets(
        self,
        cik: Optional[str] = None,
        tickers: Optional[str] = None,
        period_end: Optional[Union[str, date]] = None,
        fiscal_year: Optional[int] = None,
        fiscal_quarter: Optional[int] = None,
        timeframe: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[BalanceSheet], HTTPResponse]:
        """
        Retrieve comprehensive balance sheet data for public companies.

        :param cik: The company's Central Index Key (CIK).
        :param tickers: Filter for arrays that contain the ticker value.
        :param period_end: The last date of the reporting period (YYYY-MM-DD).
        :param fiscal_year: The fiscal year for the reporting period.
        :param fiscal_quarter: The fiscal quarter number (1, 2, 3, or 4).
        :param timeframe: The reporting period type. Possible values: quarterly, annual.
        :param limit: Limit the number of results returned per-page, default is 100 and max is 50000.
        :param sort: Sort field used for ordering.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :param options: RequestOptionBuilder for additional headers or params.
        :return: Iterator of balance sheet records
        """
        url = "/stocks/financials/v1/balance-sheets"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_balance_sheets, locals()),
            raw=raw,
            deserializer=BalanceSheet.from_dict,
            options=options,
        )

    def list_cash_flow_statements(
        self,
        cik: Optional[str] = None,
        period_end: Optional[Union[str, date]] = None,
        tickers: Optional[str] = None,
        fiscal_year: Optional[int] = None,
        fiscal_quarter: Optional[int] = None,
        timeframe: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[CashFlowStatement], HTTPResponse]:
        """
        Retrieve comprehensive cash flow statement data for public companies.

        :param cik: The company's Central Index Key (CIK).
        :param period_end: The last date of the reporting period (YYYY-MM-DD).
        :param tickers: Filter for arrays that contain the ticker value.
        :param fiscal_year: The fiscal year for the reporting period.
        :param fiscal_quarter: The fiscal quarter number (1, 2, 3, or 4).
        :param timeframe: The reporting period type. Possible values: quarterly, annual, trailing_twelve_months.
        :param limit: Limit the number of results returned per-page, default is 100 and max is 50000.
        :param sort: Sort field used for ordering.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :param options: RequestOptionBuilder for additional headers or params.
        :return: Iterator of cash flow statement records
        """
        url = "/stocks/financials/v1/cash-flow-statements"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_cash_flow_statements, locals()),
            raw=raw,
            deserializer=CashFlowStatement.from_dict,
            options=options,
        )

    def list_income_statements(
        self,
        cik: Optional[str] = None,
        tickers: Optional[str] = None,
        period_end: Optional[Union[str, date]] = None,
        fiscal_year: Optional[int] = None,
        fiscal_quarter: Optional[int] = None,
        timeframe: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[IncomeStatement], HTTPResponse]:
        """
        Retrieve comprehensive income statement data for public companies.

        :param cik: The company's Central Index Key (CIK).
        :param tickers: Filter for arrays that contain the ticker value.
        :param period_end: The last date of the reporting period (YYYY-MM-DD).
        :param fiscal_year: The fiscal year for the reporting period.
        :param fiscal_quarter: The fiscal quarter number (1, 2, 3, or 4).
        :param timeframe: The reporting period type. Possible values: quarterly, annual, trailing_twelve_months.
        :param limit: Limit the number of results returned per-page, default is 100 and max is 50000.
        :param sort: Sort field used for ordering.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :param options: RequestOptionBuilder for additional headers or params.
        :return: Iterator of income statement records
        """
        url = "/stocks/financials/v1/income-statements"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_income_statements, locals()),
            raw=raw,
            deserializer=IncomeStatement.from_dict,
            options=options,
        )

    def list_financial_ratios(
        self,
        ticker: Optional[str] = None,
        cik: Optional[str] = None,
        price: Optional[float] = None,
        average_volume: Optional[float] = None,
        market_cap: Optional[float] = None,
        earnings_per_share: Optional[float] = None,
        price_to_earnings: Optional[float] = None,
        price_to_book: Optional[float] = None,
        price_to_sales: Optional[float] = None,
        price_to_cash_flow: Optional[float] = None,
        price_to_free_cash_flow: Optional[float] = None,
        dividend_yield: Optional[float] = None,
        return_on_assets: Optional[float] = None,
        return_on_equity: Optional[float] = None,
        debt_to_equity: Optional[float] = None,
        current: Optional[float] = None,
        quick: Optional[float] = None,
        cash: Optional[float] = None,
        ev_to_sales: Optional[float] = None,
        ev_to_ebitda: Optional[float] = None,
        enterprise_value: Optional[float] = None,
        free_cash_flow: Optional[float] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FinancialRatios], HTTPResponse]:
        """
        Retrieve comprehensive financial ratios data for public companies.

        :param ticker: Stock ticker symbol for the company.
        :param cik: Central Index Key (CIK) number assigned by the SEC.
        :param price: Stock price used in ratio calculations.
        :param average_volume: Average trading volume over a recent period.
        :param market_cap: Market capitalization.
        :param earnings_per_share: Earnings per share.
        :param price_to_earnings: Price-to-earnings ratio.
        :param price_to_book: Price-to-book ratio.
        :param price_to_sales: Price-to-sales ratio.
        :param price_to_cash_flow: Price-to-cash-flow ratio.
        :param price_to_free_cash_flow: Price-to-free-cash-flow ratio.
        :param dividend_yield: Dividend yield.
        :param return_on_assets: Return on assets ratio.
        :param return_on_equity: Return on equity ratio.
        :param debt_to_equity: Debt-to-equity ratio.
        :param current: Current ratio.
        :param quick: Quick ratio (acid-test ratio).
        :param cash: Cash ratio.
        :param ev_to_sales: Enterprise value to sales ratio.
        :param ev_to_ebitda: Enterprise value to EBITDA ratio.
        :param enterprise_value: Enterprise value.
        :param free_cash_flow: Free cash flow.
        :param limit: Limit the number of results returned per-page, default is 100 and max is 50000.
        :param sort: Sort field used for ordering.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :param options: RequestOptionBuilder for additional headers or params.
        :return: Iterator of financial ratios records
        """
        url = "/stocks/financials/v1/ratios"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_financial_ratios, locals()),
            raw=raw,
            deserializer=FinancialRatios.from_dict,
            options=options,
        )

    def list_short_interest(
        self,
        ticker: Optional[str] = None,
        days_to_cover: Optional[float] = None,
        settlement_date: Optional[Union[str, date]] = None,
        avg_daily_volume: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[ShortInterest], HTTPResponse]:
        """
        Retrieve bi-monthly aggregated short interest data for stocks.

        :param ticker: The primary ticker symbol for the stock.
        :param days_to_cover: Calculated as short_interest divided by avg_daily_volume.
        :param settlement_date: The date on which the short interest data is considered settled (YYYY-MM-DD).
        :param avg_daily_volume: The average daily trading volume for the stock.
        :param limit: Limit the number of results returned per-page, default is 10 and max is 50000.
        :param sort: Sort field used for ordering.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :param options: RequestOptionBuilder for additional headers or params.
        :return: Iterator of short interest records
        """
        url = "/stocks/v1/short-interest"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_short_interest, locals()),
            raw=raw,
            deserializer=ShortInterest.from_dict,
            options=options,
        )

    def list_short_volume(
        self,
        ticker: Optional[str] = None,
        date: Optional[Union[str, date]] = None,
        short_volume_ratio: Optional[float] = None,
        total_volume: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[ShortVolume], HTTPResponse]:
        """
        Retrieve daily aggregated short sale volume data for stocks.

        :param ticker: The primary ticker symbol for the stock.
        :param date: The date of trade activity reported (YYYY-MM-DD).
        :param short_volume_ratio: The percentage of total volume that was sold short.
        :param total_volume: Total reported volume across all venues for the ticker.
        :param limit: Limit the number of results returned per-page, default is 10 and max is 50000.
        :param sort: Sort field used for ordering.
        :param params: Any additional query params
        :param raw: Return raw object instead of results object
        :param options: RequestOptionBuilder for additional headers or params.
        :return: Iterator of short volume records
        """
        url = "/stocks/v1/short-volume"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_short_volume, locals()),
            raw=raw,
            deserializer=ShortVolume.from_dict,
            options=options,
        )
