from typing import List, Dict

from polygon.rest import models

StockSymbol = str
ConditionTypeMap = Dict[str, str]
SymbolTypeMap = Dict[str, str]
TickerSymbol = str


class BaseDefinition:
    swagger_name_to_python: Dict[str, str]
    attribute_is_primitive: Dict[str, bool]

    def _unmarshal_json(self, input_json):
        for key, value in input_json:
            if key not in self.swagger_name_to_python:
                raise ValueError(f"response json has unexpected attribute {key}")

            python_name = self.swagger_name_to_python[key]
            if self.attribute_is_primitive[python_name]:
                if python_name not in models.name_to_class:
                    raise ValueError(
                        f"received an attribute that is not a primitive nor a definition class: {python_name}")

                value = models.name_to_class[python_name]
                value._unmarshal_json(input_json["key"])

            self.__setattr__(python_name, value)


# noinspection SpellCheckingInspection
class LastTrade(BaseDefinition):
    swagger_name_to_python = {
        "price": "price",
        "size": "size",
        "exchange": "exchange",
        "cond1": "cond1",
        "cond2": "cond2",
        "cond3": "cond3",
        "cond4": "cond4",
        "timestamp": "timestamp",
        
    }

    attribute_is_primitive = {
        "price": True,
        "size": True,
        "exchange": True,
        "cond1": True,
        "cond2": True,
        "cond3": True,
        "cond4": True,
        "timestamp": True,
        
    }

    def __init__(self, input_json):
        self.price: int
        self.size: int
        self.exchange: int
        self.cond1: int
        self.cond2: int
        self.cond3: int
        self.cond4: int
        self.timestamp: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LastQuote(BaseDefinition):
    swagger_name_to_python = {
        "askprice": "askprice",
        "asksize": "asksize",
        "askexchange": "askexchange",
        "bidprice": "bidprice",
        "bidsize": "bidsize",
        "bidexchange": "bidexchange",
        "timestamp": "timestamp",
        
    }

    attribute_is_primitive = {
        "askprice": True,
        "asksize": True,
        "askexchange": True,
        "bidprice": True,
        "bidsize": True,
        "bidexchange": True,
        "timestamp": True,
        
    }

    def __init__(self, input_json):
        self.askprice: int
        self.asksize: int
        self.askexchange: int
        self.bidprice: int
        self.bidsize: int
        self.bidexchange: int
        self.timestamp: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class HistTrade(BaseDefinition):
    swagger_name_to_python = {
        "condition1": "condition1",
        "condition2": "condition2",
        "condition3": "condition3",
        "condition4": "condition4",
        "exchange": "exchange",
        "price": "price",
        "size": "size",
        "timestamp": "timestamp",
        
    }

    attribute_is_primitive = {
        "condition1": True,
        "condition2": True,
        "condition3": True,
        "condition4": True,
        "exchange": True,
        "price": True,
        "size": True,
        "timestamp": True,
        
    }

    def __init__(self, input_json):
        self.condition1: int
        self.condition2: int
        self.condition3: int
        self.condition4: int
        self.exchange: str
        self.price: int
        self.size: int
        self.timestamp: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Quote(BaseDefinition):
    swagger_name_to_python = {
        "c": "condition_of_this_quote",
        "bE": "bid_exchange",
        "aE": "ask_exchange",
        "aP": "ask_price",
        "bP": "bid_price",
        "bS": "bid_size",
        "aS": "ask_size",
        "t": "timestamp_of_this_trade",
        
    }

    attribute_is_primitive = {
        "condition_of_this_quote": True,
        "bid_exchange": True,
        "ask_exchange": True,
        "ask_price": True,
        "bid_price": True,
        "bid_size": True,
        "ask_size": True,
        "timestamp_of_this_trade": True,
        
    }

    def __init__(self, input_json):
        self.condition_of_this_quote: int
        self.bid_exchange: str
        self.ask_exchange: str
        self.ask_price: int
        self.bid_price: int
        self.bid_size: int
        self.ask_size: int
        self.timestamp_of_this_trade: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Aggregate(BaseDefinition):
    swagger_name_to_python = {
        "o": "open_price",
        "c": "close_price",
        "l": "low_price",
        "h": "high_price",
        "v": "total_volume_of_all_trades",
        "k": "transactions",
        "t": "timestamp_of_this_aggregation",
        
    }

    attribute_is_primitive = {
        "open_price": True,
        "close_price": True,
        "low_price": True,
        "high_price": True,
        "total_volume_of_all_trades": True,
        "transactions": True,
        "timestamp_of_this_aggregation": True,
        
    }

    def __init__(self, input_json):
        self.open_price: int
        self.close_price: int
        self.low_price: int
        self.high_price: int
        self.total_volume_of_all_trades: int
        self.transactions: int
        self.timestamp_of_this_aggregation: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Company(BaseDefinition):
    swagger_name_to_python = {
        "logo": "logo",
        "exchange": "exchange",
        "name": "name",
        "symbol": "symbol",
        "listdate": "listdate",
        "cik": "cik",
        "bloomberg": "bloomberg",
        "figi": "figi",
        "lei": "lei",
        "sic": "sic",
        "country": "country",
        "industry": "industry",
        "sector": "sector",
        "marketcap": "marketcap",
        "employees": "employees",
        "phone": "phone",
        "ceo": "ceo",
        "url": "url",
        "description": "description",
        "similar": "similar",
        "tags": "tags",
        "updated": "updated",
        
    }

    attribute_is_primitive = {
        "logo": True,
        "exchange": True,
        "name": True,
        "symbol": False,
        "listdate": True,
        "cik": True,
        "bloomberg": True,
        "figi": True,
        "lei": True,
        "sic": True,
        "country": True,
        "industry": True,
        "sector": True,
        "marketcap": True,
        "employees": True,
        "phone": True,
        "ceo": True,
        "url": True,
        "description": True,
        "similar": False,
        "tags": False,
        "updated": True,
        
    }

    def __init__(self, input_json):
        self.logo: str
        self.exchange: str
        self.name: str
        self.symbol: StockSymbol
        self.listdate: str
        self.cik: str
        self.bloomberg: str
        self.figi: str
        self.lei: str
        self.sic: float
        self.country: str
        self.industry: str
        self.sector: str
        self.marketcap: float
        self.employees: float
        self.phone: str
        self.ceo: str
        self.url: str
        self.description: str
        self.similar: List[StockSymbol]
        self.tags: List[str]
        self.updated: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Symbol(BaseDefinition):
    swagger_name_to_python = {
        "symbol": "symbol",
        "name": "name",
        "type": "type",
        "url": "url",
        "updated": "updated",
        "isOTC": "is___otc",
        
    }

    attribute_is_primitive = {
        "symbol": False,
        "name": True,
        "type": True,
        "url": True,
        "updated": True,
        "is___otc": True,
        
    }

    def __init__(self, input_json):
        self.symbol: StockSymbol
        self.name: str
        self.type: str
        self.url: str
        self.updated: str
        self.is___otc: bool
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Dividend(BaseDefinition):
    swagger_name_to_python = {
        "symbol": "symbol",
        "type": "type",
        "exDate": "ex_date",
        "paymentDate": "payment_date",
        "recordDate": "record_date",
        "declaredDate": "declared_date",
        "amount": "amount",
        "qualified": "qualified",
        "flag": "flag",
        
    }

    attribute_is_primitive = {
        "symbol": False,
        "type": True,
        "ex_date": True,
        "payment_date": True,
        "record_date": True,
        "declared_date": True,
        "amount": True,
        "qualified": True,
        "flag": True,
        
    }

    def __init__(self, input_json):
        self.symbol: StockSymbol
        self.type: str
        self.ex_date: str
        self.payment_date: str
        self.record_date: str
        self.declared_date: str
        self.amount: float
        self.qualified: str
        self.flag: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class News(BaseDefinition):
    swagger_name_to_python = {
        "symbols": "symbols",
        "title": "title",
        "url": "url",
        "source": "source",
        "summary": "summary",
        "image": "image",
        "timestamp": "timestamp",
        "keywords": "keywords",
        
    }

    attribute_is_primitive = {
        "symbols": False,
        "title": True,
        "url": True,
        "source": True,
        "summary": True,
        "image": True,
        "timestamp": True,
        "keywords": False,
        
    }

    def __init__(self, input_json):
        self.symbols: List[StockSymbol]
        self.title: str
        self.url: str
        self.source: str
        self.summary: str
        self.image: str
        self.timestamp: str
        self.keywords: List[str]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Earning(BaseDefinition):
    swagger_name_to_python = {
        "symbol": "symbol",
        "EPSReportDate": "e___psrep_ortdate",
        "EPSReportDateStr": "e___psrep_ort_datestr",
        "fiscalPeriod": "fiscal_period",
        "fiscalEndDate": "fiscal_en_ddate",
        "actualEPS": "actual___eps",
        "consensusEPS": "consensus___eps",
        "estimatedEPS": "estimated___eps",
        "announceTime": "announce_time",
        "numberOfEstimates": "number_o_festimates",
        "EPSSurpriseDollar": "e___pssurpr_isedollar",
        "yearAgo": "year_ago",
        "yearAgoChangePercent": "year_ag_ochan_gepercent",
        "estimatedChangePercent": "estimated_chang_epercent",
        
    }

    attribute_is_primitive = {
        "symbol": True,
        "e___psrep_ortdate": True,
        "e___psrep_ort_datestr": True,
        "fiscal_period": True,
        "fiscal_en_ddate": True,
        "actual___eps": True,
        "consensus___eps": True,
        "estimated___eps": True,
        "announce_time": True,
        "number_o_festimates": True,
        "e___pssurpr_isedollar": True,
        "year_ago": True,
        "year_ag_ochan_gepercent": True,
        "estimated_chang_epercent": True,
        
    }

    def __init__(self, input_json):
        self.symbol: str
        self.e___psrep_ortdate: str
        self.e___psrep_ort_datestr: str
        self.fiscal_period: str
        self.fiscal_en_ddate: str
        self.actual___eps: float
        self.consensus___eps: float
        self.estimated___eps: float
        self.announce_time: str
        self.number_o_festimates: float
        self.e___pssurpr_isedollar: float
        self.year_ago: float
        self.year_ag_ochan_gepercent: float
        self.estimated_chang_epercent: float
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Financial(BaseDefinition):
    swagger_name_to_python = {
        "symbol": "symbol",
        "reportDate": "report_date",
        "reportDateStr": "report_dat_estr",
        "grossProfit": "gross_profit",
        "costOfRevenue": "cost_o_frevenue",
        "operatingRevenue": "operating_revenue",
        "totalRevenue": "total_revenue",
        "operatingIncome": "operating_income",
        "netIncome": "net_income",
        "researchAndDevelopment": "research_an_ddevelopment",
        "operatingExpense": "operating_expense",
        "currentAssets": "current_assets",
        "totalAssets": "total_assets",
        "totalLiabilities": "total_liabilities",
        "currentCash": "current_cash",
        "currentDebt": "current_debt",
        "totalCash": "total_cash",
        "totalDebt": "total_debt",
        "shareholderEquity": "shareholder_equity",
        "cashChange": "cash_change",
        "cashFlow": "cash_flow",
        "operatingGainsLosses": "operating_gain_slosses",
        
    }

    attribute_is_primitive = {
        "symbol": True,
        "report_date": True,
        "report_dat_estr": True,
        "gross_profit": True,
        "cost_o_frevenue": True,
        "operating_revenue": True,
        "total_revenue": True,
        "operating_income": True,
        "net_income": True,
        "research_an_ddevelopment": True,
        "operating_expense": True,
        "current_assets": True,
        "total_assets": True,
        "total_liabilities": True,
        "current_cash": True,
        "current_debt": True,
        "total_cash": True,
        "total_debt": True,
        "shareholder_equity": True,
        "cash_change": True,
        "cash_flow": True,
        "operating_gain_slosses": True,
        
    }

    def __init__(self, input_json):
        self.symbol: str
        self.report_date: str
        self.report_dat_estr: str
        self.gross_profit: float
        self.cost_o_frevenue: float
        self.operating_revenue: float
        self.total_revenue: float
        self.operating_income: float
        self.net_income: float
        self.research_an_ddevelopment: float
        self.operating_expense: float
        self.current_assets: float
        self.total_assets: float
        self.total_liabilities: float
        self.current_cash: float
        self.current_debt: float
        self.total_cash: float
        self.total_debt: float
        self.shareholder_equity: float
        self.cash_change: float
        self.cash_flow: float
        self.operating_gain_slosses: float
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Exchange(BaseDefinition):
    swagger_name_to_python = {
        "id": "i_d_of_the_exchange",
        "type": "type",
        "market": "market",
        "mic": "mic",
        "name": "name",
        "tape": "tape",
        
    }

    attribute_is_primitive = {
        "i_d_of_the_exchange": True,
        "type": True,
        "market": True,
        "mic": True,
        "name": True,
        "tape": True,
        
    }

    def __init__(self, input_json):
        self.i_d_of_the_exchange: float
        self.type: str
        self.market: str
        self.mic: str
        self.name: str
        self.tape: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Error(BaseDefinition):
    swagger_name_to_python = {
        "code": "code",
        "message": "message",
        "fields": "fields",
        
    }

    attribute_is_primitive = {
        "code": True,
        "message": True,
        "fields": True,
        
    }

    def __init__(self, input_json):
        self.code: int
        self.message: str
        self.fields: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class NotFound(BaseDefinition):
    swagger_name_to_python = {
        "message": "message",
        
    }

    attribute_is_primitive = {
        "message": True,
        
    }

    def __init__(self, input_json):
        self.message: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Conflict(BaseDefinition):
    swagger_name_to_python = {
        "message": "message",
        
    }

    attribute_is_primitive = {
        "message": True,
        
    }

    def __init__(self, input_json):
        self.message: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Unauthorized(BaseDefinition):
    swagger_name_to_python = {
        "message": "message",
        
    }

    attribute_is_primitive = {
        "message": True,
        
    }

    def __init__(self, input_json):
        self.message: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class MarketStatus(BaseDefinition):
    swagger_name_to_python = {
        "market": "market",
        "serverTime": "server_time",
        "exchanges": "exchanges",
        "currencies": "currencies",
        
    }

    attribute_is_primitive = {
        "market": True,
        "server_time": True,
        "exchanges": True,
        "currencies": True,
        
    }

    def __init__(self, input_json):
        self.market: str
        self.server_time: str
        self.exchanges: Dict[str, str]
        self.currencies: Dict[str, str]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class MarketHoliday(BaseDefinition):
    swagger_name_to_python = {
        "exchange": "exchange",
        "name": "name",
        "status": "status",
        "date": "date",
        "open": "open",
        "close": "close",
        
    }

    attribute_is_primitive = {
        "exchange": True,
        "name": True,
        "status": True,
        "date": True,
        "open": True,
        "close": True,
        
    }

    def __init__(self, input_json):
        self.exchange: str
        self.name: str
        self.status: str
        self.date: str
        self.open: str
        self.close: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class AnalystRatings(BaseDefinition):
    swagger_name_to_python = {
        "symbol": "symbol",
        "analysts": "analysts",
        "change": "change",
        "strongBuy": "strong_buy",
        "buy": "buy",
        "hold": "hold",
        "sell": "sell",
        "strongSell": "strong_sell",
        "updated": "updated",
        
    }

    attribute_is_primitive = {
        "symbol": True,
        "analysts": True,
        "change": True,
        "strong_buy": False,
        "buy": False,
        "hold": False,
        "sell": False,
        "strong_sell": False,
        "updated": True,
        
    }

    def __init__(self, input_json):
        self.symbol: str
        self.analysts: float
        self.change: float
        self.strong_buy: RatingSection
        self.buy: RatingSection
        self.hold: RatingSection
        self.sell: RatingSection
        self.strong_sell: RatingSection
        self.updated: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class RatingSection(BaseDefinition):
    swagger_name_to_python = {
        "current": "current",
        "month1": "month1",
        "month2": "month2",
        "month3": "month3",
        "month4": "month4",
        "month5": "month5",
        
    }

    attribute_is_primitive = {
        "current": True,
        "month1": True,
        "month2": True,
        "month3": True,
        "month4": True,
        "month5": True,
        
    }

    def __init__(self, input_json):
        self.current: float
        self.month1: float
        self.month2: float
        self.month3: float
        self.month4: float
        self.month5: float
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoTick(BaseDefinition):
    swagger_name_to_python = {
        "price": "price",
        "size": "size",
        "exchange": "exchange",
        "conditions": "conditions",
        "timestamp": "timestamp",
        
    }

    attribute_is_primitive = {
        "price": True,
        "size": True,
        "exchange": True,
        "conditions": False,
        "timestamp": True,
        
    }

    def __init__(self, input_json):
        self.price: int
        self.size: int
        self.exchange: int
        self.conditions: List[int]
        self.timestamp: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoTickJson(BaseDefinition):
    swagger_name_to_python = {
        "p": "trade_price",
        "s": "size_of_the_trade",
        "x": "exchange_the_trade_occured_on",
        "c": "c",
        "t": "timestamp_of_this_trade",
        
    }

    attribute_is_primitive = {
        "trade_price": True,
        "size_of_the_trade": True,
        "exchange_the_trade_occured_on": True,
        "c": False,
        "timestamp_of_this_trade": True,
        
    }

    def __init__(self, input_json):
        self.trade_price: int
        self.size_of_the_trade: int
        self.exchange_the_trade_occured_on: int
        self.c: List[int]
        self.timestamp_of_this_trade: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoExchange(BaseDefinition):
    swagger_name_to_python = {
        "id": "i_d_of_the_exchange",
        "type": "type",
        "market": "market",
        "name": "name",
        "url": "url",
        
    }

    attribute_is_primitive = {
        "i_d_of_the_exchange": True,
        "type": True,
        "market": True,
        "name": True,
        "url": True,
        
    }

    def __init__(self, input_json):
        self.i_d_of_the_exchange: float
        self.type: str
        self.market: str
        self.name: str
        self.url: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoSnapshotTicker(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "day": "day",
        "lastTrade": "last_trade",
        "min": "min",
        "prevDay": "prev_day",
        "todaysChange": "todays_change",
        "todaysChangePerc": "todays_chang_eperc",
        "updated": "updated",
        
    }

    attribute_is_primitive = {
        "ticker": True,
        "day": False,
        "last_trade": False,
        "min": False,
        "prev_day": False,
        "todays_change": True,
        "todays_chang_eperc": True,
        "updated": True,
        
    }

    def __init__(self, input_json):
        self.ticker: str
        self.day: CryptoSnapshotAgg
        self.last_trade: CryptoTickJson
        self.min: CryptoSnapshotAgg
        self.prev_day: CryptoSnapshotAgg
        self.todays_change: int
        self.todays_chang_eperc: int
        self.updated: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoSnapshotBookItem(BaseDefinition):
    swagger_name_to_python = {
        "p": "price_of_this_book_level",
        "x": "exchange_to_size_of_this_price_level",
        
    }

    attribute_is_primitive = {
        "price_of_this_book_level": True,
        "exchange_to_size_of_this_price_level": True,
        
    }

    def __init__(self, input_json):
        self.price_of_this_book_level: int
        self.exchange_to_size_of_this_price_level: Dict[str, str]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoSnapshotTickerBook(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "bids": "bids",
        "asks": "asks",
        "bidCount": "bid_count",
        "askCount": "ask_count",
        "spread": "spread",
        "updated": "updated",
        
    }

    attribute_is_primitive = {
        "ticker": True,
        "bids": False,
        "asks": False,
        "bid_count": True,
        "ask_count": True,
        "spread": True,
        "updated": True,
        
    }

    def __init__(self, input_json):
        self.ticker: str
        self.bids: List[CryptoSnapshotBookItem]
        self.asks: List[CryptoSnapshotBookItem]
        self.bid_count: int
        self.ask_count: int
        self.spread: int
        self.updated: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoSnapshotAgg(BaseDefinition):
    swagger_name_to_python = {
        "c": "close_price",
        "h": "high_price",
        "l": "low_price",
        "o": "open_price",
        "v": "volume",
        
    }

    attribute_is_primitive = {
        "close_price": True,
        "high_price": True,
        "low_price": True,
        "open_price": True,
        "volume": True,
        
    }

    def __init__(self, input_json):
        self.close_price: int
        self.high_price: int
        self.low_price: int
        self.open_price: int
        self.volume: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Forex(BaseDefinition):
    swagger_name_to_python = {
        "a": "ask_price",
        "b": "bid_price",
        "t": "timestamp_of_this_trade",
        
    }

    attribute_is_primitive = {
        "ask_price": True,
        "bid_price": True,
        "timestamp_of_this_trade": True,
        
    }

    def __init__(self, input_json):
        self.ask_price: int
        self.bid_price: int
        self.timestamp_of_this_trade: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LastForexTrade(BaseDefinition):
    swagger_name_to_python = {
        "price": "price",
        "exchange": "exchange",
        "timestamp": "timestamp",
        
    }

    attribute_is_primitive = {
        "price": True,
        "exchange": True,
        "timestamp": True,
        
    }

    def __init__(self, input_json):
        self.price: int
        self.exchange: int
        self.timestamp: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LastForexQuote(BaseDefinition):
    swagger_name_to_python = {
        "ask": "ask",
        "bid": "bid",
        "exchange": "exchange",
        "timestamp": "timestamp",
        
    }

    attribute_is_primitive = {
        "ask": True,
        "bid": True,
        "exchange": True,
        "timestamp": True,
        
    }

    def __init__(self, input_json):
        self.ask: int
        self.bid: int
        self.exchange: int
        self.timestamp: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class ForexAggregate(BaseDefinition):
    swagger_name_to_python = {
        "o": "open_price",
        "c": "close_price",
        "l": "low_price",
        "h": "high_price",
        "v": "volume_of_all_trades",
        "t": "timestamp_of_this_aggregation",
        
    }

    attribute_is_primitive = {
        "open_price": True,
        "close_price": True,
        "low_price": True,
        "high_price": True,
        "volume_of_all_trades": True,
        "timestamp_of_this_aggregation": True,
        
    }

    def __init__(self, input_json):
        self.open_price: int
        self.close_price: int
        self.low_price: int
        self.high_price: int
        self.volume_of_all_trades: int
        self.timestamp_of_this_aggregation: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class ForexSnapshotTicker(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "day": "day",
        "lastTrade": "last_trade",
        "min": "min",
        "prevDay": "prev_day",
        "todaysChange": "todays_change",
        "todaysChangePerc": "todays_chang_eperc",
        "updated": "updated",
        
    }

    attribute_is_primitive = {
        "ticker": True,
        "day": False,
        "last_trade": False,
        "min": False,
        "prev_day": False,
        "todays_change": True,
        "todays_chang_eperc": True,
        "updated": True,
        
    }

    def __init__(self, input_json):
        self.ticker: str
        self.day: ForexSnapshotAgg
        self.last_trade: Forex
        self.min: ForexSnapshotAgg
        self.prev_day: ForexSnapshotAgg
        self.todays_change: int
        self.todays_chang_eperc: int
        self.updated: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class ForexSnapshotAgg(BaseDefinition):
    swagger_name_to_python = {
        "c": "close_price",
        "h": "high_price",
        "l": "low_price",
        "o": "open_price",
        "v": "volume",
        
    }

    attribute_is_primitive = {
        "close_price": True,
        "high_price": True,
        "low_price": True,
        "open_price": True,
        "volume": True,
        
    }

    def __init__(self, input_json):
        self.close_price: int
        self.high_price: int
        self.low_price: int
        self.open_price: int
        self.volume: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Ticker(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "name": "name",
        "market": "market",
        "locale": "locale",
        "currency": "currency",
        "active": "active",
        "primaryExch": "primary_exch",
        "url": "url",
        "updated": "updated",
        "attrs": "attrs",
        "codes": "codes",
        
    }

    attribute_is_primitive = {
        "ticker": False,
        "name": True,
        "market": True,
        "locale": True,
        "currency": True,
        "active": True,
        "primary_exch": True,
        "url": True,
        "updated": True,
        "attrs": True,
        "codes": True,
        
    }

    def __init__(self, input_json):
        self.ticker: StockSymbol
        self.name: str
        self.market: str
        self.locale: str
        self.currency: str
        self.active: bool
        self.primary_exch: str
        self.url: str
        self.updated: str
        self.attrs: Dict[str, str]
        self.codes: Dict[str, str]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Split(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "exDate": "ex_date",
        "paymentDate": "payment_date",
        "recordDate": "record_date",
        "declaredDate": "declared_date",
        "ratio": "ratio",
        "tofactor": "tofactor",
        "forfactor": "forfactor",
        
    }

    attribute_is_primitive = {
        "ticker": False,
        "ex_date": True,
        "payment_date": True,
        "record_date": True,
        "declared_date": True,
        "ratio": True,
        "tofactor": True,
        "forfactor": True,
        
    }

    def __init__(self, input_json):
        self.ticker: TickerSymbol
        self.ex_date: str
        self.payment_date: str
        self.record_date: str
        self.declared_date: str
        self.ratio: float
        self.tofactor: float
        self.forfactor: float
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Financials(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "period": "period",
        "calendarDate": "calendar_date",
        "reportPeriod": "report_period",
        "updated": "updated",
        "accumulatedOtherComprehensiveIncome": "accumulated_othe_rcomprehensi_veincome",
        "assets": "assets",
        "assetsAverage": "assets_average",
        "assetsCurrent": "assets_current",
        "assetTurnover": "asset_turnover",
        "assetsNonCurrent": "assets_no_ncurrent",
        "bookValuePerShare": "book_valu_ep_ershare",
        "capitalExpenditure": "capital_expenditure",
        "cashAndEquivalents": "cash_an_dequivalents",
        "cashAndEquivalentsUSD": "cash_an_dequivalen___tsusd",
        "costOfRevenue": "cost_o_frevenue",
        "consolidatedIncome": "consolidated_income",
        "currentRatio": "current_ratio",
        "debtToEquityRatio": "debt_t_oequi_tyratio",
        "debt": "debt",
        "debtCurrent": "debt_current",
        "debtNonCurrent": "debt_no_ncurrent",
        "debtUSD": "debt___usd",
        "deferredRevenue": "deferred_revenue",
        "depreciationAmortizationAndAccretion": "depreciation_amortizatio_na_ndaccretion",
        "deposits": "deposits",
        "dividendYield": "dividend_yield",
        "dividendsPerBasicCommonShare": "dividends_pe_rbas_iccom_monshare",
        "earningBeforeInterestTaxes": "earning_befor_eintere_sttaxes",
        "earningsBeforeInterestTaxesDepreciationAmortization": "earnings_befor_eintere_stta_xesdeprecia_tionamortization",
        "EBITDAMargin": "e______bitdamargin",
        "earningsBeforeInterestTaxesDepreciationAmortizationUSD": "earnings_befor_eintere_stta_xesdeprecia_tionamortiz___ationusd",
        "earningBeforeInterestTaxesUSD": "earning_befor_eintere_stta___xesusd",
        "earningsBeforeTax": "earnings_befor_etax",
        "earningsPerBasicShare": "earnings_pe_rbas_icshare",
        "earningsPerDilutedShare": "earnings_pe_rdilut_edshare",
        "earningsPerBasicShareUSD": "earnings_pe_rbas_icsh___areusd",
        "shareholdersEquity": "shareholders_equity",
        "averageEquity": "average_equity",
        "shareholdersEquityUSD": "shareholders_equit___yusd",
        "enterpriseValue": "enterprise_value",
        "enterpriseValueOverEBIT": "enterprise_valu_eov____erebit",
        "enterpriseValueOverEBITDA": "enterprise_valu_eov______erebitda",
        "freeCashFlow": "free_cas_hflow",
        "freeCashFlowPerShare": "free_cas_hfl_ow_pershare",
        "foreignCurrencyUSDExchangeRate": "foreign_currenc____yusdexc_hangerate",
        "grossProfit": "gross_profit",
        "grossMargin": "gross_margin",
        "goodwillAndIntangibleAssets": "goodwill_an_dintangib_leassets",
        "interestExpense": "interest_expense",
        "investedCapital": "invested_capital",
        "investedCapitalAverage": "invested_capita_laverage",
        "inventory": "inventory",
        "investments": "investments",
        "investmentsCurrent": "investments_current",
        "investmentsNonCurrent": "investments_no_ncurrent",
        "totalLiabilities": "total_liabilities",
        "currentLiabilities": "current_liabilities",
        "liabilitiesNonCurrent": "liabilities_no_ncurrent",
        "marketCapitalization": "market_capitalization",
        "netCashFlow": "net_cas_hflow",
        "netCashFlowBusinessAcquisitionsDisposals": "net_cas_hfl_owbusin_essacquisit_ionsdisposals",
        "issuanceEquityShares": "issuance_equit_yshares",
        "issuanceDebtSecurities": "issuance_deb_tsecurities",
        "paymentDividendsOtherCashDistributions": "payment_dividend_soth_erc_ashdistributions",
        "netCashFlowFromFinancing": "net_cas_hfl_owf_romfinancing",
        "netCashFlowFromInvesting": "net_cas_hfl_owf_rominvesting",
        "netCashFlowInvestmentAcquisitionsDisposals": "net_cas_hfl_owinvestm_entacquisit_ionsdisposals",
        "netCashFlowFromOperations": "net_cas_hfl_owf_romoperations",
        "effectOfExchangeRateChangesOnCash": "effect_o_fexchan_ger_atecha_n_gesoncash",
        "netIncome": "net_income",
        "netIncomeCommonStock": "net_incom_ecomm_onstock",
        "netIncomeCommonStockUSD": "net_incom_ecomm_onst___ockusd",
        "netLossIncomeFromDiscontinuedOperations": "net_los_sinco_mef_romdisconti_nuedoperations",
        "netIncomeToNonControllingInterests": "net_incom_e_to_noncontrol_linginterests",
        "profitMargin": "profit_margin",
        "operatingExpenses": "operating_expenses",
        "operatingIncome": "operating_income",
        "tradeAndNonTradePayables": "trade_an_dn_ontr_adepayables",
        "payoutRatio": "payout_ratio",
        "priceToBookValue": "price_t_obo_okvalue",
        "priceEarnings": "price_earnings",
        "priceToEarningsRatio": "price_t_oearnin_gsratio",
        "propertyPlantEquipmentNet": "property_plan_tequipme_ntnet",
        "preferredDividendsIncomeStatementImpact": "preferred_dividend_sinco_mestatem_entimpact",
        "sharePriceAdjustedClose": "share_pric_eadjust_edclose",
        "priceSales": "price_sales",
        "priceToSalesRatio": "price_t_osal_esratio",
        "tradeAndNonTradeReceivables": "trade_an_dn_ontr_adereceivables",
        "accumulatedRetainedEarningsDeficit": "accumulated_retaine_dearnin_gsdeficit",
        "revenues": "revenues",
        "revenuesUSD": "revenues___usd",
        "researchAndDevelopmentExpense": "research_an_ddevelopme_ntexpense",
        "returnOnAverageAssets": "return_o_navera_geassets",
        "returnOnAverageEquity": "return_o_navera_geequity",
        "returnOnInvestedCapital": "return_o_ninvest_edcapital",
        "returnOnSales": "return_o_nsales",
        "shareBasedCompensation": "share_base_dcompensation",
        "sellingGeneralAndAdministrativeExpense": "selling_genera_la_ndadministrat_iveexpense",
        "shareFactor": "share_factor",
        "shares": "shares",
        "weightedAverageShares": "weighted_averag_eshares",
        "weightedAverageSharesDiluted": "weighted_averag_eshar_esdiluted",
        "salesPerShare": "sales_pe_rshare",
        "tangibleAssetValue": "tangible_asse_tvalue",
        "taxAssets": "tax_assets",
        "incomeTaxExpense": "income_ta_xexpense",
        "taxLiabilities": "tax_liabilities",
        "tangibleAssetsBookValuePerShare": "tangible_asset_sbo_okva_lu_epershare",
        "workingCapital": "working_capital",
        
    }

    attribute_is_primitive = {
        "ticker": False,
        "period": True,
        "calendar_date": True,
        "report_period": True,
        "updated": True,
        "accumulated_othe_rcomprehensi_veincome": True,
        "assets": True,
        "assets_average": True,
        "assets_current": True,
        "asset_turnover": True,
        "assets_no_ncurrent": True,
        "book_valu_ep_ershare": True,
        "capital_expenditure": True,
        "cash_an_dequivalents": True,
        "cash_an_dequivalen___tsusd": True,
        "cost_o_frevenue": True,
        "consolidated_income": True,
        "current_ratio": True,
        "debt_t_oequi_tyratio": True,
        "debt": True,
        "debt_current": True,
        "debt_no_ncurrent": True,
        "debt___usd": True,
        "deferred_revenue": True,
        "depreciation_amortizatio_na_ndaccretion": True,
        "deposits": True,
        "dividend_yield": True,
        "dividends_pe_rbas_iccom_monshare": True,
        "earning_befor_eintere_sttaxes": True,
        "earnings_befor_eintere_stta_xesdeprecia_tionamortization": True,
        "e______bitdamargin": True,
        "earnings_befor_eintere_stta_xesdeprecia_tionamortiz___ationusd": True,
        "earning_befor_eintere_stta___xesusd": True,
        "earnings_befor_etax": True,
        "earnings_pe_rbas_icshare": True,
        "earnings_pe_rdilut_edshare": True,
        "earnings_pe_rbas_icsh___areusd": True,
        "shareholders_equity": True,
        "average_equity": True,
        "shareholders_equit___yusd": True,
        "enterprise_value": True,
        "enterprise_valu_eov____erebit": True,
        "enterprise_valu_eov______erebitda": True,
        "free_cas_hflow": True,
        "free_cas_hfl_ow_pershare": True,
        "foreign_currenc____yusdexc_hangerate": True,
        "gross_profit": True,
        "gross_margin": True,
        "goodwill_an_dintangib_leassets": True,
        "interest_expense": True,
        "invested_capital": True,
        "invested_capita_laverage": True,
        "inventory": True,
        "investments": True,
        "investments_current": True,
        "investments_no_ncurrent": True,
        "total_liabilities": True,
        "current_liabilities": True,
        "liabilities_no_ncurrent": True,
        "market_capitalization": True,
        "net_cas_hflow": True,
        "net_cas_hfl_owbusin_essacquisit_ionsdisposals": True,
        "issuance_equit_yshares": True,
        "issuance_deb_tsecurities": True,
        "payment_dividend_soth_erc_ashdistributions": True,
        "net_cas_hfl_owf_romfinancing": True,
        "net_cas_hfl_owf_rominvesting": True,
        "net_cas_hfl_owinvestm_entacquisit_ionsdisposals": True,
        "net_cas_hfl_owf_romoperations": True,
        "effect_o_fexchan_ger_atecha_n_gesoncash": True,
        "net_income": True,
        "net_incom_ecomm_onstock": True,
        "net_incom_ecomm_onst___ockusd": True,
        "net_los_sinco_mef_romdisconti_nuedoperations": True,
        "net_incom_e_to_noncontrol_linginterests": True,
        "profit_margin": True,
        "operating_expenses": True,
        "operating_income": True,
        "trade_an_dn_ontr_adepayables": True,
        "payout_ratio": True,
        "price_t_obo_okvalue": True,
        "price_earnings": True,
        "price_t_oearnin_gsratio": True,
        "property_plan_tequipme_ntnet": True,
        "preferred_dividend_sinco_mestatem_entimpact": True,
        "share_pric_eadjust_edclose": True,
        "price_sales": True,
        "price_t_osal_esratio": True,
        "trade_an_dn_ontr_adereceivables": True,
        "accumulated_retaine_dearnin_gsdeficit": True,
        "revenues": True,
        "revenues___usd": True,
        "research_an_ddevelopme_ntexpense": True,
        "return_o_navera_geassets": True,
        "return_o_navera_geequity": True,
        "return_o_ninvest_edcapital": True,
        "return_o_nsales": True,
        "share_base_dcompensation": True,
        "selling_genera_la_ndadministrat_iveexpense": True,
        "share_factor": True,
        "shares": True,
        "weighted_averag_eshares": True,
        "weighted_averag_eshar_esdiluted": True,
        "sales_pe_rshare": True,
        "tangible_asse_tvalue": True,
        "tax_assets": True,
        "income_ta_xexpense": True,
        "tax_liabilities": True,
        "tangible_asset_sbo_okva_lu_epershare": True,
        "working_capital": True,
        
    }

    def __init__(self, input_json):
        self.ticker: TickerSymbol
        self.period: str
        self.calendar_date: str
        self.report_period: str
        self.updated: str
        self.accumulated_othe_rcomprehensi_veincome: int
        self.assets: int
        self.assets_average: int
        self.assets_current: int
        self.asset_turnover: int
        self.assets_no_ncurrent: int
        self.book_valu_ep_ershare: int
        self.capital_expenditure: int
        self.cash_an_dequivalents: int
        self.cash_an_dequivalen___tsusd: int
        self.cost_o_frevenue: int
        self.consolidated_income: int
        self.current_ratio: int
        self.debt_t_oequi_tyratio: int
        self.debt: int
        self.debt_current: int
        self.debt_no_ncurrent: int
        self.debt___usd: int
        self.deferred_revenue: int
        self.depreciation_amortizatio_na_ndaccretion: int
        self.deposits: int
        self.dividend_yield: int
        self.dividends_pe_rbas_iccom_monshare: int
        self.earning_befor_eintere_sttaxes: int
        self.earnings_befor_eintere_stta_xesdeprecia_tionamortization: int
        self.e______bitdamargin: int
        self.earnings_befor_eintere_stta_xesdeprecia_tionamortiz___ationusd: int
        self.earning_befor_eintere_stta___xesusd: int
        self.earnings_befor_etax: int
        self.earnings_pe_rbas_icshare: int
        self.earnings_pe_rdilut_edshare: int
        self.earnings_pe_rbas_icsh___areusd: int
        self.shareholders_equity: int
        self.average_equity: int
        self.shareholders_equit___yusd: int
        self.enterprise_value: int
        self.enterprise_valu_eov____erebit: int
        self.enterprise_valu_eov______erebitda: int
        self.free_cas_hflow: int
        self.free_cas_hfl_ow_pershare: int
        self.foreign_currenc____yusdexc_hangerate: int
        self.gross_profit: int
        self.gross_margin: int
        self.goodwill_an_dintangib_leassets: int
        self.interest_expense: int
        self.invested_capital: int
        self.invested_capita_laverage: int
        self.inventory: int
        self.investments: int
        self.investments_current: int
        self.investments_no_ncurrent: int
        self.total_liabilities: int
        self.current_liabilities: int
        self.liabilities_no_ncurrent: int
        self.market_capitalization: int
        self.net_cas_hflow: int
        self.net_cas_hfl_owbusin_essacquisit_ionsdisposals: int
        self.issuance_equit_yshares: int
        self.issuance_deb_tsecurities: int
        self.payment_dividend_soth_erc_ashdistributions: int
        self.net_cas_hfl_owf_romfinancing: int
        self.net_cas_hfl_owf_rominvesting: int
        self.net_cas_hfl_owinvestm_entacquisit_ionsdisposals: int
        self.net_cas_hfl_owf_romoperations: int
        self.effect_o_fexchan_ger_atecha_n_gesoncash: int
        self.net_income: int
        self.net_incom_ecomm_onstock: int
        self.net_incom_ecomm_onst___ockusd: int
        self.net_los_sinco_mef_romdisconti_nuedoperations: int
        self.net_incom_e_to_noncontrol_linginterests: int
        self.profit_margin: int
        self.operating_expenses: int
        self.operating_income: int
        self.trade_an_dn_ontr_adepayables: int
        self.payout_ratio: int
        self.price_t_obo_okvalue: int
        self.price_earnings: int
        self.price_t_oearnin_gsratio: int
        self.property_plan_tequipme_ntnet: int
        self.preferred_dividend_sinco_mestatem_entimpact: int
        self.share_pric_eadjust_edclose: int
        self.price_sales: int
        self.price_t_osal_esratio: int
        self.trade_an_dn_ontr_adereceivables: int
        self.accumulated_retaine_dearnin_gsdeficit: int
        self.revenues: int
        self.revenues___usd: int
        self.research_an_ddevelopme_ntexpense: int
        self.return_o_navera_geassets: int
        self.return_o_navera_geequity: int
        self.return_o_ninvest_edcapital: int
        self.return_o_nsales: int
        self.share_base_dcompensation: int
        self.selling_genera_la_ndadministrat_iveexpense: int
        self.share_factor: int
        self.shares: int
        self.weighted_averag_eshares: int
        self.weighted_averag_eshar_esdiluted: int
        self.sales_pe_rshare: int
        self.tangible_asse_tvalue: int
        self.tax_assets: int
        self.income_ta_xexpense: int
        self.tax_liabilities: int
        self.tangible_asset_sbo_okva_lu_epershare: int
        self.working_capital: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Trade(BaseDefinition):
    swagger_name_to_python = {
        "c1": "condition_1_of_this_trade",
        "c2": "condition_2_of_this_trade",
        "c3": "condition_3_of_this_trade",
        "c4": "condition_4_of_this_trade",
        "e": "the_exchange_this_trade_happened_on",
        "p": "price_of_the_trade",
        "s": "size_of_the_trade",
        "t": "timestamp_of_this_trade",
        
    }

    attribute_is_primitive = {
        "condition_1_of_this_trade": True,
        "condition_2_of_this_trade": True,
        "condition_3_of_this_trade": True,
        "condition_4_of_this_trade": True,
        "the_exchange_this_trade_happened_on": True,
        "price_of_the_trade": True,
        "size_of_the_trade": True,
        "timestamp_of_this_trade": True,
        
    }

    def __init__(self, input_json):
        self.condition_1_of_this_trade: int
        self.condition_2_of_this_trade: int
        self.condition_3_of_this_trade: int
        self.condition_4_of_this_trade: int
        self.the_exchange_this_trade_happened_on: str
        self.price_of_the_trade: int
        self.size_of_the_trade: int
        self.timestamp_of_this_trade: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StocksSnapshotTicker(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "day": "day",
        "lastTrade": "last_trade",
        "lastQuote": "last_quote",
        "min": "min",
        "prevDay": "prev_day",
        "todaysChange": "todays_change",
        "todaysChangePerc": "todays_chang_eperc",
        "updated": "updated",
        
    }

    attribute_is_primitive = {
        "ticker": True,
        "day": False,
        "last_trade": False,
        "last_quote": False,
        "min": False,
        "prev_day": False,
        "todays_change": True,
        "todays_chang_eperc": True,
        "updated": True,
        
    }

    def __init__(self, input_json):
        self.ticker: str
        self.day: StocksSnapshotAgg
        self.last_trade: Trade
        self.last_quote: StocksSnapshotQuote
        self.min: StocksSnapshotAgg
        self.prev_day: StocksSnapshotAgg
        self.todays_change: int
        self.todays_chang_eperc: int
        self.updated: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StocksSnapshotBookItem(BaseDefinition):
    swagger_name_to_python = {
        "p": "price_of_this_book_level",
        "x": "exchange_to_size_of_this_price_level",
        
    }

    attribute_is_primitive = {
        "price_of_this_book_level": True,
        "exchange_to_size_of_this_price_level": True,
        
    }

    def __init__(self, input_json):
        self.price_of_this_book_level: int
        self.exchange_to_size_of_this_price_level: Dict[str, str]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StocksSnapshotTickerBook(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "bids": "bids",
        "asks": "asks",
        "bidCount": "bid_count",
        "askCount": "ask_count",
        "spread": "spread",
        "updated": "updated",
        
    }

    attribute_is_primitive = {
        "ticker": True,
        "bids": False,
        "asks": False,
        "bid_count": True,
        "ask_count": True,
        "spread": True,
        "updated": True,
        
    }

    def __init__(self, input_json):
        self.ticker: str
        self.bids: List[StocksSnapshotBookItem]
        self.asks: List[StocksSnapshotBookItem]
        self.bid_count: int
        self.ask_count: int
        self.spread: int
        self.updated: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StocksV2Trade(BaseDefinition):
    swagger_name_to_python = {
        "T": "ticker_of_the_object",
        "t": "nanosecond_accuracy_s__ip_unix_timestamp",
        "y": "nanosecond_accuracy_participant_exchange_unix_timestamp",
        "f": "nanosecond_accuracy_t__rf",
        "q": "sequence_number",
        "i": "trade_i_d",
        "x": "exchange_i_d",
        "s": "size_volume_of_the_trade",
        "c": "c",
        "p": "price_of_the_trade",
        "z": "tape_where_trade_occured",
        
    }

    attribute_is_primitive = {
        "ticker_of_the_object": True,
        "nanosecond_accuracy_s__ip_unix_timestamp": True,
        "nanosecond_accuracy_participant_exchange_unix_timestamp": True,
        "nanosecond_accuracy_t__rf": True,
        "sequence_number": True,
        "trade_i_d": True,
        "exchange_i_d": True,
        "size_volume_of_the_trade": True,
        "c": False,
        "price_of_the_trade": True,
        "tape_where_trade_occured": True,
        
    }

    def __init__(self, input_json):
        self.ticker_of_the_object: str
        self.nanosecond_accuracy_s__ip_unix_timestamp: int
        self.nanosecond_accuracy_participant_exchange_unix_timestamp: int
        self.nanosecond_accuracy_t__rf: int
        self.sequence_number: int
        self.trade_i_d: str
        self.exchange_i_d: int
        self.size_volume_of_the_trade: int
        self.c: List[int]
        self.price_of_the_trade: int
        self.tape_where_trade_occured: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StocksV2NBBO(BaseDefinition):
    swagger_name_to_python = {
        "T": "ticker_of_the_object",
        "t": "nanosecond_accuracy_s__ip_unix_timestamp",
        "y": "nanosecond_accuracy_participant_exchange_unix_timestamp",
        "f": "nanosecond_accuracy_t__rf",
        "q": "sequence_number",
        "c": "c",
        "i": "i",
        "p": "b__id_price",
        "x": "b__id_exchange__id",
        "s": "b__id_size",
        "P": "a__sk_price",
        "X": "a__sk_exchange__id",
        "S": "a__sk_size",
        "z": "tape_where_trade_occured",
        
    }

    attribute_is_primitive = {
        "ticker_of_the_object": True,
        "nanosecond_accuracy_s__ip_unix_timestamp": True,
        "nanosecond_accuracy_participant_exchange_unix_timestamp": True,
        "nanosecond_accuracy_t__rf": True,
        "sequence_number": True,
        "c": False,
        "i": False,
        "b__id_price": True,
        "b__id_exchange__id": True,
        "b__id_size": True,
        "a__sk_price": True,
        "a__sk_exchange__id": True,
        "a__sk_size": True,
        "tape_where_trade_occured": True,
        
    }

    def __init__(self, input_json):
        self.ticker_of_the_object: str
        self.nanosecond_accuracy_s__ip_unix_timestamp: int
        self.nanosecond_accuracy_participant_exchange_unix_timestamp: int
        self.nanosecond_accuracy_t__rf: int
        self.sequence_number: int
        self.c: List[int]
        self.i: List[int]
        self.b__id_price: int
        self.b__id_exchange__id: int
        self.b__id_size: int
        self.a__sk_price: int
        self.a__sk_exchange__id: int
        self.a__sk_size: int
        self.tape_where_trade_occured: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StocksSnapshotAgg(BaseDefinition):
    swagger_name_to_python = {
        "c": "close_price",
        "h": "high_price",
        "l": "low_price",
        "o": "open_price",
        "v": "volume",
        
    }

    attribute_is_primitive = {
        "close_price": True,
        "high_price": True,
        "low_price": True,
        "open_price": True,
        "volume": True,
        
    }

    def __init__(self, input_json):
        self.close_price: int
        self.high_price: int
        self.low_price: int
        self.open_price: int
        self.volume: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StocksSnapshotQuote(BaseDefinition):
    swagger_name_to_python = {
        "p": "bid_price",
        "s": "bid_size_in_lots",
        "P": "ask_price",
        "S": "ask_size_in_lots",
        "t": "last_updated_timestamp",
        
    }

    attribute_is_primitive = {
        "bid_price": True,
        "bid_size_in_lots": True,
        "ask_price": True,
        "ask_size_in_lots": True,
        "last_updated_timestamp": True,
        
    }

    def __init__(self, input_json):
        self.bid_price: int
        self.bid_size_in_lots: int
        self.ask_price: int
        self.ask_size_in_lots: int
        self.last_updated_timestamp: int
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class Aggv2(BaseDefinition):
    swagger_name_to_python = {
        "T": "ticker_symbol",
        "v": "volume",
        "o": "open",
        "c": "close",
        "h": "high",
        "l": "low",
        "t": "unix_msec_timestamp",
        "n": "number_of_items_in_aggregate_window",
        
    }

    attribute_is_primitive = {
        "ticker_symbol": True,
        "volume": True,
        "open": True,
        "close": True,
        "high": True,
        "low": True,
        "unix_msec_timestamp": True,
        "number_of_items_in_aggregate_window": True,
        
    }

    def __init__(self, input_json):
        self.ticker_symbol: str
        self.volume: int
        self.open: int
        self.close: int
        self.high: int
        self.low: int
        self.unix_msec_timestamp: float
        self.number_of_items_in_aggregate_window: float
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class AggResponse(BaseDefinition):
    swagger_name_to_python = {
        "ticker": "ticker",
        "status": "status",
        "adjusted": "adjusted",
        "queryCount": "query_count",
        "resultsCount": "results_count",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "ticker": True,
        "status": True,
        "adjusted": True,
        "query_count": True,
        "results_count": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.ticker: str
        self.status: str
        self.adjusted: bool
        self.query_count: float
        self.results_count: float
        self.results: List[Aggv2]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class TickersApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "Symbol": "symbol",
        
    }

    attribute_is_primitive = {
        "symbol": False,
        
    }

    def __init__(self, input_json):
        self.symbol: List[Symbol]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class TickerTypesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "status": True,
        "results": True,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.results: Dict[str, str]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class TickerDetailsApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "company": "company",
        
    }

    attribute_is_primitive = {
        "company": False,
        
    }

    def __init__(self, input_json):
        self.company: Company
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class TickerNewsApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "News": "news",
        
    }

    attribute_is_primitive = {
        "news": False,
        
    }

    def __init__(self, input_json):
        self.news: List[News]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class MarketsApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "status": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.results: List[Dict[str, str]]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LocalesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "status": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.results: List[Dict[str, str]]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StockSplitsApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "count": "count",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "status": True,
        "count": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.count: float
        self.results: List[Split]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StockDividendsApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "count": "count",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "status": True,
        "count": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.count: float
        self.results: List[Dividend]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class StockFinancialsApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "count": "count",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "status": True,
        "count": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.count: float
        self.results: List[Financials]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class MarketStatusApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "marketstatus": "marketstatus",
        
    }

    attribute_is_primitive = {
        "marketstatus": False,
        
    }

    def __init__(self, input_json):
        self.marketstatus: MarketStatus
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class MarketHolidaysApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "MarketHoliday": "market_holiday",
        
    }

    attribute_is_primitive = {
        "market_holiday": False,
        
    }

    def __init__(self, input_json):
        self.market_holiday: List[MarketHoliday]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class ExchangesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "Exchange": "exchange",
        
    }

    attribute_is_primitive = {
        "exchange": False,
        
    }

    def __init__(self, input_json):
        self.exchange: List[Exchange]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class HistoricTradesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "symbol": "symbol",
        "ticks": "ticks",
        
    }

    attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "symbol": True,
        "ticks": False,
        
    }

    def __init__(self, input_json):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.symbol: str
        self.ticks: List[Trade]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class HistoricTradesV2ApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "results_count": "results_count",
        "db_latency": "db_latency",
        "success": "success",
        "ticker": "ticker",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "results_count": True,
        "db_latency": True,
        "success": True,
        "ticker": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.results_count: int
        self.db_latency: int
        self.success: bool
        self.ticker: str
        self.results: List[StocksV2Trade]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class HistoricQuotesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "symbol": "symbol",
        "ticks": "ticks",
        
    }

    attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "symbol": True,
        "ticks": False,
        
    }

    def __init__(self, input_json):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.symbol: str
        self.ticks: List[Quote]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class HistoricNBboQuotesV2ApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "results_count": "results_count",
        "db_latency": "db_latency",
        "success": "success",
        "ticker": "ticker",
        "results": "results",
        
    }

    attribute_is_primitive = {
        "results_count": True,
        "db_latency": True,
        "success": True,
        "ticker": True,
        "results": False,
        
    }

    def __init__(self, input_json):
        self.results_count: int
        self.db_latency: int
        self.success: bool
        self.ticker: str
        self.results: List[StocksV2NBBO]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LastTradeForASymbolApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",
        
    }

    attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.symbol: str
        self.last: LastTrade
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LastQuoteForASymbolApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",
        
    }

    attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.symbol: str
        self.last: LastQuote
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class DailyOpenCloseApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "symbol": "symbol",
        "open": "open",
        "close": "close",
        "afterHours": "after_hours",
        
    }

    attribute_is_primitive = {
        "symbol": True,
        "open": False,
        "close": False,
        "after_hours": False,
        
    }

    def __init__(self, input_json):
        self.symbol: str
        self.open: HistTrade
        self.close: HistTrade
        self.after_hours: HistTrade
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class ConditionMappingsApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "conditiontypemap": "conditiontypemap",
        
    }

    attribute_is_primitive = {
        "conditiontypemap": False,
        
    }

    def __init__(self, input_json):
        self.conditiontypemap: ConditionTypeMap
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotAllTickersApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",
        
    }

    attribute_is_primitive = {
        "status": True,
        "tickers": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.tickers: List[StocksSnapshotTicker]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotSingleTickerApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "ticker": "ticker",
        
    }

    attribute_is_primitive = {
        "status": True,
        "ticker": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.ticker: StocksSnapshotTicker
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotGainersLosersApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",
        
    }

    attribute_is_primitive = {
        "status": True,
        "tickers": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.tickers: List[StocksSnapshotTicker]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class PreviousCloseApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "aggresponse": "aggresponse",
        
    }

    attribute_is_primitive = {
        "aggresponse": False,
        
    }

    def __init__(self, input_json):
        self.aggresponse: AggResponse
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class AggregatesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "aggresponse": "aggresponse",
        
    }

    attribute_is_primitive = {
        "aggresponse": False,
        
    }

    def __init__(self, input_json):
        self.aggresponse: AggResponse
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class GroupedDailyApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "aggresponse": "aggresponse",
        
    }

    attribute_is_primitive = {
        "aggresponse": False,
        
    }

    def __init__(self, input_json):
        self.aggresponse: AggResponse
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class HistoricForexTicksApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "pair": "pair",
        "ticks": "ticks",
        
    }

    attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "pair": True,
        "ticks": False,
        
    }

    def __init__(self, input_json):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.pair: str
        self.ticks: List[Forex]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class RealTimeCurrencyConversionApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "from": "from_",
        "to": "to_currency_symbol",
        "initialAmount": "initial_amount",
        "converted": "converted",
        "lastTrade": "last_trade",
        "symbol": "symbol",
        
    }

    attribute_is_primitive = {
        "status": True,
        "from_": True,
        "to_currency_symbol": True,
        "initial_amount": True,
        "converted": True,
        "last_trade": False,
        "symbol": True,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.from_: str
        self.to_currency_symbol: str
        self.initial_amount: float
        self.converted: float
        self.last_trade: LastForexTrade
        self.symbol: str
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LastQuoteForACurrencyPairApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",
        
    }

    attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.symbol: str
        self.last: LastForexQuote
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotAllTickersApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",
        
    }

    attribute_is_primitive = {
        "status": True,
        "tickers": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.tickers: List[ForexSnapshotTicker]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotGainersLosersApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",
        
    }

    attribute_is_primitive = {
        "status": True,
        "tickers": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.tickers: List[ForexSnapshotTicker]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class CryptoExchangesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "CryptoExchange": "crypto_exchange",
        
    }

    attribute_is_primitive = {
        "crypto_exchange": False,
        
    }

    def __init__(self, input_json):
        self.crypto_exchange: List[CryptoExchange]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class LastTradeForACryptoPairApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",
        "lastAverage": "last_average",
        
    }

    attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,
        "last_average": True,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.symbol: str
        self.last: CryptoTick
        self.last_average: Dict[str, str]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class DailyOpenCloseApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "symbol": "symbol",
        "isUTC": "is___utc",
        "day": "day",
        "open": "open",
        "close": "close",
        "openTrades": "open_trades",
        "closingTrades": "closing_trades",
        
    }

    attribute_is_primitive = {
        "symbol": True,
        "is___utc": True,
        "day": True,
        "open": True,
        "close": True,
        "open_trades": False,
        "closing_trades": False,
        
    }

    def __init__(self, input_json):
        self.symbol: str
        self.is___utc: bool
        self.day: str
        self.open: int
        self.close: int
        self.open_trades: List[CryptoTickJson]
        self.closing_trades: List[CryptoTickJson]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class HistoricCryptoTradesApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "symbol": "symbol",
        "ticks": "ticks",
        
    }

    attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "symbol": True,
        "ticks": False,
        
    }

    def __init__(self, input_json):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.symbol: str
        self.ticks: List[CryptoTickJson]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotAllTickersApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",
        
    }

    attribute_is_primitive = {
        "status": True,
        "tickers": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.tickers: List[CryptoSnapshotTicker]
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotSingleTickerApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "ticker": "ticker",
        
    }

    attribute_is_primitive = {
        "status": True,
        "ticker": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.ticker: CryptoSnapshotTicker
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotSingleTickerFullBookApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "data": "data",
        
    }

    attribute_is_primitive = {
        "status": True,
        "data": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.data: CryptoSnapshotTickerBook
        
        self._unmarshal_json(input_json)


# noinspection SpellCheckingInspection
class SnapshotGainersLosersApiResponse(BaseDefinition):
    swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",
        
    }

    attribute_is_primitive = {
        "status": True,
        "tickers": False,
        
    }

    def __init__(self, input_json):
        self.status: str
        self.tickers: List[CryptoSnapshotTicker]
        
        self._unmarshal_json(input_json)

