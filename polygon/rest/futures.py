from .base import BaseClient
from typing import Optional, Any, Dict, List, Union, Iterator
from .models.futures import (
    FuturesAggregate,
    FuturesContract,
    FuturesMarketStatus,
    FuturesProduct,
    FuturesSchedule,
    FuturesQuote,
    FuturesTrade,
)
from .models import Sort, Order
from urllib3 import HTTPResponse
from datetime import datetime, date
from .models.request import RequestOptionBuilder


class FuturesClient(BaseClient):
    def list_futures_aggs(
        self,
        ticker: str,
        resolution: str,
        window_start: Optional[Union[str, int, datetime, date]] = None,
        window_start_gte: Optional[Union[str, int, datetime, date]] = None,
        window_start_gt: Optional[Union[str, int, datetime, date]] = None,
        window_start_lte: Optional[Union[str, int, datetime, date]] = None,
        window_start_lt: Optional[Union[str, int, datetime, date]] = None,
        order: Optional[Union[str, Order]] = "desc",
        limit: Optional[int] = 1000,
        sort: Optional[Union[str, Sort]] = "timestamp",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesAggregate], HTTPResponse]:
        """
        List aggregates for a futures contract in a given time range with pagination.

        :param ticker: The futures contract identifier (e.g., "ESZ4").
        :param resolution: The resolution of the aggregates (e.g., "1Min", "1D").
        :param window_start: Query by window start timestamp (YYYY-MM-DD or nanosecond timestamp).
        :param window_start_gte: Window start greater than or equal to.
        :param window_start_gt: Window start greater than.
        :param window_start_lte: Window start less than or equal to.
        :param window_start_lt: Window start less than.
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 1000, max 50000).
        :param sort: Sort field (default "timestamp").
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesAggregate objects or HTTPResponse if raw=True.
        """
        url = f"/futures/vX/aggs/{ticker}"
        return self._paginate(
            path=url,
            params=self._get_params(
                self.list_futures_aggs, locals(), datetime_res="nanos"
            ),
            raw=raw,
            deserializer=FuturesAggregate.from_dict,
            options=options,
        )

    def list_futures_contracts(
        self,
        product_code: Optional[str] = None,
        first_trade_date: Optional[Union[str, date]] = None,
        last_trade_date: Optional[Union[str, date]] = None,
        as_of: Optional[Union[str, date]] = None,
        active: Optional[str] = "all",
        type: Optional[str] = "all",
        order: Optional[Union[str, Order]] = "asc",
        limit: Optional[int] = 100,
        sort: Optional[Union[str, Sort]] = "product_code",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesContract], HTTPResponse]:
        """
        List futures contracts based on various parameters with pagination.

        :param product_code: Filter by product code.
        :param first_trade_date: Filter by first trade date (YYYY-MM-DD).
        :param last_trade_date: Filter by last trade date (YYYY-MM-DD).
        :param as_of: Point-in-time date (YYYY-MM-DD).
        :param active: Filter by active status ("all", "true", "false").
        :param type: Filter by contract type ("all", "single", "combo").
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 100, max 1000).
        :param sort: Sort field (default "product_code").
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesContract objects or HTTPResponse if raw=True.
        """
        url = "/futures/vX/contracts"
        return self._paginate(
            path=url,
            params=self._get_params(self.list_futures_contracts, locals()),
            raw=raw,
            deserializer=FuturesContract.from_dict,
            options=options,
        )

    def get_futures_contract(
        self,
        ticker: str,
        as_of: Optional[Union[str, date]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[FuturesContract, HTTPResponse]:
        """
        Get details for a single futures contract.

        :param ticker: The ticker symbol of the contract (e.g., "ESZ4").
        :param as_of: Point-in-time date (YYYY-MM-DD).
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: FuturesContract object or HTTPResponse if raw=True.
        """
        url = f"/futures/vX/contracts/{ticker}"
        return self._get(
            path=url,
            params=self._get_params(self.get_futures_contract, locals()),
            result_key="results",
            deserializer=FuturesContract.from_dict,
            raw=raw,
            options=options,
        )

    def list_futures_market_statuses(
        self,
        product_code_any_of: Optional[List[str]] = None,
        order: Optional[Union[str, Order]] = "asc",
        limit: Optional[int] = 100,
        sort: Optional[Union[str, Sort]] = "product_code",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesMarketStatus], HTTPResponse]:
        """
        List current market statuses for futures products with pagination.

        :param product_code_any_of: Comma-separated list of product codes.
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 100, max 1000).
        :param sort: Sort field (default "product_code").
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesMarketStatus objects or HTTPResponse if raw=True.
        """
        url = "/futures/vX/market-status"
        return self._paginate(
            path=url,
            params=self._get_params(self.list_futures_market_statuses, locals()),
            raw=raw,
            deserializer=FuturesMarketStatus.from_dict,
            options=options,
        )

    def list_futures_products(
        self,
        name: Optional[str] = None,
        as_of: Optional[Union[str, date]] = None,
        exchange_code: Optional[str] = None,
        sector: Optional[str] = None,
        sub_sector: Optional[str] = None,
        asset_class: Optional[str] = None,
        asset_sub_class: Optional[str] = None,
        type: Optional[str] = "all",
        name_search: Optional[str] = None,
        order: Optional[Union[str, Order]] = "asc",
        limit: Optional[int] = 100,
        sort: Optional[Union[str, Sort]] = "name",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesProduct], HTTPResponse]:
        """
        List futures products based on various parameters with pagination.

        :param name: Filter by product name (exact match).
        :param as_of: Point-in-time date (YYYY-MM-DD).
        :param exchange_code: Filter by exchange code (MIC).
        :param sector: Filter by sector.
        :param sub_sector: Filter by sub-sector.
        :param asset_class: Filter by asset class.
        :param asset_sub_class: Filter by asset sub-class.
        :param type: Filter by product type ("all", "single", "combo").
        :param name_search: Search by name (partial match).
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 100, max 1000).
        :param sort: Sort field (default "name").
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesProduct objects or HTTPResponse if raw=True.
        """
        url = "/futures/vX/products"
        return self._paginate(
            path=url,
            params=self._get_params(self.list_futures_products, locals()),
            raw=raw,
            deserializer=FuturesProduct.from_dict,
            options=options,
        )

    def get_futures_product(
        self,
        product_code: str,
        type: Optional[str] = "single",
        as_of: Optional[Union[str, date]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[FuturesProduct, HTTPResponse]:
        """
        Get details for a single futures product.

        :param product_code: The unique identifier for the product.
        :param type: Product type ("single" or "combo").
        :param as_of: Point-in-time date (YYYY-MM-DD).
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: FuturesProduct object or HTTPResponse if raw=True.
        """
        url = f"/futures/vX/products/{product_code}"
        return self._get(
            path=url,
            params=self._get_params(self.get_futures_product, locals()),
            result_key="results",
            deserializer=FuturesProduct.from_dict,
            raw=raw,
            options=options,
        )

    def list_futures_product_schedules(
        self,
        product_code: str,
        session_end_date: Optional[Union[str, date]] = None,
        session_end_date_gte: Optional[Union[str, date]] = None,
        session_end_date_gt: Optional[Union[str, date]] = None,
        session_end_date_lte: Optional[Union[str, date]] = None,
        session_end_date_lt: Optional[Union[str, date]] = None,
        order: Optional[Union[str, Order]] = "desc",
        limit: Optional[int] = 100,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesSchedule], HTTPResponse]:
        """
        List trading schedules for a specific futures product with pagination.

        :param product_code: The product code for the futures product.
        :param session_end_date: Filter by session end date (YYYY-MM-DD).
        :param session_end_date_gte: Session end date greater than or equal to.
        :param session_end_date_gt: Session end date greater than.
        :param session_end_date_lte: Session end date less than or equal to.
        :param session_end_date_lt: Session end date less than.
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 100, max 1000).
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesSchedule objects or HTTPResponse if raw=True.
        """
        url = f"/futures/vX/products/{product_code}/schedules"
        return self._paginate(
            path=url,
            params=self._get_params(self.list_futures_product_schedules, locals()),
            raw=raw,
            deserializer=FuturesSchedule.from_dict,
            options=options,
        )

    def list_futures_quotes(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        session_start_date: Optional[Union[str, date]] = None,
        session_start_date_gte: Optional[Union[str, date]] = None,
        session_start_date_gt: Optional[Union[str, date]] = None,
        session_start_date_lte: Optional[Union[str, date]] = None,
        session_start_date_lt: Optional[Union[str, date]] = None,
        order: Optional[Union[str, Order]] = "desc",
        limit: Optional[int] = 1000,
        sort: Optional[Union[str, Sort]] = "timestamp",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesQuote], HTTPResponse]:
        """
        List quotes for a futures contract in a given time range with pagination.

        :param ticker: The futures contract identifier (e.g., "ESZ4").
        :param timestamp: Query by quote timestamp (YYYY-MM-DD or nanosecond timestamp).
        :param timestamp_gte: Timestamp greater than or equal to.
        :param timestamp_gt: Timestamp greater than.
        :param timestamp_lte: Timestamp less than or equal to.
        :param timestamp_lt: Timestamp less than.
        :param session_start_date: Query by session start date (YYYY-MM-DD).
        :param session_start_date_gte: Session start date greater than or equal to.
        :param session_start_date_gt: Session start date greater than.
        :param session_start_date_lte: Session start date less than or equal to.
        :param session_start_date_lt: Session start date less than.
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 1000, max 50000).
        :param sort: Sort field (default "timestamp").
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesQuote objects or HTTPResponse if raw=True.
        """
        url = f"/futures/vX/quotes/{ticker}"
        return self._paginate(
            path=url,
            params=self._get_params(
                self.list_futures_quotes, locals(), datetime_res="nanos"
            ),
            raw=raw,
            deserializer=FuturesQuote.from_dict,
            options=options,
        )

    def list_futures_schedules_by_session_start_date(
        self,
        session_start_date: Optional[Union[str, date]] = None,
        market_identifier_code: Optional[str] = None,
        order: Optional[Union[str, Order]] = "desc",
        limit: Optional[int] = 10,
        sort: Optional[Union[str, Sort]] = "session_start_date",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesSchedule], HTTPResponse]:
        """
        List trading schedules by session start date across all products with pagination.

        :param session_start_date: Filter by session start date (YYYY-MM-DD).
        :param market_identifier_code: Filter by MIC of the exchange.
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 10, max 1000).
        :param sort: Sort field (default "session_start_date").
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesSchedule objects or HTTPResponse if raw=True.
        """
        url = "/futures/vX/schedules"
        return self._paginate(
            path=url,
            params=self._get_params(
                self.list_futures_schedules_by_session_start_date, locals()
            ),
            raw=raw,
            deserializer=FuturesSchedule.from_dict,
            options=options,
        )

    def list_futures_trades(
        self,
        ticker: str,
        timestamp: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_gt: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lte: Optional[Union[str, int, datetime, date]] = None,
        timestamp_lt: Optional[Union[str, int, datetime, date]] = None,
        session_start_date: Optional[Union[str, date]] = None,
        session_start_date_gte: Optional[Union[str, date]] = None,
        session_start_date_gt: Optional[Union[str, date]] = None,
        session_start_date_lte: Optional[Union[str, date]] = None,
        session_start_date_lt: Optional[Union[str, date]] = None,
        order: Optional[Union[str, Order]] = "desc",
        limit: Optional[int] = 1000,
        sort: Optional[Union[str, Sort]] = "timestamp",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
        options: Optional[RequestOptionBuilder] = None,
    ) -> Union[Iterator[FuturesTrade], HTTPResponse]:
        """
        List trades for a futures contract in a given time range with pagination.

        :param ticker: The futures contract identifier (e.g., "ESZ4").
        :param timestamp: Query by trade timestamp (YYYY-MM-DD or nanosecond timestamp).
        :param timestamp_gte: Timestamp greater than or equal to.
        :param timestamp_gt: Timestamp greater than.
        :param timestamp_lte: Timestamp less than or equal to.
        :param timestamp_lt: Timestamp less than.
        :param session_start_date: Query by session start date (YYYY-MM-DD).
        :param session_start_date_gte: Session start date greater than or equal to.
        :param session_start_date_gt: Session start date greater than.
        :param session_start_date_lte: Session start date less than or equal to.
        :param session_start_date_lt: Session start date less than.
        :param order: Order results (asc or desc).
        :param limit: Limit the number of results per page (default 1000, max 50000).
        :param sort: Sort field (default "timestamp").
        :param params: Additional query params.
        :param raw: Return raw HTTPResponse if True.
        :return: Iterator of FuturesTrade objects or HTTPResponse if raw=True.
        """
        url = f"/futures/vX/trades/{ticker}"
        return self._paginate(
            path=url,
            params=self._get_params(
                self.list_futures_trades, locals(), datetime_res="nanos"
            ),
            raw=raw,
            deserializer=FuturesTrade.from_dict,
            options=options,
        )
