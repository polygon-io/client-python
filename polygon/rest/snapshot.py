from .base import BaseClient
from typing import Optional, Any, Dict, List, Union
from .models import (
    Snapshot,
    Direction,
    OptionContractSnapshot,
    SnapshotMarketType,
    SnapshotTickerFullBook,
)
from urllib3 import HTTPResponse


class SnapshotClient(BaseClient):
    def get_snapshot_all(
        self,
        market_type: Optional[Union[str, SnapshotMarketType]] = "stocks",
        tickers: Optional[Union[str, List[str]]] = None,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[List[Snapshot], HTTPResponse]:
        """
        Get the most up-to-date market data for all traded stock symbols.

        Note: Snapshot data is cleared at 12am EST and gets populated as data is received from the exchanges. This can happen as early as 4am EST.

        :param market_type: Which market to get a snapshot of.
        :param tickers: A comma separated list of tickers to get snapshots for.
        :return: List of Snapshots
        """
        url = f"/v2/snapshot/locale/us/markets/{market_type}/tickers"
        if type(tickers) is list:
            tickers = ",".join(tickers)
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_all, locals()),
            deserializer=Snapshot.from_dict,
            raw=raw,
            result_key="tickers",
        )

    def get_snapshot_direction(
        self,
        direction: Union[str, Direction],
        market_type: Optional[Union[str, SnapshotMarketType]] = "stocks",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[List[Snapshot], HTTPResponse]:
        """
        Get the most up-to-date market data for the current top 20 gainers or losers of the day in the stocks/equities markets.

        Top gainers are those tickers whose price has increased by the highest percentage since the previous day's close. Top losers are those tickers whose price has decreased by the highest percentage since the previous day's close.

        Note: Snapshot data is cleared at 12am EST and gets populated as data is received from the exchanges.

        :param market_type: Which market to get a snapshot of.
        :param direction: The direction ("gainers" or "losers")
        :return: List of Snapshots
        """
        url = f"/v2/snapshot/locale/us/markets/{market_type}/{direction}"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_direction, locals()),
            result_key="tickers",
            deserializer=Snapshot.from_dict,
            raw=raw,
        )

    def get_snapshot_ticker(
        self,
        ticker: str,
        market_type: Optional[Union[str, SnapshotMarketType]] = "stocks",
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[Snapshot, HTTPResponse]:
        """
        Get the most up-to-date market data for all traded stock symbols.

        Note: Snapshot data is cleared at 12am EST and gets populated as data is received from the exchanges. This can happen as early as 4am EST.

        :param market_type: Which market to get a snapshot of.
        :param ticker: The ticker symbol.
        :return: List of Snapshots
        """
        url = f"/v2/snapshot/locale/us/markets/{market_type}/tickers/{ticker}"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_ticker, locals()),
            result_key="ticker",
            deserializer=Snapshot.from_dict,
            raw=raw,
        )

    def get_snapshot_option(
        self,
        underlying_asset: str,
        option_contract: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[OptionContractSnapshot, HTTPResponse]:
        """
        Get the snapshot of an option contract for a stock equity.

        :param underlying_asset: The underlying ticker symbol of the option contract.
        :param option_contract: The option contract identifier.
        :return: List of Snapshots
        """
        url = f"/v3/snapshot/options/{underlying_asset}/{option_contract}"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_option, locals()),
            result_key="results",
            deserializer=OptionContractSnapshot.from_dict,
            raw=raw,
        )

    def get_snapshot_crypto_book(
        self,
        ticker: str,
        params: Optional[Dict[str, Any]] = None,
        raw: bool = False,
    ) -> Union[SnapshotTickerFullBook, HTTPResponse]:
        """
        Get the current level 2 book of a single ticker. This is the combined book from all of the exchanges.

        Note: Snapshot data is cleared at 12am EST and gets populated as data is received from the exchanges.

        :param ticker: The ticker symbol.
        :return: List of Snapshots
        """
        url = f"/v2/snapshot/locale/global/markets/crypto/tickers/{ticker}/book"
        return self._get(
            path=url,
            params=self._get_params(self.get_snapshot_crypto_book, locals()),
            result_key="data",
            deserializer=SnapshotTickerFullBook.from_dict,
            raw=raw,
        )
