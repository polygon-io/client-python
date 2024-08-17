from .base import BaseClient
from typing import Optional, Any, Dict, List, Union, Iterator
from .models import (
    MarketHoliday,
    MarketStatus,
    Ticker,
    TickerChangeResults,
    TickerDetails,
    TickerNews,
    RelatedCompany,
    TickerTypes,
    Sort,
    Order,
    AssetClass,
    Locale,
    Split,
    Dividend,
    DividendType,
    Frequency,
    Condition,
    DataType,
    SIP,
    Exchange,
    OptionsContract,
)
from urllib3 import HTTPResponse
from datetime import date

from .models.request import RequestOptionBuilder


class MarketsClient(BaseClient):
    def get_market_holidays(
        self, params: Optional[Dict[str, Any]] = None, raw: bool = False
    ) -> Union[List[MarketHoliday], HTTPResponse]:
        
        url = "/v1/marketstatus/upcoming"

        return self._get(
            path=url,
            params=params,
            deserializer=MarketHoliday.from_dict,
            raw=raw,
            result_key="",
        )

    def get_market_status(
        self, params: Optional[Dict[str, Any]] = None, raw: bool = False
    ) -> Union[MarketStatus, HTTPResponse]:
       
        url = "/v1/marketstatus/now"

        return self._get(
            path=url, params=params, deserializer=MarketStatus.from_dict, raw=raw
        )


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
        limit: Optional[int] = 10,
        sort: Optional[Union[str, Sort]] = "ticker",
        order: Optional[Union[str, Order]] = "asc",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[Ticker], HTTPResponse]:
        
        url = "/v3/reference/tickers"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_tickers, locals()),
            raw=raw,
            deserializer=Ticker.from_dict,
            options=options,
        )

    def get_ticker_details(
        self,
        ticker: Optional[str] = None,
        date: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[TickerDetails, HTTPResponse]:
       
        url = f"/v3/reference/tickers/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_ticker_details, locals()),
            deserializer=TickerDetails.from_dict,
            raw=raw,
            result_key="results",
            options=options,
        )

    def get_ticker_events(
        self,
        ticker: str,
        types: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[TickerChangeResults, HTTPResponse]:
       
        url = f"/vX/reference/tickers/{ticker}/events"

        return self._get(
            path=url,
            params=self._get_params(self.get_ticker_events, locals()),
            deserializer=TickerChangeResults.from_dict,
            result_key="results",
            raw=raw,
            options=options,
        )

    def list_ticker_news(
        self,
        ticker: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        published_utc: Optional[str] = None,
        published_utc_lt: Optional[str] = None,
        published_utc_lte: Optional[str] = None,
        published_utc_gt: Optional[str] = None,
        published_utc_gte: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[TickerNews], HTTPResponse]:
        
        url = "/v2/reference/news"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_ticker_news, locals()),
            raw=raw,
            deserializer=TickerNews.from_dict,
            options=options,
        )

    def get_ticker_types(
        self,
        asset_class: Optional[Union[str, AssetClass]] = None,
        locale: Optional[Union[str, Locale]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[List[TickerTypes], HTTPResponse]:
        
        url = "/v3/reference/tickers/types"

        return self._get(
            path=url,
            params=self._get_params(self.get_ticker_types, locals()),
            deserializer=TickerTypes.from_dict,
            raw=raw,
            result_key="results",
            options=options,
        )

    def get_related_companies(
        self,
        ticker: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[RelatedCompany, HTTPResponse]:
        """
        Get a list of tickers related to the queried ticker based on News and Returns data.

        :param ticker: The ticker symbol to search.
        :param params: Any additional query params.
        :param raw: Return raw object instead of results object.
        :return: Related Companies.
        """
        url = f"/v1/related-companies/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_related_companies, locals()),
            deserializer=RelatedCompany.from_dict,
            raw=raw,
            result_key="results",
            options=options,
        )


class SplitsClient(BaseClient):
    def list_splits(
        self,
        ticker: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        execution_date: Optional[Union[str, date]] = None,
        execution_date_lt: Optional[Union[str, date]] = None,
        execution_date_lte: Optional[Union[str, date]] = None,
        execution_date_gt: Optional[Union[str, date]] = None,
        execution_date_gte: Optional[Union[str, date]] = None,
        reverse_split: Optional[bool] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[Split], HTTPResponse]:
    
        url = "/v3/reference/splits"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_splits, locals()),
            raw=raw,
            deserializer=Split.from_dict,
            options=options,
        )


class DividendsClient(BaseClient):
    def list_dividends(
        self,
        ticker: Optional[str] = None,
        ticker_lt: Optional[str] = None,
        ticker_lte: Optional[str] = None,
        ticker_gt: Optional[str] = None,
        ticker_gte: Optional[str] = None,
        ex_dividend_date: Optional[Union[str, date]] = None,
        ex_dividend_date_lt: Optional[Union[str, date]] = None,
        ex_dividend_date_lte: Optional[Union[str, date]] = None,
        ex_dividend_date_gt: Optional[Union[str, date]] = None,
        ex_dividend_date_gte: Optional[Union[str, date]] = None,
        record_date: Optional[Union[str, date]] = None,
        record_date_lt: Optional[Union[str, date]] = None,
        record_date_lte: Optional[Union[str, date]] = None,
        record_date_gt: Optional[Union[str, date]] = None,
        record_date_gte: Optional[Union[str, date]] = None,
        declaration_date: Optional[Union[str, date]] = None,
        declaration_date_lt: Optional[Union[str, date]] = None,
        declaration_date_lte: Optional[Union[str, date]] = None,
        declaration_date_gt: Optional[Union[str, date]] = None,
        declaration_date_gte: Optional[Union[str, date]] = None,
        pay_date: Optional[Union[str, date]] = None,
        pay_date_lt: Optional[Union[str, date]] = None,
        pay_date_lte: Optional[Union[str, date]] = None,
        pay_date_gt: Optional[Union[str, date]] = None,
        pay_date_gte: Optional[Union[str, date]] = None,
        frequency: Optional[Union[int, Frequency]] = None,
        cash_amount: Optional[float] = None,
        cash_amount_lt: Optional[float] = None,
        cash_amount_lte: Optional[float] = None,
        cash_amount_gt: Optional[float] = None,
        cash_amount_gte: Optional[float] = None,
        dividend_type: Optional[Union[str, DividendType]] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[Dividend], HTTPResponse]:
        
        url = "/v3/reference/dividends"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_dividends, locals()),
            raw=raw,
            deserializer=Dividend.from_dict,
            options=options,
        )


class ConditionsClient(BaseClient):
    def list_conditions(
        self,
        asset_class: Optional[Union[str, AssetClass]] = None,
        data_type: Optional[Union[str, DataType]] = None,
        id: Optional[int] = None,
        sip: Optional[Union[str, SIP]] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[Condition], HTTPResponse]:
        
        url = "/v3/reference/conditions"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_conditions, locals()),
            raw=raw,
            deserializer=Condition.from_dict,
            options=options,
        )


class ExchangesClient(BaseClient):
    def get_exchanges(
        self,
        asset_class: Optional[Union[str, AssetClass]] = None,
        locale: Optional[Union[str, Locale]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[List[Exchange], HTTPResponse]:
        
        url = "/v3/reference/exchanges"

        return self._get(
            path=url,
            params=self._get_params(self.get_exchanges, locals()),
            deserializer=Exchange.from_dict,
            raw=raw,
            result_key="results",
            options=options,
        )


class ContractsClient(BaseClient):
    def get_options_contract(
        self,
        ticker: str,
        as_of: Optional[Union[str, date]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[OptionsContract, HTTPResponse]:
        
        url = f"/v3/reference/options/contracts/{ticker}"

        return self._get(
            path=url,
            params=self._get_params(self.get_options_contract, locals()),
            result_key="results",
            deserializer=OptionsContract.from_dict,
            raw=raw,
            options=options,
        )

    def list_options_contracts(
        self,
        underlying_ticker: Optional[str] = None,
        underlying_ticker_lt: Optional[str] = None,
        underlying_ticker_lte: Optional[str] = None,
        underlying_ticker_gt: Optional[str] = None,
        underlying_ticker_gte: Optional[str] = None,
        contract_type: Optional[str] = None,
        expiration_date: Optional[Union[str, date]] = None,
        expiration_date_lt: Optional[Union[str, date]] = None,
        expiration_date_lte: Optional[Union[str, date]] = None,
        expiration_date_gt: Optional[Union[str, date]] = None,
        expiration_date_gte: Optional[Union[str, date]] = None,
        as_of: Optional[Union[str, date]] = None,
        strike_price: Optional[float] = None,
        strike_price_lt: Optional[float] = None,
        strike_price_lte: Optional[float] = None,
        strike_price_gt: Optional[float] = None,
        strike_price_gte: Optional[float] = None,
        expired: Optional[bool] = None,
        limit: Optional[int] = None,
        sort: Optional[Union[str, Sort]] = None,
        order: Optional[Union[str, Order]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[OptionsContract], HTTPResponse]:
        
        url = "/v3/reference/options/contracts"

        return self._paginate(
            path=url,
            params=self._get_params(self.list_options_contracts, locals()),
            raw=raw,
            deserializer=OptionsContract.from_dict,
            options=options,
        )
