import os
import unittest

from polygon.rest import RESTClient


class TestAPI(unittest.TestCase):
    def setUp(self):
        api_key = os.getenv("API_KEY")
        assert api_key

        self.api_client = RESTClient(api_key)
    
    def test_tickers(self):
        resp = self.api_client.tickers()
        print(resp)
    
    def test_ticker_types(self):
        resp = self.api_client.ticker_types()
        print(resp)
    
    def test_ticker_details(self):
        resp = self.api_client.ticker_details("AAPL")
        print(resp)
    
    def test_ticker_news(self):
        resp = self.api_client.ticker_news("AAPL")
        print(resp)
    
    def test_markets(self):
        resp = self.api_client.markets()
        print(resp)
    
    def test_locales(self):
        resp = self.api_client.locales()
        print(resp)
    
    def test_stock_splits(self):
        resp = self.api_client.stock_splits("AAPL")
        print(resp)
    
    def test_stock_dividends(self):
        resp = self.api_client.stock_dividends("AAPL")
        print(resp)
    
    def test_stock_financials(self):
        resp = self.api_client.stock_financials("AAPL")
        print(resp)
    
    def test_market_status(self):
        resp = self.api_client.market_status()
        print(resp)
    
    def test_market_holidays(self):
        resp = self.api_client.market_holidays()
        print(resp)
    
    def test_exchanges(self):
        resp = self.api_client.exchanges()
        print(resp)
    
    def test_historic_trades(self):
        resp = self.api_client.historic_trades("AAPL", "2018-2-2")
        print(resp)
    
    def test_historic_trades_v2(self):
        resp = self.api_client.historic_trades_v2("AAPL", "2018-02-02")
        print(resp)
    
    def test_historic_quotes(self):
        resp = self.api_client.historic_quotes("AAPL", "2018-2-2")
        print(resp)
    
    def test_historic_n___bbo_quotes_v2(self):
        resp = self.api_client.historic_n___bbo_quotes_v2("AAPL", "2018-02-02")
        print(resp)
    
    def test_last_trade_for_a_symbol(self):
        resp = self.api_client.last_trade_for_a_symbol("AAPL")
        print(resp)
    
    def test_last_quote_for_a_symbol(self):
        resp = self.api_client.last_quote_for_a_symbol("AAPL")
        print(resp)
    
    def test_daily_open_close(self):
        resp = self.api_client.daily_open_close("AAPL", "2018-3-2")
        print(resp)
    
    def test_condition_mappings(self):
        resp = self.api_client.condition_mappings("trades")
        print(resp)
    
    def test_snapshot_all_tickers(self):
        resp = self.api_client.snapshot_all_tickers()
        print(resp)
    
    def test_snapshot_single_ticker(self):
        resp = self.api_client.snapshot_single_ticker("AAPL")
        print(resp)
    
    def test_snapshot_gainers_losers(self):
        resp = self.api_client.snapshot_gainers_losers("gainers")
        print(resp)
    
    def test_previous_close(self):
        resp = self.api_client.previous_close("AAPL")
        print(resp)
    
    def test_aggregates(self):
        resp = self.api_client.aggregates("AAPL", "1", "day", "2019-01-01", "2019-02-01")
        print(resp)
    
    def test_grouped_daily(self):
        resp = self.api_client.grouped_daily("US", "STOCKS", "2019-02-01")
        print(resp)
    
    def test_historic_forex_ticks(self):
        resp = self.api_client.historic_forex_ticks("AUD", "USD", "2018-2-2")
        print(resp)
    
    def test_real_time_currency_conversion(self):
        resp = self.api_client.real_time_currency_conversion("AUD", "USD")
        print(resp)
    
    def test_last_quote_for_a_currency_pair(self):
        resp = self.api_client.last_quote_for_a_currency_pair("AUD", "USD")
        print(resp)
    
    def test_snapshot_all_tickers(self):
        resp = self.api_client.snapshot_all_tickers()
        print(resp)
    
    def test_snapshot_gainers_losers(self):
        resp = self.api_client.snapshot_gainers_losers("gainers")
        print(resp)
    
    def test_crypto_exchanges(self):
        resp = self.api_client.crypto_exchanges()
        print(resp)
    
    def test_last_trade_for_a_crypto_pair(self):
        resp = self.api_client.last_trade_for_a_crypto_pair("BTC", "USD")
        print(resp)
    
    def test_daily_open_close(self):
        resp = self.api_client.daily_open_close("BTC", "USD", "2018-5-9")
        print(resp)
    
    def test_historic_crypto_trades(self):
        resp = self.api_client.historic_crypto_trades("BTC", "USD", "2018-5-9")
        print(resp)
    
    def test_snapshot_all_tickers(self):
        resp = self.api_client.snapshot_all_tickers()
        print(resp)
    
    def test_snapshot_single_ticker(self):
        resp = self.api_client.snapshot_single_ticker("~BTCUSD")
        print(resp)
    
    def test_snapshot_single_ticker_full_book(self):
        resp = self.api_client.snapshot_single_ticker_full_book("~BTCUSD")
        print(resp)
    
    def test_snapshot_gainers_losers(self):
        resp = self.api_client.snapshot_gainers_losers("gainers")
        print(resp)
    
