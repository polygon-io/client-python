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
        cik_any_of: Optional[str] = None,
        tickers: Optional[str] = None,
        tickers_any_of: Optional[str] = None,
        tickers_all_of: Optional[str] = None,
        period_end: Optional[Union[str, date]] = None,
        period_end_gt: Optional[Union[str, date]] = None,
        period_end_gte: Optional[Union[str, date]] = None,
        period_end_lt: Optional[Union[str, date]] = None,
        period_end_lte: Optional[Union[str, date]] = None,
        fiscal_year: Optional[int] = None,
        fiscal_year_gt: Optional[int] = None,
        fiscal_year_gte: Optional[int] = None,
        fiscal_year_lt: Optional[int] = None,
        fiscal_year_lte: Optional[int] = None,
        fiscal_quarter: Optional[int] = None,
        fiscal_quarter_gt: Optional[int] = None,
        fiscal_quarter_gte: Optional[int] = None,
        fiscal_quarter_lt: Optional[int] = None,
        fiscal_quarter_lte: Optional[int] = None,
        timeframe: Optional[str] = None,
        timeframe_any_of: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[BalanceSheet], HTTPResponse]:
        """
        Retrieve comprehensive balance sheet data for public companies.

        :param cik: The company's Central Index Key (CIK).
        :param cik_any_of: Filter equal to any of the CIK values (comma-separated list).
        :param tickers: Filter for arrays that contain the ticker value.
        :param tickers_any_of: Filter for arrays that contain any of the ticker values (comma-separated list).
        :param tickers_all_of: Filter for arrays that contain all of the ticker values (comma-separated list).
        :param period_end: The last date of the reporting period (YYYY-MM-DD).
        :param period_end_gt: Filter for period_end greater than the provided date.
        :param period_end_gte: Filter for period_end greater than or equal to the provided date.
        :param period_end_lt: Filter for period_end less than the provided date.
        :param period_end_lte: Filter for period_end less than or equal to the provided date.
        :param fiscal_year: The fiscal year for the reporting period.
        :param fiscal_year_gt: Filter for fiscal_year greater than the provided value.
        :param fiscal_year_gte: Filter for fiscal_year greater than or equal to the provided value.
        :param fiscal_year_lt: Filter for fiscal_year less than the provided value.
        :param fiscal_year_lte: Filter for fiscal_year less than or equal to the provided value.
        :param fiscal_quarter: The fiscal quarter number (1, 2, 3, or 4).
        :param fiscal_quarter_gt: Filter for fiscal_quarter greater than the provided value.
        :param fiscal_quarter_gte: Filter for fiscal_quarter greater than or equal to the provided value.
        :param fiscal_quarter_lt: Filter for fiscal_quarter less than the provided value.
        :param fiscal_quarter_lte: Filter for fiscal_quarter less than or equal to the provided value.
        :param timeframe: The reporting period type. Possible values: quarterly, annual.
        :param timeframe_any_of: Filter equal to any of the timeframe values (comma-separated list).
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
        cik_any_of: Optional[str] = None,
        cik_gt: Optional[str] = None,
        cik_gte: Optional[str] = None,
        cik_lt: Optional[str] = None,
        cik_lte: Optional[str] = None,
        tickers: Optional[str] = None,
        tickers_all_of: Optional[str] = None,
        tickers_any_of: Optional[str] = None,
        period_end: Optional[Union[str, date]] = None,
        period_end_gt: Optional[Union[str, date]] = None,
        period_end_gte: Optional[Union[str, date]] = None,
        period_end_lt: Optional[Union[str, date]] = None,
        period_end_lte: Optional[Union[str, date]] = None,
        fiscal_year: Optional[int] = None,
        fiscal_year_gt: Optional[int] = None,
        fiscal_year_gte: Optional[int] = None,
        fiscal_year_lt: Optional[int] = None,
        fiscal_year_lte: Optional[int] = None,
        fiscal_quarter: Optional[int] = None,
        fiscal_quarter_gt: Optional[int] = None,
        fiscal_quarter_gte: Optional[int] = None,
        fiscal_quarter_lt: Optional[int] = None,
        fiscal_quarter_lte: Optional[int] = None,
        timeframe: Optional[str] = None,
        timeframe_any_of: Optional[str] = None,
        timeframe_gt: Optional[str] = None,
        timeframe_gte: Optional[str] = None,
        timeframe_lt: Optional[str] = None,
        timeframe_lte: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[CashFlowStatement], HTTPResponse]:
        """
        Retrieve comprehensive cash flow statement data for public companies.

        :param cik: The company's Central Index Key (CIK).
        :param cik_any_of: Filter equal to any of the CIK values (comma-separated list).
        :param cik_gt: Filter for CIK greater than the provided value.
        :param cik_gte: Filter for CIK greater than or equal to the provided value.
        :param cik_lt: Filter for CIK less than the provided value.
        :param cik_lte: Filter for CIK less than or equal to the provided value.
        :param tickers: Filter for arrays that contain the ticker value.
        :param tickers_all_of: Filter for tickers that contain all of the values (comma-separated list).
        :param tickers_any_of: Filter for tickers that contain any of the values (comma-separated list).
        :param period_end: The last date of the reporting period (YYYY-MM-DD).
        :param period_end_gt: Filter for period_end greater than the provided date.
        :param period_end_gte: Filter for period_end greater than or equal to the provided date.
        :param period_end_lt: Filter for period_end less than the provided date.
        :param period_end_lte: Filter for period_end less than or equal to the provided date.
        :param fiscal_year: The fiscal year for the reporting period.
        :param fiscal_year_gt: Filter for fiscal_year greater than the provided value.
        :param fiscal_year_gte: Filter for fiscal_year greater than or equal to the provided value.
        :param fiscal_year_lt: Filter for fiscal_year less than the provided value.
        :param fiscal_year_lte: Filter for fiscal_year less than or equal to the provided value.
        :param fiscal_quarter: The fiscal quarter number (1, 2, 3, or 4).
        :param fiscal_quarter_gt: Filter for fiscal_quarter greater than the provided value.
        :param fiscal_quarter_gte: Filter for fiscal_quarter greater than or equal to the provided value.
        :param fiscal_quarter_lt: Filter for fiscal_quarter less than the provided value.
        :param fiscal_quarter_lte: Filter for fiscal_quarter less than or equal to the provided value.
        :param timeframe: The reporting period type. Possible values: quarterly, annual.
        :param timeframe_any_of: Filter equal to any of the timeframe values (comma-separated list).
        :param timeframe_gt: Filter for timeframe greater than the provided value.
        :param timeframe_gte: Filter for timeframe greater than or equal to the provided value.
        :param timeframe_lt: Filter for timeframe less than the provided value.
        :param timeframe_lte: Filter for timeframe less than or equal to the provided value.
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
        cik_any_of: Optional[str] = None,
        cik_gt: Optional[str] = None,
        cik_gte: Optional[str] = None,
        cik_lt: Optional[str] = None,
        cik_lte: Optional[str] = None,
        tickers: Optional[str] = None,
        tickers_all_of: Optional[str] = None,
        tickers_any_of: Optional[str] = None,
        period_end: Optional[Union[str, date]] = None,
        period_end_gt: Optional[Union[str, date]] = None,
        period_end_gte: Optional[Union[str, date]] = None,
        period_end_lt: Optional[Union[str, date]] = None,
        period_end_lte: Optional[Union[str, date]] = None,
        fiscal_year: Optional[int] = None,
        fiscal_year_gt: Optional[int] = None,
        fiscal_year_gte: Optional[int] = None,
        fiscal_year_lt: Optional[int] = None,
        fiscal_year_lte: Optional[int] = None,
        fiscal_quarter: Optional[int] = None,
        fiscal_quarter_gt: Optional[int] = None,
        fiscal_quarter_gte: Optional[int] = None,
        fiscal_quarter_lt: Optional[int] = None,
        fiscal_quarter_lte: Optional[int] = None,
        timeframe: Optional[str] = None,
        timeframe_any_of: Optional[str] = None,
        timeframe_gt: Optional[str] = None,
        timeframe_gte: Optional[str] = None,
        timeframe_lt: Optional[str] = None,
        timeframe_lte: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[IncomeStatement], HTTPResponse]:
        """
        Retrieve comprehensive income statement data for public companies.

        :param cik: The company's Central Index Key (CIK).
        :param cik_any_of: Filter equal to any of the CIK values (comma-separated list).
        :param cik_gt: Filter for CIK greater than the provided value.
        :param cik_gte: Filter for CIK greater than or equal to the provided value.
        :param cik_lt: Filter for CIK less than the provided value.
        :param cik_lte: Filter for CIK less than or equal to the provided value.
        :param tickers: Filter for arrays that contain the ticker value.
        :param tickers_all_of: Filter for tickers that contain all of the values (comma-separated list).
        :param tickers_any_of: Filter for tickers that contain any of the values (comma-separated list).
        :param period_end: The last date of the reporting period (YYYY-MM-DD).
        :param period_end_gt: Filter for period_end greater than the provided date.
        :param period_end_gte: Filter for period_end greater than or equal to the provided date.
        :param period_end_lt: Filter for period_end less than the provided date.
        :param period_end_lte: Filter for period_end less than or equal to the provided date.
        :param fiscal_year: The fiscal year for the reporting period.
        :param fiscal_year_gt: Filter for fiscal_year greater than the provided value.
        :param fiscal_year_gte: Filter for fiscal_year greater than or equal to the provided value.
        :param fiscal_year_lt: Filter for fiscal_year less than the provided value.
        :param fiscal_year_lte: Filter for fiscal_year less than or equal to the provided value.
        :param fiscal_quarter: The fiscal quarter number (1, 2, 3, or 4).
        :param fiscal_quarter_gt: Filter for fiscal_quarter greater than the provided value.
        :param fiscal_quarter_gte: Filter for fiscal_quarter greater than or equal to the provided value.
        :param fiscal_quarter_lt: Filter for fiscal_quarter less than the provided value.
        :param fiscal_quarter_lte: Filter for fiscal_quarter less than or equal to the provided value.
        :param timeframe: The reporting period type. Possible values: quarterly, annual.
        :param timeframe_any_of: Filter equal to any of the timeframe values (comma-separated list).
        :param timeframe_gt: Filter for timeframe greater than the provided value.
        :param timeframe_gte: Filter for timeframe greater than or equal to the provided value.
        :param timeframe_lt: Filter for timeframe less than the provided value.
        :param timeframe_lte: Filter for timeframe less than or equal to the provided value.
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
        ticker_any_of: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        cik: Optional[str] = None,
        cik_any_of: Optional[str] = None,
        cik_gt: Optional[str] = None,
        cik_gte: Optional[str] = None,
        cik_lt: Optional[str] = None,
        cik_lte: Optional[str] = None,
        price: Optional[float] = None,
        price_gt: Optional[float] = None,
        price_gte: Optional[float] = None,
        price_lt: Optional[float] = None,
        price_lte: Optional[float] = None,
        average_volume: Optional[float] = None,
        average_volume_gt: Optional[float] = None,
        average_volume_gte: Optional[float] = None,
        average_volume_lt: Optional[float] = None,
        average_volume_lte: Optional[float] = None,
        market_cap: Optional[float] = None,
        market_cap_gt: Optional[float] = None,
        market_cap_gte: Optional[float] = None,
        market_cap_lt: Optional[float] = None,
        market_cap_lte: Optional[float] = None,
        earnings_per_share: Optional[float] = None,
        earnings_per_share_gt: Optional[float] = None,
        earnings_per_share_gte: Optional[float] = None,
        earnings_per_share_lt: Optional[float] = None,
        earnings_per_share_lte: Optional[float] = None,
        price_to_earnings: Optional[float] = None,
        price_to_earnings_gt: Optional[float] = None,
        price_to_earnings_gte: Optional[float] = None,
        price_to_earnings_lt: Optional[float] = None,
        price_to_earnings_lte: Optional[float] = None,
        price_to_book: Optional[float] = None,
        price_to_book_gt: Optional[float] = None,
        price_to_book_gte: Optional[float] = None,
        price_to_book_lt: Optional[float] = None,
        price_to_book_lte: Optional[float] = None,
        price_to_sales: Optional[float] = None,
        price_to_sales_gt: Optional[float] = None,
        price_to_sales_gte: Optional[float] = None,
        price_to_sales_lt: Optional[float] = None,
        price_to_sales_lte: Optional[float] = None,
        price_to_cash_flow: Optional[float] = None,
        price_to_cash_flow_gt: Optional[float] = None,
        price_to_cash_flow_gte: Optional[float] = None,
        price_to_cash_flow_lt: Optional[float] = None,
        price_to_cash_flow_lte: Optional[float] = None,
        price_to_free_cash_flow: Optional[float] = None,
        price_to_free_cash_flow_gt: Optional[float] = None,
        price_to_free_cash_flow_gte: Optional[float] = None,
        price_to_free_cash_flow_lt: Optional[float] = None,
        price_to_free_cash_flow_lte: Optional[float] = None,
        dividend_yield: Optional[float] = None,
        dividend_yield_gt: Optional[float] = None,
        dividend_yield_gte: Optional[float] = None,
        dividend_yield_lt: Optional[float] = None,
        dividend_yield_lte: Optional[float] = None,
        return_on_assets: Optional[float] = None,
        return_on_assets_gt: Optional[float] = None,
        return_on_assets_gte: Optional[float] = None,
        return_on_assets_lt: Optional[float] = None,
        return_on_assets_lte: Optional[float] = None,
        return_on_equity: Optional[float] = None,
        return_on_equity_gt: Optional[float] = None,
        return_on_equity_gte: Optional[float] = None,
        return_on_equity_lt: Optional[float] = None,
        return_on_equity_lte: Optional[float] = None,
        debt_to_equity: Optional[float] = None,
        debt_to_equity_gt: Optional[float] = None,
        debt_to_equity_gte: Optional[float] = None,
        debt_to_equity_lt: Optional[float] = None,
        debt_to_equity_lte: Optional[float] = None,
        current: Optional[float] = None,
        current_gt: Optional[float] = None,
        current_gte: Optional[float] = None,
        current_lt: Optional[float] = None,
        current_lte: Optional[float] = None,
        quick: Optional[float] = None,
        quick_gt: Optional[float] = None,
        quick_gte: Optional[float] = None,
        quick_lt: Optional[float] = None,
        quick_lte: Optional[float] = None,
        cash: Optional[float] = None,
        cash_gt: Optional[float] = None,
        cash_gte: Optional[float] = None,
        cash_lt: Optional[float] = None,
        cash_lte: Optional[float] = None,
        ev_to_sales: Optional[float] = None,
        ev_to_sales_gt: Optional[float] = None,
        ev_to_sales_gte: Optional[float] = None,
        ev_to_sales_lt: Optional[float] = None,
        ev_to_sales_lte: Optional[float] = None,
        ev_to_ebitda: Optional[float] = None,
        ev_to_ebitda_gt: Optional[float] = None,
        ev_to_ebitda_gte: Optional[float] = None,
        ev_to_ebitda_lt: Optional[float] = None,
        ev_to_ebitda_lte: Optional[float] = None,
        enterprise_value: Optional[float] = None,
        enterprise_value_gt: Optional[float] = None,
        enterprise_value_gte: Optional[float] = None,
        enterprise_value_lt: Optional[float] = None,
        enterprise_value_lte: Optional[float] = None,
        free_cash_flow: Optional[float] = None,
        free_cash_flow_gt: Optional[float] = None,
        free_cash_flow_gte: Optional[float] = None,
        free_cash_flow_lt: Optional[float] = None,
        free_cash_flow_lte: Optional[float] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FinancialRatios], HTTPResponse]:
        """
        Retrieve comprehensive financial ratios data for public companies.

        :param ticker: Stock ticker symbol for the company.
        :param ticker_any_of: Filter equal to any of the ticker values (comma-separated list).
        :param ticker_gt: Filter for ticker greater than the provided value.
        :param ticker_gte: Filter for ticker greater than or equal to the provided value.
        :param ticker_lt: Filter for ticker less than the provided value.
        :param ticker_lte: Filter for ticker less than or equal to the provided value.
        :param cik: Central Index Key (CIK) number assigned by the SEC.
        :param cik_any_of: Filter equal to any of the CIK values (comma-separated list).
        :param cik_gt: Filter for CIK greater than the provided value.
        :param cik_gte: Filter for CIK greater than or equal to the provided value.
        :param cik_lt: Filter for CIK less than the provided value.
        :param cik_lte: Filter for CIK less than or equal to the provided value.
        :param price: Stock price used in ratio calculations.
        :param price_gt: Filter for price greater than the provided value.
        :param price_gte: Filter for price greater than or equal to the provided value.
        :param price_lt: Filter for price less than the provided value.
        :param price_lte: Filter for price less than or equal to the provided value.
        :param average_volume: Average trading volume over a recent period.
        :param average_volume_gt: Filter for average_volume greater than the provided value.
        :param average_volume_gte: Filter for average_volume greater than or equal to the provided value.
        :param average_volume_lt: Filter for average_volume less than the provided value.
        :param average_volume_lte: Filter for average_volume less than or equal to the provided value.
        :param market_cap: Market capitalization.
        :param market_cap_gt: Filter for market_cap greater than the provided value.
        :param market_cap_gte: Filter for market_cap greater than or equal to the provided value.
        :param market_cap_lt: Filter for market_cap less than the provided value.
        :param market_cap_lte: Filter for market_cap less than or equal to the provided value.
        :param earnings_per_share: Earnings per share.
        :param earnings_per_share_gt: Filter for earnings_per_share greater than the provided value.
        :param earnings_per_share_gte: Filter for earnings_per_share greater than or equal to the provided value.
        :param earnings_per_share_lt: Filter for earnings_per_share less than the provided value.
        :param earnings_per_share_lte: Filter for earnings_per_share less than or equal to the provided value.
        :param price_to_earnings: Price-to-earnings ratio.
        :param price_to_earnings_gt: Filter for price_to_earnings greater than the provided value.
        :param price_to_earnings_gte: Filter for price_to_earnings greater than or equal to the provided value.
        :param price_to_earnings_lt: Filter for price_to_earnings less than the provided value.
        :param price_to_earnings_lte: Filter for price_to_earnings less than or equal to the provided value.
        :param price_to_book: Price-to-book ratio.
        :param price_to_book_gt: Filter for price_to_book greater than the provided value.
        :param price_to_book_gte: Filter for price_to_book greater than or equal to the provided value.
        :param price_to_book_lt: Filter for price_to_book less than the provided value.
        :param price_to_book_lte: Filter for price_to_book less than or equal to the provided value.
        :param price_to_sales: Price-to-sales ratio.
        :param price_to_sales_gt: Filter for price_to_sales greater than the provided value.
        :param price_to_sales_gte: Filter for price_to_sales greater than or equal to the provided value.
        :param price_to_sales_lt: Filter for price_to_sales less than the provided value.
        :param price_to_sales_lte: Filter for price_to_sales less than or equal to the provided value.
        :param price_to_cash_flow: Price-to-cash-flow ratio.
        :param price_to_cash_flow_gt: Filter for price_to_cash_flow greater than the provided value.
        :param price_to_cash_flow_gte: Filter for price_to_cash_flow greater than or equal to the provided value.
        :param price_to_cash_flow_lt: Filter for price_to_cash_flow less than the provided value.
        :param price_to_cash_flow_lte: Filter for price_to_cash_flow less than or equal to the provided value.
        :param price_to_free_cash_flow: Price-to-free-cash-flow ratio.
        :param price_to_free_cash_flow_gt: Filter for price_to_free_cash_flow greater than the provided value.
        :param price_to_free_cash_flow_gte: Filter for price_to_free_cash_flow greater than or equal to the provided value.
        :param price_to_free_cash_flow_lt: Filter for price_to_free_cash_flow less than the provided value.
        :param price_to_free_cash_flow_lte: Filter for price_to_free_cash_flow less than or equal to the provided value.
        :param dividend_yield: Dividend yield.
        :param dividend_yield_gt: Filter for dividend_yield greater than the provided value.
        :param dividend_yield_gte: Filter for dividend_yield greater than or equal to the provided value.
        :param dividend_yield_lt: Filter for dividend_yield less than the provided value.
        :param dividend_yield_lte: Filter for dividend_yield less than or equal to the provided value.
        :param return_on_assets: Return on assets ratio.
        :param return_on_assets_gt: Filter for return_on_assets greater than the provided value.
        :param return_on_assets_gte: Filter for return_on_assets greater than or equal to the provided value.
        :param return_on_assets_lt: Filter for return_on_assets less than the provided value.
        :param return_on_assets_lte: Filter for return_on_assets less than or equal to the provided value.
        :param return_on_equity: Return on equity ratio.
        :param return_on_equity_gt: Filter for return_on_equity greater than the provided value.
        :param return_on_equity_gte: Filter for return_on_equity greater than or equal to the provided value.
        :param return_on_equity_lt: Filter for return_on_equity less than the provided value.
        :param return_on_equity_lte: Filter for return_on_equity less than or equal to the provided value.
        :param debt_to_equity: Debt-to-equity ratio.
        :param debt_to_equity_gt: Filter for debt_to_equity greater than the provided value.
        :param debt_to_equity_gte: Filter for debt_to_equity greater than or equal to the provided value.
        :param debt_to_equity_lt: Filter for debt_to_equity less than the provided value.
        :param debt_to_equity_lte: Filter for debt_to_equity less than or equal to the provided value.
        :param current: Current ratio.
        :param current_gt: Filter for current ratio greater than the provided value.
        :param current_gte: Filter for current ratio greater than or equal to the provided value.
        :param current_lt: Filter for current ratio less than the provided value.
        :param current_lte: Filter for current ratio less than or equal to the provided value.
        :param quick: Quick ratio (acid-test ratio).
        :param quick_gt: Filter for quick ratio greater than the provided value.
        :param quick_gte: Filter for quick ratio greater than or equal to the provided value.
        :param quick_lt: Filter for quick ratio less than the provided value.
        :param quick_lte: Filter for quick ratio less than or equal to the provided value.
        :param cash: Cash ratio.
        :param cash_gt: Filter for cash ratio greater than the provided value.
        :param cash_gte: Filter for cash ratio greater than or equal to the provided value.
        :param cash_lt: Filter for cash ratio less than the provided value.
        :param cash_lte: Filter for cash ratio less than or equal to the provided value.
        :param ev_to_sales: Enterprise value to sales ratio.
        :param ev_to_sales_gt: Filter for ev_to_sales greater than the provided value.
        :param ev_to_sales_gte: Filter for ev_to_sales greater than or equal to the provided value.
        :param ev_to_sales_lt: Filter for ev_to_sales less than the provided value.
        :param ev_to_sales_lte: Filter for ev_to_sales less than or equal to the provided value.
        :param ev_to_ebitda: Enterprise value to EBITDA ratio.
        :param ev_to_ebitda_gt: Filter for ev_to_ebitda greater than the provided value.
        :param ev_to_ebitda_gte: Filter for ev_to_ebitda greater than or equal to the provided value.
        :param ev_to_ebitda_lt: Filter for ev_to_ebitda less than the provided value.
        :param ev_to_ebitda_lte: Filter for ev_to_ebitda less than or equal to the provided value.
        :param enterprise_value: Enterprise value.
        :param enterprise_value_gt: Filter for enterprise_value greater than the provided value.
        :param enterprise_value_gte: Filter for enterprise_value greater than or equal to the provided value.
        :param enterprise_value_lt: Filter for enterprise_value less than the provided value.
        :param enterprise_value_lte: Filter for enterprise_value less than or equal to the provided value.
        :param free_cash_flow: Free cash flow.
        :param free_cash_flow_gt: Filter for free_cash_flow greater than the provided value.
        :param free_cash_flow_gte: Filter for free_cash_flow greater than or equal to the provided value.
        :param free_cash_flow_lt: Filter for free_cash_flow less than the provided value.
        :param free_cash_flow_lte: Filter for free_cash_flow less than or equal to the provided value.
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
        ticker_any_of: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        days_to_cover: Optional[float] = None,
        days_to_cover_any_of: Optional[str] = None,
        days_to_cover_gt: Optional[float] = None,
        days_to_cover_gte: Optional[float] = None,
        days_to_cover_lt: Optional[float] = None,
        days_to_cover_lte: Optional[float] = None,
        settlement_date: Optional[Union[str, date]] = None,
        settlement_date_any_of: Optional[str] = None,
        settlement_date_gt: Optional[Union[str, date]] = None,
        settlement_date_gte: Optional[Union[str, date]] = None,
        settlement_date_lt: Optional[Union[str, date]] = None,
        settlement_date_lte: Optional[Union[str, date]] = None,
        avg_daily_volume: Optional[int] = None,
        avg_daily_volume_any_of: Optional[str] = None,
        avg_daily_volume_gt: Optional[int] = None,
        avg_daily_volume_gte: Optional[int] = None,
        avg_daily_volume_lt: Optional[int] = None,
        avg_daily_volume_lte: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[ShortInterest], HTTPResponse]:
        """
        Retrieve bi-monthly aggregated short interest data for stocks.

        :param ticker: The primary ticker symbol for the stock.
        :param ticker_any_of: Filter equal to any of the ticker values (comma-separated list).
        :param ticker_gt: Filter for ticker greater than the provided value.
        :param ticker_gte: Filter for ticker greater than or equal to the provided value.
        :param ticker_lt: Filter for ticker less than the provided value.
        :param ticker_lte: Filter for ticker less than or equal to the provided value.
        :param days_to_cover: Calculated as short_interest divided by avg_daily_volume.
        :param days_to_cover_any_of: Filter equal to any of the days_to_cover values (comma-separated list).
        :param days_to_cover_gt: Filter for days_to_cover greater than the provided value.
        :param days_to_cover_gte: Filter for days_to_cover greater than or equal to the provided value.
        :param days_to_cover_lt: Filter for days_to_cover less than the provided value.
        :param days_to_cover_lte: Filter for days_to_cover less than or equal to the provided value.
        :param settlement_date: The date on which the short interest data is considered settled (YYYY-MM-DD).
        :param settlement_date_any_of: Filter equal to any of the settlement_date values (comma-separated list).
        :param settlement_date_gt: Filter for settlement_date greater than the provided date.
        :param settlement_date_gte: Filter for settlement_date greater than or equal to the provided date.
        :param settlement_date_lt: Filter for settlement_date less than the provided date.
        :param settlement_date_lte: Filter for settlement_date less than or equal to the provided date.
        :param avg_daily_volume: The average daily trading volume for the stock.
        :param avg_daily_volume_any_of: Filter equal to any of the avg_daily_volume values (comma-separated list).
        :param avg_daily_volume_gt: Filter for avg_daily_volume greater than the provided value.
        :param avg_daily_volume_gte: Filter for avg_daily_volume greater than or equal to the provided value.
        :param avg_daily_volume_lt: Filter for avg_daily_volume less than the provided value.
        :param avg_daily_volume_lte: Filter for avg_daily_volume less than or equal to the provided value.
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
        ticker_any_of: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        date: Optional[Union[str, date]] = None,
        date_any_of: Optional[str] = None,
        date_gt: Optional[Union[str, date]] = None,
        date_gte: Optional[Union[str, date]] = None,
        date_lt: Optional[Union[str, date]] = None,
        date_lte: Optional[Union[str, date]] = None,
        short_volume_ratio: Optional[float] = None,
        short_volume_ratio_any_of: Optional[str] = None,
        short_volume_ratio_gt: Optional[float] = None,
        short_volume_ratio_gte: Optional[float] = None,
        short_volume_ratio_lt: Optional[float] = None,
        short_volume_ratio_lte: Optional[float] = None,
        total_volume: Optional[int] = None,
        total_volume_any_of: Optional[str] = None,
        total_volume_gt: Optional[int] = None,
        total_volume_gte: Optional[int] = None,
        total_volume_lt: Optional[int] = None,
        total_volume_lte: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[ShortVolume], HTTPResponse]:
        """
        Retrieve daily aggregated short sale volume data for stocks.

        :param ticker: The primary ticker symbol for the stock.
        :param ticker_any_of: Filter equal to any of the ticker values (comma-separated list).
        :param ticker_gt: Filter for ticker greater than the provided value.
        :param ticker_gte: Filter for ticker greater than or equal to the provided value.
        :param ticker_lt: Filter for ticker less than the provided value.
        :param ticker_lte: Filter for ticker less than or equal to the provided value.
        :param date: The date of trade activity reported (YYYY-MM-DD).
        :param date_any_of: Filter equal to any of the date values (comma-separated list).
        :param date_gt: Filter for date greater than the provided date.
        :param date_gte: Filter for date greater than or equal to the provided date.
        :param date_lt: Filter for date less than the provided date.
        :param date_lte: Filter for date less than or equal to the provided date.
        :param short_volume_ratio: The percentage of total volume that was sold short.
        :param short_volume_ratio_any_of: Filter equal to any of the short_volume_ratio values (comma-separated list).
        :param short_volume_ratio_gt: Filter for short_volume_ratio greater than the provided value.
        :param short_volume_ratio_gte: Filter for short_volume_ratio greater than or equal to the provided value.
        :param short_volume_ratio_lt: Filter for short_volume_ratio less than the provided value.
        :param short_volume_ratio_lte: Filter for short_volume_ratio less than or equal to the provided value.
        :param total_volume: Total reported volume across all venues for the ticker.
        :param total_volume_any_of: Filter equal to any of the total_volume values (comma-separated list).
        :param total_volume_gt: Filter for total_volume greater than the provided value.
        :param total_volume_gte: Filter for total_volume greater than or equal to the provided value.
        :param total_volume_lt: Filter for total_volume less than the provided value.
        :param total_volume_lte: Filter for total_volume less than or equal to the provided value.
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
