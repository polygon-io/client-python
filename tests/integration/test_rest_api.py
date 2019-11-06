import os

import pytest

from polygon.rest import RESTClient
from polygon.rest import models


class TestAPI:
    """ The tests checks is the response was correctly unmarshalled and that no error occurred """
    api_key = os.getenv("API_KEY")
    assert api_key
    api_client = RESTClient(api_key)

    def test_reference_tickers(self):
        resp = self.api_client.reference_tickers(sort="ticker", perpage="50", page="1")
        assert isinstance(resp, models.ReferenceTickersApiResponse)

    def test_reference_ticker_types(self):
        resp = self.api_client.reference_ticker_types()
        assert isinstance(resp, models.ReferenceTickerTypesApiResponse)

    def test_reference_ticker_details(self):
        resp = self.api_client.reference_ticker_details("AAPL")
        assert isinstance(resp, models.ReferenceTickerDetailsApiResponse)

    def test_reference_ticker_news(self):
        resp = self.api_client.reference_ticker_news("AAPL", perpage="50", page="1")
        assert isinstance(resp, models.ReferenceTickerNewsApiResponse)

    def test_reference_markets(self):
        resp = self.api_client.reference_markets()
        assert isinstance(resp, models.ReferenceMarketsApiResponse)

    def test_reference_locales(self):
        resp = self.api_client.reference_locales()
        assert isinstance(resp, models.ReferenceLocalesApiResponse)

    def test_reference_stock_splits(self):
        resp = self.api_client.reference_stock_splits("AAPL")
        assert isinstance(resp, models.ReferenceStockSplitsApiResponse)

    def test_reference_stock_dividends(self):
        resp = self.api_client.reference_stock_dividends("AAPL")
        assert isinstance(resp, models.ReferenceStockDividendsApiResponse)

    def test_reference_stock_financials(self):
        resp = self.api_client.reference_stock_financials("AAPL", limit="5")
        assert isinstance(resp, models.ReferenceStockFinancialsApiResponse)

    def test_reference_market_status(self):
        resp = self.api_client.reference_market_status()
        assert isinstance(resp, models.ReferenceMarketStatusApiResponse)

    def test_reference_market_holidays(self):
        resp = self.api_client.reference_market_holidays()
        assert isinstance(resp, models.ReferenceMarketHolidaysApiResponse)

    def test_stocks_equities_exchanges(self):
        resp = self.api_client.stocks_equities_exchanges()
        assert isinstance(resp, models.StocksEquitiesExchangesApiResponse)

    def test_stocks_equities_historic_trades(self):
        resp = self.api_client.stocks_equities_historic_trades("AAPL", "2018-2-2", limit="100")
        assert isinstance(resp, models.StocksEquitiesHistoricTradesApiResponse)

    def test_historic_trades_v2(self):
        resp = self.api_client.historic_trades_v2("AAPL", "2018-02-02", limit="100")
        assert isinstance(resp, models.HistoricTradesV2ApiResponse)

    def test_stocks_equities_historic_quotes(self):
        resp = self.api_client.stocks_equities_historic_quotes("AAPL", "2018-2-2", limit="100")
        assert isinstance(resp, models.StocksEquitiesHistoricQuotesApiResponse)

    def test_historic_n___bbo_quotes_v2(self):
        resp = self.api_client.historic_n___bbo_quotes_v2("AAPL", "2018-02-02", limit="100")
        assert isinstance(resp, models.HistoricNBboQuotesV2ApiResponse)

    def test_stocks_equities_last_trade_for_a_symbol(self):
        resp = self.api_client.stocks_equities_last_trade_for_a_symbol("AAPL")
        assert isinstance(resp, models.StocksEquitiesLastTradeForASymbolApiResponse)

    def test_stocks_equities_last_quote_for_a_symbol(self):
        resp = self.api_client.stocks_equities_last_quote_for_a_symbol("AAPL")
        assert isinstance(resp, models.StocksEquitiesLastQuoteForASymbolApiResponse)

    def test_stocks_equities_daily_open_close(self):
        resp = self.api_client.stocks_equities_daily_open_close("AAPL", "2018-3-2")
        assert isinstance(resp, models.StocksEquitiesDailyOpenCloseApiResponse)

    def test_stocks_equities_condition_mappings(self):
        resp = self.api_client.stocks_equities_condition_mappings("trades")
        assert isinstance(resp, models.StocksEquitiesConditionMappingsApiResponse)

    def test_stocks_equities_snapshot_all_tickers(self):
        resp = self.api_client.stocks_equities_snapshot_all_tickers()
        assert isinstance(resp, models.StocksEquitiesSnapshotAllTickersApiResponse)

    def test_stocks_equities_snapshot_single_ticker(self):
        resp = self.api_client.stocks_equities_snapshot_single_ticker("AAPL")
        assert isinstance(resp, models.StocksEquitiesSnapshotSingleTickerApiResponse)

    def test_stocks_equities_snapshot_gainers_losers(self):
        resp = self.api_client.stocks_equities_snapshot_gainers_losers("gainers")
        assert isinstance(resp, models.StocksEquitiesSnapshotGainersLosersApiResponse)

    def test_stocks_equities_previous_close(self):
        resp = self.api_client.stocks_equities_previous_close("AAPL")
        assert isinstance(resp, models.StocksEquitiesPreviousCloseApiResponse)

    def test_stocks_equities_aggregates(self):
        resp = self.api_client.stocks_equities_aggregates("AAPL", "1", "day", "2019-01-01", "2019-02-01")
        assert isinstance(resp, models.StocksEquitiesAggregatesApiResponse)

    def test_stocks_equities_grouped_daily(self):
        resp = self.api_client.stocks_equities_grouped_daily("US", "STOCKS", "2019-02-01")
        assert isinstance(resp, models.StocksEquitiesGroupedDailyApiResponse)

    def test_forex_currencies_historic_forex_ticks(self):
        resp = self.api_client.forex_currencies_historic_forex_ticks("AUD", "USD", "2018-2-2", limit="100")
        assert isinstance(resp, models.ForexCurrenciesHistoricForexTicksApiResponse)

    def test_forex_currencies_real_time_currency_conversion(self):
        resp = self.api_client.forex_currencies_real_time_currency_conversion("AUD", "USD", amount="100", precision="2")
        assert isinstance(resp, models.ForexCurrenciesRealTimeCurrencyConversionApiResponse)

    def test_forex_currencies_last_quote_for_a_currency_pair(self):
        resp = self.api_client.forex_currencies_last_quote_for_a_currency_pair("AUD", "USD")
        assert isinstance(resp, models.ForexCurrenciesLastQuoteForACurrencyPairApiResponse)

    def test_forex_currencies_snapshot_all_tickers(self):
        resp = self.api_client.forex_currencies_snapshot_all_tickers()
        assert isinstance(resp, models.ForexCurrenciesSnapshotAllTickersApiResponse)

    def test_forex_currencies_snapshot_gainers_losers(self):
        resp = self.api_client.forex_currencies_snapshot_gainers_losers("gainers")
        assert isinstance(resp, models.ForexCurrenciesSnapshotGainersLosersApiResponse)

    def test_crypto_crypto_exchanges(self):
        resp = self.api_client.crypto_crypto_exchanges()
        assert isinstance(resp, models.CryptoCryptoExchangesApiResponse)

    def test_crypto_last_trade_for_a_crypto_pair(self):
        resp = self.api_client.crypto_last_trade_for_a_crypto_pair("BTC", "USD")
        assert isinstance(resp, models.CryptoLastTradeForACryptoPairApiResponse)

    def test_crypto_daily_open_close(self):
        resp = self.api_client.crypto_daily_open_close("BTC", "USD", "2018-5-9")
        assert isinstance(resp, models.CryptoDailyOpenCloseApiResponse)

    def test_crypto_historic_crypto_trades(self):
        resp = self.api_client.crypto_historic_crypto_trades("BTC", "USD", "2018-5-9", limit="100")
        assert isinstance(resp, models.CryptoHistoricCryptoTradesApiResponse)

    def test_crypto_snapshot_all_tickers(self):
        resp = self.api_client.crypto_snapshot_all_tickers()
        assert isinstance(resp, models.CryptoSnapshotAllTickersApiResponse)

    @pytest.mark.skip(reason="server 404's")
    def test_crypto_snapshot_single_ticker(self):
        resp = self.api_client.crypto_snapshot_single_ticker("~BTCUSD")
        assert isinstance(resp, models.CryptoSnapshotSingleTickerApiResponse)

    @pytest.mark.skip(reason="server 409's")
    def test_crypto_snapshot_single_ticker_full_book(self):
        resp = self.api_client.crypto_snapshot_single_ticker_full_book("~BTCUSD")
        assert isinstance(resp, models.CryptoSnapshotSingleTickerFullBookApiResponse)

    def test_crypto_snapshot_gainers_losers(self):
        resp = self.api_client.crypto_snapshot_gainers_losers("gainers")
        assert isinstance(resp, models.CryptoSnapshotGainersLosersApiResponse)
