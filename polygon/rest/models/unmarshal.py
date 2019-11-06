from typing import Dict, Callable

from polygon.rest import models

# noinspection SpellCheckingInspection
classes: Dict[str, Callable] = {
    "tickers": models.TickersApiResponse,
    "ticker_types": models.TickerTypesApiResponse,
    "ticker_details": models.TickerDetailsApiResponse,
    "ticker_news": models.TickerNewsApiResponse,
    "markets": models.MarketsApiResponse,
    "locales": models.LocalesApiResponse,
    "stock_splits": models.StockSplitsApiResponse,
    "stock_dividends": models.StockDividendsApiResponse,
    "stock_financials": models.StockFinancialsApiResponse,
    "market_status": models.MarketStatusApiResponse,
    "market_holidays": models.MarketHolidaysApiResponse,
    "exchanges": models.ExchangesApiResponse,
    "historic_trades": models.HistoricTradesApiResponse,
    "historic_trades_v2": models.HistoricTradesV2ApiResponse,
    "historic_quotes": models.HistoricQuotesApiResponse,
    "historic_n___bbo_quotes_v2": models.HistoricNBboQuotesV2ApiResponse,
    "last_trade_for_a_symbol": models.LastTradeForASymbolApiResponse,
    "last_quote_for_a_symbol": models.LastQuoteForASymbolApiResponse,
    "daily_open_close": models.DailyOpenCloseApiResponse,
    "condition_mappings": models.ConditionMappingsApiResponse,
    "snapshot_all_tickers": models.SnapshotAllTickersApiResponse,
    "snapshot_single_ticker": models.SnapshotSingleTickerApiResponse,
    "snapshot_gainers_losers": models.SnapshotGainersLosersApiResponse,
    "previous_close": models.PreviousCloseApiResponse,
    "aggregates": models.AggregatesApiResponse,
    "grouped_daily": models.GroupedDailyApiResponse,
    "historic_forex_ticks": models.HistoricForexTicksApiResponse,
    "real_time_currency_conversion": models.RealTimeCurrencyConversionApiResponse,
    "last_quote_for_a_currency_pair": models.LastQuoteForACurrencyPairApiResponse,
    "snapshot_all_tickers": models.SnapshotAllTickersApiResponse,
    "snapshot_gainers_losers": models.SnapshotGainersLosersApiResponse,
    "crypto_exchanges": models.CryptoExchangesApiResponse,
    "last_trade_for_a_crypto_pair": models.LastTradeForACryptoPairApiResponse,
    "daily_open_close": models.DailyOpenCloseApiResponse,
    "historic_crypto_trades": models.HistoricCryptoTradesApiResponse,
    "snapshot_all_tickers": models.SnapshotAllTickersApiResponse,
    "snapshot_single_ticker": models.SnapshotSingleTickerApiResponse,
    "snapshot_single_ticker_full_book": models.SnapshotSingleTickerFullBookApiResponse,
    "snapshot_gainers_losers": models.SnapshotGainersLosersApiResponse,
    
}


def unmarshal_json(handler, resp_json):
    response_object = classes[handler](resp_json)
