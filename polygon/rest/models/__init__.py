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
from .definitions import ReferenceTickersApiResponse
from .definitions import ReferenceTickerTypesApiResponse
from .definitions import ReferenceTickerDetailsApiResponse
from .definitions import ReferenceTickerNewsApiResponse
from .definitions import ReferenceMarketsApiResponse
from .definitions import ReferenceLocalesApiResponse
from .definitions import ReferenceStockSplitsApiResponse
from .definitions import ReferenceStockDividendsApiResponse
from .definitions import ReferenceStockFinancialsApiResponse
from .definitions import ReferenceMarketStatusApiResponse
from .definitions import ReferenceMarketHolidaysApiResponse
from .definitions import StocksEquitiesExchangesApiResponse
from .definitions import StocksEquitiesHistoricTradesApiResponse
from .definitions import HistoricTradesV2ApiResponse
from .definitions import StocksEquitiesHistoricQuotesApiResponse
from .definitions import HistoricNBboQuotesV2ApiResponse
from .definitions import StocksEquitiesLastTradeForASymbolApiResponse
from .definitions import StocksEquitiesLastQuoteForASymbolApiResponse
from .definitions import StocksEquitiesDailyOpenCloseApiResponse
from .definitions import StocksEquitiesConditionMappingsApiResponse
from .definitions import StocksEquitiesSnapshotAllTickersApiResponse
from .definitions import StocksEquitiesSnapshotSingleTickerApiResponse
from .definitions import StocksEquitiesSnapshotGainersLosersApiResponse
from .definitions import StocksEquitiesPreviousCloseApiResponse
from .definitions import StocksEquitiesAggregatesApiResponse
from .definitions import StocksEquitiesGroupedDailyApiResponse
from .definitions import ForexCurrenciesHistoricForexTicksApiResponse
from .definitions import ForexCurrenciesRealTimeCurrencyConversionApiResponse
from .definitions import ForexCurrenciesLastQuoteForACurrencyPairApiResponse
from .definitions import ForexCurrenciesSnapshotAllTickersApiResponse
from .definitions import ForexCurrenciesSnapshotGainersLosersApiResponse
from .definitions import CryptoCryptoExchangesApiResponse
from .definitions import CryptoLastTradeForACryptoPairApiResponse
from .definitions import CryptoDailyOpenCloseApiResponse
from .definitions import CryptoHistoricCryptoTradesApiResponse
from .definitions import CryptoSnapshotAllTickersApiResponse
from .definitions import CryptoSnapshotSingleTickerApiResponse
from .definitions import CryptoSnapshotSingleTickerFullBookApiResponse
from .definitions import CryptoSnapshotGainersLosersApiResponse
from .definitions import StockSymbol
from .definitions import ConditionTypeMap
from .definitions import SymbolTypeMap
from .definitions import TickerSymbol


import typing

from .definitions import Definition


AnyDefinition = typing.TypeVar("AnyDefinition", bound=Definition)

# noinspection SpellCheckingInspection
name_to_class: typing.Dict[str, typing.Callable[[], typing.Type[AnyDefinition]]] = {
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
    "ReferenceTickersApiResponse": ReferenceTickersApiResponse,
    "ReferenceTickerTypesApiResponse": ReferenceTickerTypesApiResponse,
    "ReferenceTickerDetailsApiResponse": ReferenceTickerDetailsApiResponse,
    "ReferenceTickerNewsApiResponse": ReferenceTickerNewsApiResponse,
    "ReferenceMarketsApiResponse": ReferenceMarketsApiResponse,
    "ReferenceLocalesApiResponse": ReferenceLocalesApiResponse,
    "ReferenceStockSplitsApiResponse": ReferenceStockSplitsApiResponse,
    "ReferenceStockDividendsApiResponse": ReferenceStockDividendsApiResponse,
    "ReferenceStockFinancialsApiResponse": ReferenceStockFinancialsApiResponse,
    "ReferenceMarketStatusApiResponse": ReferenceMarketStatusApiResponse,
    "ReferenceMarketHolidaysApiResponse": ReferenceMarketHolidaysApiResponse,
    "StocksEquitiesExchangesApiResponse": StocksEquitiesExchangesApiResponse,
    "StocksEquitiesHistoricTradesApiResponse": StocksEquitiesHistoricTradesApiResponse,
    "HistoricTradesV2ApiResponse": HistoricTradesV2ApiResponse,
    "StocksEquitiesHistoricQuotesApiResponse": StocksEquitiesHistoricQuotesApiResponse,
    "HistoricNBboQuotesV2ApiResponse": HistoricNBboQuotesV2ApiResponse,
    "StocksEquitiesLastTradeForASymbolApiResponse": StocksEquitiesLastTradeForASymbolApiResponse,
    "StocksEquitiesLastQuoteForASymbolApiResponse": StocksEquitiesLastQuoteForASymbolApiResponse,
    "StocksEquitiesDailyOpenCloseApiResponse": StocksEquitiesDailyOpenCloseApiResponse,
    "StocksEquitiesConditionMappingsApiResponse": StocksEquitiesConditionMappingsApiResponse,
    "StocksEquitiesSnapshotAllTickersApiResponse": StocksEquitiesSnapshotAllTickersApiResponse,
    "StocksEquitiesSnapshotSingleTickerApiResponse": StocksEquitiesSnapshotSingleTickerApiResponse,
    "StocksEquitiesSnapshotGainersLosersApiResponse": StocksEquitiesSnapshotGainersLosersApiResponse,
    "StocksEquitiesPreviousCloseApiResponse": StocksEquitiesPreviousCloseApiResponse,
    "StocksEquitiesAggregatesApiResponse": StocksEquitiesAggregatesApiResponse,
    "StocksEquitiesGroupedDailyApiResponse": StocksEquitiesGroupedDailyApiResponse,
    "ForexCurrenciesHistoricForexTicksApiResponse": ForexCurrenciesHistoricForexTicksApiResponse,
    "ForexCurrenciesRealTimeCurrencyConversionApiResponse": ForexCurrenciesRealTimeCurrencyConversionApiResponse,
    "ForexCurrenciesLastQuoteForACurrencyPairApiResponse": ForexCurrenciesLastQuoteForACurrencyPairApiResponse,
    "ForexCurrenciesSnapshotAllTickersApiResponse": ForexCurrenciesSnapshotAllTickersApiResponse,
    "ForexCurrenciesSnapshotGainersLosersApiResponse": ForexCurrenciesSnapshotGainersLosersApiResponse,
    "CryptoCryptoExchangesApiResponse": CryptoCryptoExchangesApiResponse,
    "CryptoLastTradeForACryptoPairApiResponse": CryptoLastTradeForACryptoPairApiResponse,
    "CryptoDailyOpenCloseApiResponse": CryptoDailyOpenCloseApiResponse,
    "CryptoHistoricCryptoTradesApiResponse": CryptoHistoricCryptoTradesApiResponse,
    "CryptoSnapshotAllTickersApiResponse": CryptoSnapshotAllTickersApiResponse,
    "CryptoSnapshotSingleTickerApiResponse": CryptoSnapshotSingleTickerApiResponse,
    "CryptoSnapshotSingleTickerFullBookApiResponse": CryptoSnapshotSingleTickerFullBookApiResponse,
    "CryptoSnapshotGainersLosersApiResponse": CryptoSnapshotGainersLosersApiResponse,

}

# noinspection SpellCheckingInspection
name_to_type = {
    "StockSymbol": StockSymbol,
    "ConditionTypeMap": ConditionTypeMap,
    "SymbolTypeMap": SymbolTypeMap,
    "TickerSymbol": TickerSymbol,

}