from .definitions import LastTrade
from .definitions import LastQuote
from .definitions import HistTrade
from .definitions import Quote
from .definitions import Aggregate
from .definitions import Company
from .definitions import Symbol
from .definitions import Dividend
from .definitions import News
from .definitions import Earning
from .definitions import Financial
from .definitions import Exchange
from .definitions import Error
from .definitions import NotFound
from .definitions import Conflict
from .definitions import Unauthorized
from .definitions import MarketStatus
from .definitions import MarketHoliday
from .definitions import AnalystRatings
from .definitions import RatingSection
from .definitions import CryptoTick
from .definitions import CryptoTickJson
from .definitions import CryptoExchange
from .definitions import CryptoSnapshotTicker
from .definitions import CryptoSnapshotBookItem
from .definitions import CryptoSnapshotTickerBook
from .definitions import CryptoSnapshotAgg
from .definitions import Forex
from .definitions import LastForexTrade
from .definitions import LastForexQuote
from .definitions import ForexAggregate
from .definitions import ForexSnapshotTicker
from .definitions import ForexSnapshotAgg
from .definitions import Ticker
from .definitions import Split
from .definitions import Financials
from .definitions import Trade
from .definitions import StocksSnapshotTicker
from .definitions import StocksSnapshotBookItem
from .definitions import StocksSnapshotTickerBook
from .definitions import StocksV2Trade
from .definitions import StocksV2NBBO
from .definitions import StocksSnapshotAgg
from .definitions import StocksSnapshotQuote
from .definitions import Aggv2
from .definitions import AggResponse
from .definitions import TickersApiResponse
from .definitions import TickerTypesApiResponse
from .definitions import TickerDetailsApiResponse
from .definitions import TickerNewsApiResponse
from .definitions import MarketsApiResponse
from .definitions import LocalesApiResponse
from .definitions import StockSplitsApiResponse
from .definitions import StockDividendsApiResponse
from .definitions import StockFinancialsApiResponse
from .definitions import MarketStatusApiResponse
from .definitions import MarketHolidaysApiResponse
from .definitions import ExchangesApiResponse
from .definitions import HistoricTradesApiResponse
from .definitions import HistoricTradesV2ApiResponse
from .definitions import HistoricQuotesApiResponse
from .definitions import HistoricNBboQuotesV2ApiResponse
from .definitions import LastTradeForASymbolApiResponse
from .definitions import LastQuoteForASymbolApiResponse
from .definitions import DailyOpenCloseApiResponse
from .definitions import ConditionMappingsApiResponse
from .definitions import SnapshotAllTickersApiResponse
from .definitions import SnapshotSingleTickerApiResponse
from .definitions import SnapshotGainersLosersApiResponse
from .definitions import PreviousCloseApiResponse
from .definitions import AggregatesApiResponse
from .definitions import GroupedDailyApiResponse
from .definitions import HistoricForexTicksApiResponse
from .definitions import RealTimeCurrencyConversionApiResponse
from .definitions import LastQuoteForACurrencyPairApiResponse
from .definitions import SnapshotAllTickersApiResponse
from .definitions import SnapshotGainersLosersApiResponse
from .definitions import CryptoExchangesApiResponse
from .definitions import LastTradeForACryptoPairApiResponse
from .definitions import DailyOpenCloseApiResponse
from .definitions import HistoricCryptoTradesApiResponse
from .definitions import SnapshotAllTickersApiResponse
from .definitions import SnapshotSingleTickerApiResponse
from .definitions import SnapshotSingleTickerFullBookApiResponse
from .definitions import SnapshotGainersLosersApiResponse
from .definitions import StockSymbol
from .definitions import ConditionTypeMap
from .definitions import SymbolTypeMap
from .definitions import TickerSymbol


import typing

from .definitions import BaseDefinition

# noinspection SpellCheckingInspection
name_to_class: typing.Dict[str, BaseDefinition] = {
    "LastTrade": LastTrade,
    "LastQuote": LastQuote,
    "HistTrade": HistTrade,
    "Quote": Quote,
    "Aggregate": Aggregate,
    "Company": Company,
    "Symbol": Symbol,
    "Dividend": Dividend,
    "News": News,
    "Earning": Earning,
    "Financial": Financial,
    "Exchange": Exchange,
    "Error": Error,
    "NotFound": NotFound,
    "Conflict": Conflict,
    "Unauthorized": Unauthorized,
    "MarketStatus": MarketStatus,
    "MarketHoliday": MarketHoliday,
    "AnalystRatings": AnalystRatings,
    "RatingSection": RatingSection,
    "CryptoTick": CryptoTick,
    "CryptoTickJson": CryptoTickJson,
    "CryptoExchange": CryptoExchange,
    "CryptoSnapshotTicker": CryptoSnapshotTicker,
    "CryptoSnapshotBookItem": CryptoSnapshotBookItem,
    "CryptoSnapshotTickerBook": CryptoSnapshotTickerBook,
    "CryptoSnapshotAgg": CryptoSnapshotAgg,
    "Forex": Forex,
    "LastForexTrade": LastForexTrade,
    "LastForexQuote": LastForexQuote,
    "ForexAggregate": ForexAggregate,
    "ForexSnapshotTicker": ForexSnapshotTicker,
    "ForexSnapshotAgg": ForexSnapshotAgg,
    "Ticker": Ticker,
    "Split": Split,
    "Financials": Financials,
    "Trade": Trade,
    "StocksSnapshotTicker": StocksSnapshotTicker,
    "StocksSnapshotBookItem": StocksSnapshotBookItem,
    "StocksSnapshotTickerBook": StocksSnapshotTickerBook,
    "StocksV2Trade": StocksV2Trade,
    "StocksV2NBBO": StocksV2NBBO,
    "StocksSnapshotAgg": StocksSnapshotAgg,
    "StocksSnapshotQuote": StocksSnapshotQuote,
    "Aggv2": Aggv2,
    "AggResponse": AggResponse,
    "TickersApiResponse": TickersApiResponse,
    "TickerTypesApiResponse": TickerTypesApiResponse,
    "TickerDetailsApiResponse": TickerDetailsApiResponse,
    "TickerNewsApiResponse": TickerNewsApiResponse,
    "MarketsApiResponse": MarketsApiResponse,
    "LocalesApiResponse": LocalesApiResponse,
    "StockSplitsApiResponse": StockSplitsApiResponse,
    "StockDividendsApiResponse": StockDividendsApiResponse,
    "StockFinancialsApiResponse": StockFinancialsApiResponse,
    "MarketStatusApiResponse": MarketStatusApiResponse,
    "MarketHolidaysApiResponse": MarketHolidaysApiResponse,
    "ExchangesApiResponse": ExchangesApiResponse,
    "HistoricTradesApiResponse": HistoricTradesApiResponse,
    "HistoricTradesV2ApiResponse": HistoricTradesV2ApiResponse,
    "HistoricQuotesApiResponse": HistoricQuotesApiResponse,
    "HistoricNBboQuotesV2ApiResponse": HistoricNBboQuotesV2ApiResponse,
    "LastTradeForASymbolApiResponse": LastTradeForASymbolApiResponse,
    "LastQuoteForASymbolApiResponse": LastQuoteForASymbolApiResponse,
    "DailyOpenCloseApiResponse": DailyOpenCloseApiResponse,
    "ConditionMappingsApiResponse": ConditionMappingsApiResponse,
    "SnapshotAllTickersApiResponse": SnapshotAllTickersApiResponse,
    "SnapshotSingleTickerApiResponse": SnapshotSingleTickerApiResponse,
    "SnapshotGainersLosersApiResponse": SnapshotGainersLosersApiResponse,
    "PreviousCloseApiResponse": PreviousCloseApiResponse,
    "AggregatesApiResponse": AggregatesApiResponse,
    "GroupedDailyApiResponse": GroupedDailyApiResponse,
    "HistoricForexTicksApiResponse": HistoricForexTicksApiResponse,
    "RealTimeCurrencyConversionApiResponse": RealTimeCurrencyConversionApiResponse,
    "LastQuoteForACurrencyPairApiResponse": LastQuoteForACurrencyPairApiResponse,
    "SnapshotAllTickersApiResponse": SnapshotAllTickersApiResponse,
    "SnapshotGainersLosersApiResponse": SnapshotGainersLosersApiResponse,
    "CryptoExchangesApiResponse": CryptoExchangesApiResponse,
    "LastTradeForACryptoPairApiResponse": LastTradeForACryptoPairApiResponse,
    "DailyOpenCloseApiResponse": DailyOpenCloseApiResponse,
    "HistoricCryptoTradesApiResponse": HistoricCryptoTradesApiResponse,
    "SnapshotAllTickersApiResponse": SnapshotAllTickersApiResponse,
    "SnapshotSingleTickerApiResponse": SnapshotSingleTickerApiResponse,
    "SnapshotSingleTickerFullBookApiResponse": SnapshotSingleTickerFullBookApiResponse,
    "SnapshotGainersLosersApiResponse": SnapshotGainersLosersApiResponse,
    
}

# noinspection SpellCheckingInspection
name_to_type = {
    "StockSymbol": StockSymbol,
    "ConditionTypeMap": ConditionTypeMap,
    "SymbolTypeMap": SymbolTypeMap,
    "TickerSymbol": TickerSymbol,
    
}