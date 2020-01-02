import keyword
from typing import List, Dict, Any

from polygon.rest import models


class Definition:
    _swagger_name_to_python: Dict[str, str]
    _attribute_is_primitive: Dict[str, bool]
    _attributes_to_types: Dict[str, Any]

    def unmarshal_json(self, input_json):
        if isinstance(input_json, list):
            list_attribute_name = list(self._swagger_name_to_python.values())[0]
            if list_attribute_name in self._attributes_to_types:
                list_type = self._attributes_to_types[list_attribute_name]
                known_type = list_type.split("[")[1][:-1]
                list_items = self._unmarshal_json_list(input_json, known_type)
            else:
                list_items = input_json
            self.__setattr__(list_attribute_name, list_items)
            return self
        elif isinstance(input_json, dict):
            self._unmarshal_json_object(input_json)
            return self
        elif isinstance(input_json, float) or isinstance(input_json, int):
            return input_json

    @staticmethod
    def _unmarshal_json_list(input_json, known_type):
        items = []
        for item in input_json:
            new_item = models.name_to_class[known_type]()
            items.append(new_item._unmarshal_json_object(item))

        return items

    def _unmarshal_json_object(self, input_json):
        for key, value in input_json.items():
            if key in self._swagger_name_to_python:
                attribute_name = self._swagger_name_to_python[key]
                if not self._attribute_is_primitive[attribute_name]:
                    if attribute_name in self._attributes_to_types:
                        attribute_type = self._attributes_to_types[attribute_name]
                        if attribute_type in models.name_to_class:
                            model = models.name_to_class[attribute_type]()
                            value = model.unmarshal_json(input_json[key])
            else:
                attribute_name = key + ('_' if keyword.iskeyword(key) else '')

            self.__setattr__(attribute_name, value)
        return self


# noinspection SpellCheckingInspection
class LastTrade(Definition):
    _swagger_name_to_python = {
        "price": "price",
        "size": "size",
        "exchange": "exchange",
        "cond1": "cond1",
        "cond2": "cond2",
        "cond3": "cond3",
        "cond4": "cond4",
        "timestamp": "timestamp",

    }

    _attribute_is_primitive = {
        "price": True,
        "size": True,
        "exchange": True,
        "cond1": True,
        "cond2": True,
        "cond3": True,
        "cond4": True,
        "timestamp": True,

    }

    _attributes_to_types = {
        "price": "int",
        "size": "int",
        "exchange": "int",
        "cond1": "int",
        "cond2": "int",
        "cond3": "int",
        "cond4": "int",
        "timestamp": "int",

    }

    def __init__(self):
        self.price: int
        self.size: int
        self.exchange: int
        self.cond1: int
        self.cond2: int
        self.cond3: int
        self.cond4: int
        self.timestamp: int


# noinspection SpellCheckingInspection
class LastQuote(Definition):
    _swagger_name_to_python = {
        "askprice": "askprice",
        "asksize": "asksize",
        "askexchange": "askexchange",
        "bidprice": "bidprice",
        "bidsize": "bidsize",
        "bidexchange": "bidexchange",
        "timestamp": "timestamp",

    }

    _attribute_is_primitive = {
        "askprice": True,
        "asksize": True,
        "askexchange": True,
        "bidprice": True,
        "bidsize": True,
        "bidexchange": True,
        "timestamp": True,

    }

    _attributes_to_types = {
        "askprice": "int",
        "asksize": "int",
        "askexchange": "int",
        "bidprice": "int",
        "bidsize": "int",
        "bidexchange": "int",
        "timestamp": "int",

    }

    def __init__(self):
        self.askprice: int
        self.asksize: int
        self.askexchange: int
        self.bidprice: int
        self.bidsize: int
        self.bidexchange: int
        self.timestamp: int


# noinspection SpellCheckingInspection
class HistTrade(Definition):
    _swagger_name_to_python = {
        "condition1": "condition1",
        "condition2": "condition2",
        "condition3": "condition3",
        "condition4": "condition4",
        "exchange": "exchange",
        "price": "price",
        "size": "size",
        "timestamp": "timestamp",

    }

    _attribute_is_primitive = {
        "condition1": True,
        "condition2": True,
        "condition3": True,
        "condition4": True,
        "exchange": True,
        "price": True,
        "size": True,
        "timestamp": True,

    }

    _attributes_to_types = {
        "condition1": "int",
        "condition2": "int",
        "condition3": "int",
        "condition4": "int",
        "exchange": "str",
        "price": "int",
        "size": "int",
        "timestamp": "str",

    }

    def __init__(self):
        self.condition1: int
        self.condition2: int
        self.condition3: int
        self.condition4: int
        self.exchange: str
        self.price: int
        self.size: int
        self.timestamp: str


# noinspection SpellCheckingInspection
class Quote(Definition):
    _swagger_name_to_python = {
        "c": "condition_of_this_quote",
        "bE": "bid_exchange",
        "aE": "ask_exchange",
        "aP": "ask_price",
        "bP": "bid_price",
        "bS": "bid_size",
        "aS": "ask_size",
        "t": "timestamp_of_this_trade",

    }

    _attribute_is_primitive = {
        "condition_of_this_quote": True,
        "bid_exchange": True,
        "ask_exchange": True,
        "ask_price": True,
        "bid_price": True,
        "bid_size": True,
        "ask_size": True,
        "timestamp_of_this_trade": True,

    }

    _attributes_to_types = {
        "condition_of_this_quote": "int",
        "bid_exchange": "str",
        "ask_exchange": "str",
        "ask_price": "int",
        "bid_price": "int",
        "bid_size": "int",
        "ask_size": "int",
        "timestamp_of_this_trade": "int",

    }

    def __init__(self):
        self.condition_of_this_quote: int
        self.bid_exchange: str
        self.ask_exchange: str
        self.ask_price: int
        self.bid_price: int
        self.bid_size: int
        self.ask_size: int
        self.timestamp_of_this_trade: int


# noinspection SpellCheckingInspection
class Aggregate(Definition):
    _swagger_name_to_python = {
        "o": "open_price",
        "c": "close_price",
        "l": "low_price",
        "h": "high_price",
        "v": "total_volume_of_all_trades",
        "k": "transactions",
        "t": "timestamp_of_this_aggregation",

    }

    _attribute_is_primitive = {
        "open_price": True,
        "close_price": True,
        "low_price": True,
        "high_price": True,
        "total_volume_of_all_trades": True,
        "transactions": True,
        "timestamp_of_this_aggregation": True,

    }

    _attributes_to_types = {
        "open_price": "int",
        "close_price": "int",
        "low_price": "int",
        "high_price": "int",
        "total_volume_of_all_trades": "int",
        "transactions": "int",
        "timestamp_of_this_aggregation": "int",

    }

    def __init__(self):
        self.open_price: int
        self.close_price: int
        self.low_price: int
        self.high_price: int
        self.total_volume_of_all_trades: int
        self.transactions: int
        self.timestamp_of_this_aggregation: int


# noinspection SpellCheckingInspection
class Company(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "logo": "str",
        "exchange": "str",
        "name": "str",
        "symbol": "StockSymbol",
        "listdate": "str",
        "cik": "str",
        "bloomberg": "str",
        "figi": "str",
        "lei": "str",
        "sic": "float",
        "country": "str",
        "industry": "str",
        "sector": "str",
        "marketcap": "float",
        "employees": "float",
        "phone": "str",
        "ceo": "str",
        "url": "str",
        "description": "str",
        "similar": "List[StockSymbol]",
        "tags": "List[str]",
        "updated": "str",

    }

    def __init__(self):
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


# noinspection SpellCheckingInspection
class Symbol(Definition):
    _swagger_name_to_python = {
        "symbol": "symbol",
        "name": "name",
        "type": "type",
        "url": "url",
        "updated": "updated",
        "isOTC": "is___otc",

    }

    _attribute_is_primitive = {
        "symbol": False,
        "name": True,
        "type": True,
        "url": True,
        "updated": True,
        "is___otc": True,

    }

    _attributes_to_types = {
        "symbol": "StockSymbol",
        "name": "str",
        "type": "str",
        "url": "str",
        "updated": "str",
        "is___otc": "bool",

    }

    def __init__(self):
        self.symbol: StockSymbol
        self.name: str
        self.type: str
        self.url: str
        self.updated: str
        self.is___otc: bool


# noinspection SpellCheckingInspection
class Dividend(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "symbol": "StockSymbol",
        "type": "str",
        "ex_date": "str",
        "payment_date": "str",
        "record_date": "str",
        "declared_date": "str",
        "amount": "float",
        "qualified": "str",
        "flag": "str",

    }

    def __init__(self):
        self.symbol: StockSymbol
        self.type: str
        self.ex_date: str
        self.payment_date: str
        self.record_date: str
        self.declared_date: str
        self.amount: float
        self.qualified: str
        self.flag: str


# noinspection SpellCheckingInspection
class News(Definition):
    _swagger_name_to_python = {
        "symbols": "symbols",
        "title": "title",
        "url": "url",
        "source": "source",
        "summary": "summary",
        "image": "image",
        "timestamp": "timestamp",
        "keywords": "keywords",

    }

    _attribute_is_primitive = {
        "symbols": False,
        "title": True,
        "url": True,
        "source": True,
        "summary": True,
        "image": True,
        "timestamp": True,
        "keywords": False,

    }

    _attributes_to_types = {
        "symbols": "List[StockSymbol]",
        "title": "str",
        "url": "str",
        "source": "str",
        "summary": "str",
        "image": "str",
        "timestamp": "str",
        "keywords": "List[str]",

    }

    def __init__(self):
        self.symbols: List[StockSymbol]
        self.title: str
        self.url: str
        self.source: str
        self.summary: str
        self.image: str
        self.timestamp: str
        self.keywords: List[str]


# noinspection SpellCheckingInspection
class Earning(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "symbol": "str",
        "e___psrep_ortdate": "str",
        "e___psrep_ort_datestr": "str",
        "fiscal_period": "str",
        "fiscal_en_ddate": "str",
        "actual___eps": "float",
        "consensus___eps": "float",
        "estimated___eps": "float",
        "announce_time": "str",
        "number_o_festimates": "float",
        "e___pssurpr_isedollar": "float",
        "year_ago": "float",
        "year_ag_ochan_gepercent": "float",
        "estimated_chang_epercent": "float",

    }

    def __init__(self):
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


# noinspection SpellCheckingInspection
class Financial(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "symbol": "str",
        "report_date": "str",
        "report_dat_estr": "str",
        "gross_profit": "float",
        "cost_o_frevenue": "float",
        "operating_revenue": "float",
        "total_revenue": "float",
        "operating_income": "float",
        "net_income": "float",
        "research_an_ddevelopment": "float",
        "operating_expense": "float",
        "current_assets": "float",
        "total_assets": "float",
        "total_liabilities": "float",
        "current_cash": "float",
        "current_debt": "float",
        "total_cash": "float",
        "total_debt": "float",
        "shareholder_equity": "float",
        "cash_change": "float",
        "cash_flow": "float",
        "operating_gain_slosses": "float",

    }

    def __init__(self):
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


# noinspection SpellCheckingInspection
class Exchange(Definition):
    _swagger_name_to_python = {
        "id": "i_d_of_the_exchange",
        "type": "type",
        "market": "market",
        "mic": "mic",
        "name": "name",
        "tape": "tape",

    }

    _attribute_is_primitive = {
        "i_d_of_the_exchange": True,
        "type": True,
        "market": True,
        "mic": True,
        "name": True,
        "tape": True,

    }

    _attributes_to_types = {
        "i_d_of_the_exchange": "float",
        "type": "str",
        "market": "str",
        "mic": "str",
        "name": "str",
        "tape": "str",

    }

    def __init__(self):
        self.i_d_of_the_exchange: float
        self.type: str
        self.market: str
        self.mic: str
        self.name: str
        self.tape: str


# noinspection SpellCheckingInspection
class Error(Definition):
    _swagger_name_to_python = {
        "code": "code",
        "message": "message",
        "fields": "fields",

    }

    _attribute_is_primitive = {
        "code": True,
        "message": True,
        "fields": True,

    }

    _attributes_to_types = {
        "code": "int",
        "message": "str",
        "fields": "str",

    }

    def __init__(self):
        self.code: int
        self.message: str
        self.fields: str


# noinspection SpellCheckingInspection
class NotFound(Definition):
    _swagger_name_to_python = {
        "message": "message",

    }

    _attribute_is_primitive = {
        "message": True,

    }

    _attributes_to_types = {
        "message": "str",

    }

    def __init__(self):
        self.message: str


# noinspection SpellCheckingInspection
class Conflict(Definition):
    _swagger_name_to_python = {
        "message": "message",

    }

    _attribute_is_primitive = {
        "message": True,

    }

    _attributes_to_types = {
        "message": "str",

    }

    def __init__(self):
        self.message: str


# noinspection SpellCheckingInspection
class Unauthorized(Definition):
    _swagger_name_to_python = {
        "message": "message",

    }

    _attribute_is_primitive = {
        "message": True,

    }

    _attributes_to_types = {
        "message": "str",

    }

    def __init__(self):
        self.message: str


# noinspection SpellCheckingInspection
class MarketStatus(Definition):
    _swagger_name_to_python = {
        "market": "market",
        "serverTime": "server_time",
        "exchanges": "exchanges",
        "currencies": "currencies",

    }

    _attribute_is_primitive = {
        "market": True,
        "server_time": True,
        "exchanges": True,
        "currencies": True,

    }

    _attributes_to_types = {
        "market": "str",
        "server_time": "str",
        "exchanges": "Dict[str, str]",
        "currencies": "Dict[str, str]",

    }

    def __init__(self):
        self.market: str
        self.server_time: str
        self.exchanges: Dict[str, str]
        self.currencies: Dict[str, str]


# noinspection SpellCheckingInspection
class MarketHoliday(Definition):
    _swagger_name_to_python = {
        "exchange": "exchange",
        "name": "name",
        "status": "status",
        "date": "date",
        "open": "open",
        "close": "close",

    }

    _attribute_is_primitive = {
        "exchange": True,
        "name": True,
        "status": True,
        "date": True,
        "open": True,
        "close": True,

    }

    _attributes_to_types = {
        "exchange": "str",
        "name": "str",
        "status": "str",
        "date": "str",
        "open": "str",
        "close": "str",

    }

    def __init__(self):
        self.exchange: str
        self.name: str
        self.status: str
        self.date: str
        self.open: str
        self.close: str


# noinspection SpellCheckingInspection
class AnalystRatings(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "symbol": "str",
        "analysts": "float",
        "change": "float",
        "strong_buy": "RatingSection",
        "buy": "RatingSection",
        "hold": "RatingSection",
        "sell": "RatingSection",
        "strong_sell": "RatingSection",
        "updated": "str",

    }

    def __init__(self):
        self.symbol: str
        self.analysts: float
        self.change: float
        self.strong_buy: RatingSection
        self.buy: RatingSection
        self.hold: RatingSection
        self.sell: RatingSection
        self.strong_sell: RatingSection
        self.updated: str


# noinspection SpellCheckingInspection
class RatingSection(Definition):
    _swagger_name_to_python = {
        "current": "current",
        "month1": "month1",
        "month2": "month2",
        "month3": "month3",
        "month4": "month4",
        "month5": "month5",

    }

    _attribute_is_primitive = {
        "current": True,
        "month1": True,
        "month2": True,
        "month3": True,
        "month4": True,
        "month5": True,

    }

    _attributes_to_types = {
        "current": "float",
        "month1": "float",
        "month2": "float",
        "month3": "float",
        "month4": "float",
        "month5": "float",

    }

    def __init__(self):
        self.current: float
        self.month1: float
        self.month2: float
        self.month3: float
        self.month4: float
        self.month5: float


# noinspection SpellCheckingInspection
class CryptoTick(Definition):
    _swagger_name_to_python = {
        "price": "price",
        "size": "size",
        "exchange": "exchange",
        "conditions": "conditions",
        "timestamp": "timestamp",

    }

    _attribute_is_primitive = {
        "price": True,
        "size": True,
        "exchange": True,
        "conditions": False,
        "timestamp": True,

    }

    _attributes_to_types = {
        "price": "int",
        "size": "int",
        "exchange": "int",
        "conditions": "List[int]",
        "timestamp": "int",

    }

    def __init__(self):
        self.price: int
        self.size: int
        self.exchange: int
        self.conditions: List[int]
        self.timestamp: int


# noinspection SpellCheckingInspection
class CryptoTickJson(Definition):
    _swagger_name_to_python = {
        "p": "trade_price",
        "s": "size_of_the_trade",
        "x": "exchange_the_trade_occured_on",
        "c": "c",
        "t": "timestamp_of_this_trade",

    }

    _attribute_is_primitive = {
        "trade_price": True,
        "size_of_the_trade": True,
        "exchange_the_trade_occured_on": True,
        "c": False,
        "timestamp_of_this_trade": True,

    }

    _attributes_to_types = {
        "trade_price": "int",
        "size_of_the_trade": "int",
        "exchange_the_trade_occured_on": "int",
        "c": "List[int]",
        "timestamp_of_this_trade": "int",

    }

    def __init__(self):
        self.trade_price: int
        self.size_of_the_trade: int
        self.exchange_the_trade_occured_on: int
        self.c: List[int]
        self.timestamp_of_this_trade: int


# noinspection SpellCheckingInspection
class CryptoExchange(Definition):
    _swagger_name_to_python = {
        "id": "i_d_of_the_exchange",
        "type": "type",
        "market": "market",
        "name": "name",
        "url": "url",

    }

    _attribute_is_primitive = {
        "i_d_of_the_exchange": True,
        "type": True,
        "market": True,
        "name": True,
        "url": True,

    }

    _attributes_to_types = {
        "i_d_of_the_exchange": "float",
        "type": "str",
        "market": "str",
        "name": "str",
        "url": "str",

    }

    def __init__(self):
        self.i_d_of_the_exchange: float
        self.type: str
        self.market: str
        self.name: str
        self.url: str


# noinspection SpellCheckingInspection
class CryptoSnapshotTicker(Definition):
    _swagger_name_to_python = {
        "ticker": "ticker",
        "day": "day",
        "lastTrade": "last_trade",
        "min": "min",
        "prevDay": "prev_day",
        "todaysChange": "todays_change",
        "todaysChangePerc": "todays_chang_eperc",
        "updated": "updated",

    }

    _attribute_is_primitive = {
        "ticker": True,
        "day": False,
        "last_trade": False,
        "min": False,
        "prev_day": False,
        "todays_change": True,
        "todays_chang_eperc": True,
        "updated": True,

    }

    _attributes_to_types = {
        "ticker": "str",
        "day": "CryptoSnapshotAgg",
        "last_trade": "CryptoTickJson",
        "min": "CryptoSnapshotAgg",
        "prev_day": "CryptoSnapshotAgg",
        "todays_change": "int",
        "todays_chang_eperc": "int",
        "updated": "int",

    }

    def __init__(self):
        self.ticker: str
        self.day: CryptoSnapshotAgg
        self.last_trade: CryptoTickJson
        self.min: CryptoSnapshotAgg
        self.prev_day: CryptoSnapshotAgg
        self.todays_change: int
        self.todays_chang_eperc: int
        self.updated: int


# noinspection SpellCheckingInspection
class CryptoSnapshotBookItem(Definition):
    _swagger_name_to_python = {
        "p": "price_of_this_book_level",
        "x": "exchange_to_size_of_this_price_level",

    }

    _attribute_is_primitive = {
        "price_of_this_book_level": True,
        "exchange_to_size_of_this_price_level": True,

    }

    _attributes_to_types = {
        "price_of_this_book_level": "int",
        "exchange_to_size_of_this_price_level": "Dict[str, str]",

    }

    def __init__(self):
        self.price_of_this_book_level: int
        self.exchange_to_size_of_this_price_level: Dict[str, str]


# noinspection SpellCheckingInspection
class CryptoSnapshotTickerBook(Definition):
    _swagger_name_to_python = {
        "ticker": "ticker",
        "bids": "bids",
        "asks": "asks",
        "bidCount": "bid_count",
        "askCount": "ask_count",
        "spread": "spread",
        "updated": "updated",

    }

    _attribute_is_primitive = {
        "ticker": True,
        "bids": False,
        "asks": False,
        "bid_count": True,
        "ask_count": True,
        "spread": True,
        "updated": True,

    }

    _attributes_to_types = {
        "ticker": "str",
        "bids": "List[CryptoSnapshotBookItem]",
        "asks": "List[CryptoSnapshotBookItem]",
        "bid_count": "int",
        "ask_count": "int",
        "spread": "int",
        "updated": "int",

    }

    def __init__(self):
        self.ticker: str
        self.bids: List[CryptoSnapshotBookItem]
        self.asks: List[CryptoSnapshotBookItem]
        self.bid_count: int
        self.ask_count: int
        self.spread: int
        self.updated: int


# noinspection SpellCheckingInspection
class CryptoSnapshotAgg(Definition):
    _swagger_name_to_python = {
        "c": "close_price",
        "h": "high_price",
        "l": "low_price",
        "o": "open_price",
        "v": "volume",

    }

    _attribute_is_primitive = {
        "close_price": True,
        "high_price": True,
        "low_price": True,
        "open_price": True,
        "volume": True,

    }

    _attributes_to_types = {
        "close_price": "int",
        "high_price": "int",
        "low_price": "int",
        "open_price": "int",
        "volume": "int",

    }

    def __init__(self):
        self.close_price: int
        self.high_price: int
        self.low_price: int
        self.open_price: int
        self.volume: int


# noinspection SpellCheckingInspection
class Forex(Definition):
    _swagger_name_to_python = {
        "a": "ask_price",
        "b": "bid_price",
        "t": "timestamp_of_this_trade",

    }

    _attribute_is_primitive = {
        "ask_price": True,
        "bid_price": True,
        "timestamp_of_this_trade": True,

    }

    _attributes_to_types = {
        "ask_price": "int",
        "bid_price": "int",
        "timestamp_of_this_trade": "int",

    }

    def __init__(self):
        self.ask_price: int
        self.bid_price: int
        self.timestamp_of_this_trade: int


# noinspection SpellCheckingInspection
class LastForexTrade(Definition):
    _swagger_name_to_python = {
        "price": "price",
        "exchange": "exchange",
        "timestamp": "timestamp",

    }

    _attribute_is_primitive = {
        "price": True,
        "exchange": True,
        "timestamp": True,

    }

    _attributes_to_types = {
        "price": "int",
        "exchange": "int",
        "timestamp": "int",

    }

    def __init__(self):
        self.price: int
        self.exchange: int
        self.timestamp: int


# noinspection SpellCheckingInspection
class LastForexQuote(Definition):
    _swagger_name_to_python = {
        "ask": "ask",
        "bid": "bid",
        "exchange": "exchange",
        "timestamp": "timestamp",

    }

    _attribute_is_primitive = {
        "ask": True,
        "bid": True,
        "exchange": True,
        "timestamp": True,

    }

    _attributes_to_types = {
        "ask": "int",
        "bid": "int",
        "exchange": "int",
        "timestamp": "int",

    }

    def __init__(self):
        self.ask: int
        self.bid: int
        self.exchange: int
        self.timestamp: int


# noinspection SpellCheckingInspection
class ForexAggregate(Definition):
    _swagger_name_to_python = {
        "o": "open_price",
        "c": "close_price",
        "l": "low_price",
        "h": "high_price",
        "v": "volume_of_all_trades",
        "t": "timestamp_of_this_aggregation",

    }

    _attribute_is_primitive = {
        "open_price": True,
        "close_price": True,
        "low_price": True,
        "high_price": True,
        "volume_of_all_trades": True,
        "timestamp_of_this_aggregation": True,

    }

    _attributes_to_types = {
        "open_price": "int",
        "close_price": "int",
        "low_price": "int",
        "high_price": "int",
        "volume_of_all_trades": "int",
        "timestamp_of_this_aggregation": "int",

    }

    def __init__(self):
        self.open_price: int
        self.close_price: int
        self.low_price: int
        self.high_price: int
        self.volume_of_all_trades: int
        self.timestamp_of_this_aggregation: int


# noinspection SpellCheckingInspection
class ForexSnapshotTicker(Definition):
    _swagger_name_to_python = {
        "ticker": "ticker",
        "day": "day",
        "lastTrade": "last_trade",
        "min": "min",
        "prevDay": "prev_day",
        "todaysChange": "todays_change",
        "todaysChangePerc": "todays_chang_eperc",
        "updated": "updated",

    }

    _attribute_is_primitive = {
        "ticker": True,
        "day": False,
        "last_trade": False,
        "min": False,
        "prev_day": False,
        "todays_change": True,
        "todays_chang_eperc": True,
        "updated": True,

    }

    _attributes_to_types = {
        "ticker": "str",
        "day": "ForexSnapshotAgg",
        "last_trade": "Forex",
        "min": "ForexSnapshotAgg",
        "prev_day": "ForexSnapshotAgg",
        "todays_change": "int",
        "todays_chang_eperc": "int",
        "updated": "int",

    }

    def __init__(self):
        self.ticker: str
        self.day: ForexSnapshotAgg
        self.last_trade: Forex
        self.min: ForexSnapshotAgg
        self.prev_day: ForexSnapshotAgg
        self.todays_change: int
        self.todays_chang_eperc: int
        self.updated: int


# noinspection SpellCheckingInspection
class ForexSnapshotAgg(Definition):
    _swagger_name_to_python = {
        "c": "close_price",
        "h": "high_price",
        "l": "low_price",
        "o": "open_price",
        "v": "volume",

    }

    _attribute_is_primitive = {
        "close_price": True,
        "high_price": True,
        "low_price": True,
        "open_price": True,
        "volume": True,

    }

    _attributes_to_types = {
        "close_price": "int",
        "high_price": "int",
        "low_price": "int",
        "open_price": "int",
        "volume": "int",

    }

    def __init__(self):
        self.close_price: int
        self.high_price: int
        self.low_price: int
        self.open_price: int
        self.volume: int


# noinspection SpellCheckingInspection
class Ticker(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "ticker": "StockSymbol",
        "name": "str",
        "market": "str",
        "locale": "str",
        "currency": "str",
        "active": "bool",
        "primary_exch": "str",
        "url": "str",
        "updated": "str",
        "attrs": "Dict[str, str]",
        "codes": "Dict[str, str]",

    }

    def __init__(self):
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


# noinspection SpellCheckingInspection
class Split(Definition):
    _swagger_name_to_python = {
        "ticker": "ticker",
        "exDate": "ex_date",
        "paymentDate": "payment_date",
        "recordDate": "record_date",
        "declaredDate": "declared_date",
        "ratio": "ratio",
        "tofactor": "tofactor",
        "forfactor": "forfactor",

    }

    _attribute_is_primitive = {
        "ticker": False,
        "ex_date": True,
        "payment_date": True,
        "record_date": True,
        "declared_date": True,
        "ratio": True,
        "tofactor": True,
        "forfactor": True,

    }

    _attributes_to_types = {
        "ticker": "TickerSymbol",
        "ex_date": "str",
        "payment_date": "str",
        "record_date": "str",
        "declared_date": "str",
        "ratio": "float",
        "tofactor": "float",
        "forfactor": "float",

    }

    def __init__(self):
        self.ticker: TickerSymbol
        self.ex_date: str
        self.payment_date: str
        self.record_date: str
        self.declared_date: str
        self.ratio: float
        self.tofactor: float
        self.forfactor: float


# noinspection SpellCheckingInspection
class Financials(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "ticker": "TickerSymbol",
        "period": "str",
        "calendar_date": "str",
        "report_period": "str",
        "updated": "str",
        "accumulated_othe_rcomprehensi_veincome": "int",
        "assets": "int",
        "assets_average": "int",
        "assets_current": "int",
        "asset_turnover": "int",
        "assets_no_ncurrent": "int",
        "book_valu_ep_ershare": "int",
        "capital_expenditure": "int",
        "cash_an_dequivalents": "int",
        "cash_an_dequivalen___tsusd": "int",
        "cost_o_frevenue": "int",
        "consolidated_income": "int",
        "current_ratio": "int",
        "debt_t_oequi_tyratio": "int",
        "debt": "int",
        "debt_current": "int",
        "debt_no_ncurrent": "int",
        "debt___usd": "int",
        "deferred_revenue": "int",
        "depreciation_amortizatio_na_ndaccretion": "int",
        "deposits": "int",
        "dividend_yield": "int",
        "dividends_pe_rbas_iccom_monshare": "int",
        "earning_befor_eintere_sttaxes": "int",
        "earnings_befor_eintere_stta_xesdeprecia_tionamortization": "int",
        "e______bitdamargin": "int",
        "earnings_befor_eintere_stta_xesdeprecia_tionamortiz___ationusd": "int",
        "earning_befor_eintere_stta___xesusd": "int",
        "earnings_befor_etax": "int",
        "earnings_pe_rbas_icshare": "int",
        "earnings_pe_rdilut_edshare": "int",
        "earnings_pe_rbas_icsh___areusd": "int",
        "shareholders_equity": "int",
        "average_equity": "int",
        "shareholders_equit___yusd": "int",
        "enterprise_value": "int",
        "enterprise_valu_eov____erebit": "int",
        "enterprise_valu_eov______erebitda": "int",
        "free_cas_hflow": "int",
        "free_cas_hfl_ow_pershare": "int",
        "foreign_currenc____yusdexc_hangerate": "int",
        "gross_profit": "int",
        "gross_margin": "int",
        "goodwill_an_dintangib_leassets": "int",
        "interest_expense": "int",
        "invested_capital": "int",
        "invested_capita_laverage": "int",
        "inventory": "int",
        "investments": "int",
        "investments_current": "int",
        "investments_no_ncurrent": "int",
        "total_liabilities": "int",
        "current_liabilities": "int",
        "liabilities_no_ncurrent": "int",
        "market_capitalization": "int",
        "net_cas_hflow": "int",
        "net_cas_hfl_owbusin_essacquisit_ionsdisposals": "int",
        "issuance_equit_yshares": "int",
        "issuance_deb_tsecurities": "int",
        "payment_dividend_soth_erc_ashdistributions": "int",
        "net_cas_hfl_owf_romfinancing": "int",
        "net_cas_hfl_owf_rominvesting": "int",
        "net_cas_hfl_owinvestm_entacquisit_ionsdisposals": "int",
        "net_cas_hfl_owf_romoperations": "int",
        "effect_o_fexchan_ger_atecha_n_gesoncash": "int",
        "net_income": "int",
        "net_incom_ecomm_onstock": "int",
        "net_incom_ecomm_onst___ockusd": "int",
        "net_los_sinco_mef_romdisconti_nuedoperations": "int",
        "net_incom_e_to_noncontrol_linginterests": "int",
        "profit_margin": "int",
        "operating_expenses": "int",
        "operating_income": "int",
        "trade_an_dn_ontr_adepayables": "int",
        "payout_ratio": "int",
        "price_t_obo_okvalue": "int",
        "price_earnings": "int",
        "price_t_oearnin_gsratio": "int",
        "property_plan_tequipme_ntnet": "int",
        "preferred_dividend_sinco_mestatem_entimpact": "int",
        "share_pric_eadjust_edclose": "int",
        "price_sales": "int",
        "price_t_osal_esratio": "int",
        "trade_an_dn_ontr_adereceivables": "int",
        "accumulated_retaine_dearnin_gsdeficit": "int",
        "revenues": "int",
        "revenues___usd": "int",
        "research_an_ddevelopme_ntexpense": "int",
        "return_o_navera_geassets": "int",
        "return_o_navera_geequity": "int",
        "return_o_ninvest_edcapital": "int",
        "return_o_nsales": "int",
        "share_base_dcompensation": "int",
        "selling_genera_la_ndadministrat_iveexpense": "int",
        "share_factor": "int",
        "shares": "int",
        "weighted_averag_eshares": "int",
        "weighted_averag_eshar_esdiluted": "int",
        "sales_pe_rshare": "int",
        "tangible_asse_tvalue": "int",
        "tax_assets": "int",
        "income_ta_xexpense": "int",
        "tax_liabilities": "int",
        "tangible_asset_sbo_okva_lu_epershare": "int",
        "working_capital": "int",

    }

    def __init__(self):
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


# noinspection SpellCheckingInspection
class Trade(Definition):
    _swagger_name_to_python = {
        "c1": "condition_1_of_this_trade",
        "c2": "condition_2_of_this_trade",
        "c3": "condition_3_of_this_trade",
        "c4": "condition_4_of_this_trade",
        "e": "the_exchange_this_trade_happened_on",
        "p": "price_of_the_trade",
        "s": "size_of_the_trade",
        "t": "timestamp_of_this_trade",

    }

    _attribute_is_primitive = {
        "condition_1_of_this_trade": True,
        "condition_2_of_this_trade": True,
        "condition_3_of_this_trade": True,
        "condition_4_of_this_trade": True,
        "the_exchange_this_trade_happened_on": True,
        "price_of_the_trade": True,
        "size_of_the_trade": True,
        "timestamp_of_this_trade": True,

    }

    _attributes_to_types = {
        "condition_1_of_this_trade": "int",
        "condition_2_of_this_trade": "int",
        "condition_3_of_this_trade": "int",
        "condition_4_of_this_trade": "int",
        "the_exchange_this_trade_happened_on": "str",
        "price_of_the_trade": "int",
        "size_of_the_trade": "int",
        "timestamp_of_this_trade": "int",

    }

    def __init__(self):
        self.condition_1_of_this_trade: int
        self.condition_2_of_this_trade: int
        self.condition_3_of_this_trade: int
        self.condition_4_of_this_trade: int
        self.the_exchange_this_trade_happened_on: str
        self.price_of_the_trade: int
        self.size_of_the_trade: int
        self.timestamp_of_this_trade: int


# noinspection SpellCheckingInspection
class StocksSnapshotTicker(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "ticker": "str",
        "day": "StocksSnapshotAgg",
        "last_trade": "Trade",
        "last_quote": "StocksSnapshotQuote",
        "min": "StocksSnapshotAgg",
        "prev_day": "StocksSnapshotAgg",
        "todays_change": "int",
        "todays_chang_eperc": "int",
        "updated": "int",

    }

    def __init__(self):
        self.ticker: str
        self.day: StocksSnapshotAgg
        self.last_trade: Trade
        self.last_quote: StocksSnapshotQuote
        self.min: StocksSnapshotAgg
        self.prev_day: StocksSnapshotAgg
        self.todays_change: int
        self.todays_chang_eperc: int
        self.updated: int


# noinspection SpellCheckingInspection
class StocksSnapshotBookItem(Definition):
    _swagger_name_to_python = {
        "p": "price_of_this_book_level",
        "x": "exchange_to_size_of_this_price_level",

    }

    _attribute_is_primitive = {
        "price_of_this_book_level": True,
        "exchange_to_size_of_this_price_level": True,

    }

    _attributes_to_types = {
        "price_of_this_book_level": "int",
        "exchange_to_size_of_this_price_level": "Dict[str, str]",

    }

    def __init__(self):
        self.price_of_this_book_level: int
        self.exchange_to_size_of_this_price_level: Dict[str, str]


# noinspection SpellCheckingInspection
class StocksSnapshotTickerBook(Definition):
    _swagger_name_to_python = {
        "ticker": "ticker",
        "bids": "bids",
        "asks": "asks",
        "bidCount": "bid_count",
        "askCount": "ask_count",
        "spread": "spread",
        "updated": "updated",

    }

    _attribute_is_primitive = {
        "ticker": True,
        "bids": False,
        "asks": False,
        "bid_count": True,
        "ask_count": True,
        "spread": True,
        "updated": True,

    }

    _attributes_to_types = {
        "ticker": "str",
        "bids": "List[StocksSnapshotBookItem]",
        "asks": "List[StocksSnapshotBookItem]",
        "bid_count": "int",
        "ask_count": "int",
        "spread": "int",
        "updated": "int",

    }

    def __init__(self):
        self.ticker: str
        self.bids: List[StocksSnapshotBookItem]
        self.asks: List[StocksSnapshotBookItem]
        self.bid_count: int
        self.ask_count: int
        self.spread: int
        self.updated: int


# noinspection SpellCheckingInspection
class StocksV2Trade(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "ticker_of_the_object": "str",
        "nanosecond_accuracy_s__ip_unix_timestamp": "int",
        "nanosecond_accuracy_participant_exchange_unix_timestamp": "int",
        "nanosecond_accuracy_t__rf": "int",
        "sequence_number": "int",
        "trade_i_d": "str",
        "exchange_i_d": "int",
        "size_volume_of_the_trade": "int",
        "c": "List[int]",
        "price_of_the_trade": "int",
        "tape_where_trade_occured": "int",

    }

    def __init__(self):
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


# noinspection SpellCheckingInspection
class StocksV2NBBO(Definition):
    _swagger_name_to_python = {
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

    _attribute_is_primitive = {
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

    _attributes_to_types = {
        "ticker_of_the_object": "str",
        "nanosecond_accuracy_s__ip_unix_timestamp": "int",
        "nanosecond_accuracy_participant_exchange_unix_timestamp": "int",
        "nanosecond_accuracy_t__rf": "int",
        "sequence_number": "int",
        "c": "List[int]",
        "i": "List[int]",
        "b__id_price": "int",
        "b__id_exchange__id": "int",
        "b__id_size": "int",
        "a__sk_price": "int",
        "a__sk_exchange__id": "int",
        "a__sk_size": "int",
        "tape_where_trade_occured": "int",

    }

    def __init__(self):
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


# noinspection SpellCheckingInspection
class StocksSnapshotAgg(Definition):
    _swagger_name_to_python = {
        "c": "close_price",
        "h": "high_price",
        "l": "low_price",
        "o": "open_price",
        "v": "volume",

    }

    _attribute_is_primitive = {
        "close_price": True,
        "high_price": True,
        "low_price": True,
        "open_price": True,
        "volume": True,

    }

    _attributes_to_types = {
        "close_price": "int",
        "high_price": "int",
        "low_price": "int",
        "open_price": "int",
        "volume": "int",

    }

    def __init__(self):
        self.close_price: int
        self.high_price: int
        self.low_price: int
        self.open_price: int
        self.volume: int


# noinspection SpellCheckingInspection
class StocksSnapshotQuote(Definition):
    _swagger_name_to_python = {
        "p": "bid_price",
        "s": "bid_size_in_lots",
        "P": "ask_price",
        "S": "ask_size_in_lots",
        "t": "last_updated_timestamp",

    }

    _attribute_is_primitive = {
        "bid_price": True,
        "bid_size_in_lots": True,
        "ask_price": True,
        "ask_size_in_lots": True,
        "last_updated_timestamp": True,

    }

    _attributes_to_types = {
        "bid_price": "int",
        "bid_size_in_lots": "int",
        "ask_price": "int",
        "ask_size_in_lots": "int",
        "last_updated_timestamp": "int",

    }

    def __init__(self):
        self.bid_price: int
        self.bid_size_in_lots: int
        self.ask_price: int
        self.ask_size_in_lots: int
        self.last_updated_timestamp: int


# noinspection SpellCheckingInspection
class Aggv2(Definition):
    _swagger_name_to_python = {
        "T": "ticker_symbol",
        "v": "volume",
        "o": "open",
        "c": "close",
        "h": "high",
        "l": "low",
        "t": "unix_msec_timestamp",
        "n": "number_of_items_in_aggregate_window",

    }

    _attribute_is_primitive = {
        "ticker_symbol": True,
        "volume": True,
        "open": True,
        "close": True,
        "high": True,
        "low": True,
        "unix_msec_timestamp": True,
        "number_of_items_in_aggregate_window": True,

    }

    _attributes_to_types = {
        "ticker_symbol": "str",
        "volume": "int",
        "open": "int",
        "close": "int",
        "high": "int",
        "low": "int",
        "unix_msec_timestamp": "float",
        "number_of_items_in_aggregate_window": "float",

    }

    def __init__(self):
        self.ticker_symbol: str
        self.volume: int
        self.open: int
        self.close: int
        self.high: int
        self.low: int
        self.unix_msec_timestamp: float
        self.number_of_items_in_aggregate_window: float


# noinspection SpellCheckingInspection
class AggResponse(Definition):
    _swagger_name_to_python = {
        "ticker": "ticker",
        "status": "status",
        "adjusted": "adjusted",
        "queryCount": "query_count",
        "resultsCount": "results_count",
        "results": "results",

    }

    _attribute_is_primitive = {
        "ticker": True,
        "status": True,
        "adjusted": True,
        "query_count": True,
        "results_count": True,
        "results": False,

    }

    _attributes_to_types = {
        "ticker": "str",
        "status": "str",
        "adjusted": "bool",
        "query_count": "float",
        "results_count": "float",
        "results": "List[Aggv2]",

    }

    def __init__(self):
        self.ticker: str
        self.status: str
        self.adjusted: bool
        self.query_count: float
        self.results_count: float
        self.results: List[Aggv2]


# noinspection SpellCheckingInspection
class ReferenceTickersApiResponse(Definition):
    _swagger_name_to_python = {
        "symbol": "symbol",

    }

    _attribute_is_primitive = {
        "symbol": False,

    }

    _attributes_to_types = {
        "symbol": "List[Symbol]",

    }

    def __init__(self):
        self.symbol: List[Symbol]


# noinspection SpellCheckingInspection
class ReferenceTickerTypesApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "results": "results",

    }

    _attribute_is_primitive = {
        "status": True,
        "results": True,

    }

    _attributes_to_types = {
        "status": "str",
        "results": "Dict[str, str]",

    }

    def __init__(self):
        self.status: str
        self.results: Dict[str, str]


# noinspection SpellCheckingInspection
class ReferenceTickerDetailsApiResponse(Definition):
    _swagger_name_to_python = {
        "company": "company",

    }

    _attribute_is_primitive = {
        "company": False,

    }

    _attributes_to_types = {
        "company": "Company",

    }

    def __init__(self):
        self.company: Company


# noinspection SpellCheckingInspection
class ReferenceTickerNewsApiResponse(Definition):
    _swagger_name_to_python = {
        "news": "news",

    }

    _attribute_is_primitive = {
        "news": False,

    }

    _attributes_to_types = {
        "news": "List[News]",

    }

    def __init__(self):
        self.news: List[News]


# noinspection SpellCheckingInspection
class ReferenceMarketsApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "results": "results",

    }

    _attribute_is_primitive = {
        "status": True,
        "results": False,

    }

    _attributes_to_types = {
        "status": "str",
        "results": "List[Dict[str, str]]",

    }

    def __init__(self):
        self.status: str
        self.results: List[Dict[str, str]]


# noinspection SpellCheckingInspection
class ReferenceLocalesApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "results": "results",

    }

    _attribute_is_primitive = {
        "status": True,
        "results": False,

    }

    _attributes_to_types = {
        "status": "str",
        "results": "List[Dict[str, str]]",

    }

    def __init__(self):
        self.status: str
        self.results: List[Dict[str, str]]


# noinspection SpellCheckingInspection
class ReferenceStockSplitsApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "count": "count",
        "results": "results",

    }

    _attribute_is_primitive = {
        "status": True,
        "count": True,
        "results": False,

    }

    _attributes_to_types = {
        "status": "str",
        "count": "float",
        "results": "List[Split]",

    }

    def __init__(self):
        self.status: str
        self.count: float
        self.results: List[Split]


# noinspection SpellCheckingInspection
class ReferenceStockDividendsApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "count": "count",
        "results": "results",

    }

    _attribute_is_primitive = {
        "status": True,
        "count": True,
        "results": False,

    }

    _attributes_to_types = {
        "status": "str",
        "count": "float",
        "results": "List[Dividend]",

    }

    def __init__(self):
        self.status: str
        self.count: float
        self.results: List[Dividend]


# noinspection SpellCheckingInspection
class ReferenceStockFinancialsApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "count": "count",
        "results": "results",

    }

    _attribute_is_primitive = {
        "status": True,
        "count": True,
        "results": False,

    }

    _attributes_to_types = {
        "status": "str",
        "count": "float",
        "results": "List[Financials]",

    }

    def __init__(self):
        self.status: str
        self.count: float
        self.results: List[Financials]


# noinspection SpellCheckingInspection
class ReferenceMarketStatusApiResponse(Definition):
    _swagger_name_to_python = {
        "marketstatus": "marketstatus",

    }

    _attribute_is_primitive = {
        "marketstatus": False,

    }

    _attributes_to_types = {
        "marketstatus": "MarketStatus",

    }

    def __init__(self):
        self.marketstatus: MarketStatus


# noinspection SpellCheckingInspection
class ReferenceMarketHolidaysApiResponse(Definition):
    _swagger_name_to_python = {
        "marketholiday": "marketholiday",

    }

    _attribute_is_primitive = {
        "marketholiday": False,

    }

    _attributes_to_types = {
        "marketholiday": "List[MarketHoliday]",

    }

    def __init__(self):
        self.marketholiday: List[MarketHoliday]


# noinspection SpellCheckingInspection
class StocksEquitiesExchangesApiResponse(Definition):
    _swagger_name_to_python = {
        "exchange": "exchange",

    }

    _attribute_is_primitive = {
        "exchange": False,

    }

    _attributes_to_types = {
        "exchange": "List[Exchange]",

    }

    def __init__(self):
        self.exchange: List[Exchange]


# noinspection SpellCheckingInspection
class StocksEquitiesHistoricTradesApiResponse(Definition):
    _swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "symbol": "symbol",
        "ticks": "ticks",

    }

    _attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "symbol": True,
        "ticks": False,

    }

    _attributes_to_types = {
        "day": "str",
        "map": "Dict[str, str]",
        "ms_latency": "int",
        "status": "str",
        "symbol": "str",
        "ticks": "List[Trade]",

    }

    def __init__(self):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.symbol: str
        self.ticks: List[Trade]


# noinspection SpellCheckingInspection
class HistoricTradesV2ApiResponse(Definition):
    _swagger_name_to_python = {
        "results_count": "results_count",
        "db_latency": "db_latency",
        "success": "success",
        "ticker": "ticker",
        "results": "results",

    }

    _attribute_is_primitive = {
        "results_count": True,
        "db_latency": True,
        "success": True,
        "ticker": True,
        "results": False,

    }

    _attributes_to_types = {
        "results_count": "int",
        "db_latency": "int",
        "success": "bool",
        "ticker": "str",
        "results": "List[StocksV2Trade]",

    }

    def __init__(self):
        self.results_count: int
        self.db_latency: int
        self.success: bool
        self.ticker: str
        self.results: List[StocksV2Trade]


# noinspection SpellCheckingInspection
class StocksEquitiesHistoricQuotesApiResponse(Definition):
    _swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "symbol": "symbol",
        "ticks": "ticks",

    }

    _attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "symbol": True,
        "ticks": False,

    }

    _attributes_to_types = {
        "day": "str",
        "map": "Dict[str, str]",
        "ms_latency": "int",
        "status": "str",
        "symbol": "str",
        "ticks": "List[Quote]",

    }

    def __init__(self):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.symbol: str
        self.ticks: List[Quote]


# noinspection SpellCheckingInspection
class HistoricNBboQuotesV2ApiResponse(Definition):
    _swagger_name_to_python = {
        "results_count": "results_count",
        "db_latency": "db_latency",
        "success": "success",
        "ticker": "ticker",
        "results": "results",

    }

    _attribute_is_primitive = {
        "results_count": True,
        "db_latency": True,
        "success": True,
        "ticker": True,
        "results": False,

    }

    _attributes_to_types = {
        "results_count": "int",
        "db_latency": "int",
        "success": "bool",
        "ticker": "str",
        "results": "List[StocksV2NBBO]",

    }

    def __init__(self):
        self.results_count: int
        self.db_latency: int
        self.success: bool
        self.ticker: str
        self.results: List[StocksV2NBBO]


# noinspection SpellCheckingInspection
class StocksEquitiesLastTradeForASymbolApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",

    }

    _attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,

    }

    _attributes_to_types = {
        "status": "str",
        "symbol": "str",
        "last": "LastTrade",

    }

    def __init__(self):
        self.status: str
        self.symbol: str
        self.last: LastTrade


# noinspection SpellCheckingInspection
class StocksEquitiesLastQuoteForASymbolApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",

    }

    _attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,

    }

    _attributes_to_types = {
        "status": "str",
        "symbol": "str",
        "last": "LastQuote",

    }

    def __init__(self):
        self.status: str
        self.symbol: str
        self.last: LastQuote


# noinspection SpellCheckingInspection
class StocksEquitiesDailyOpenCloseApiResponse(Definition):
    _swagger_name_to_python = {
        "symbol": "symbol",
        "open": "open",
        "close": "close",
        "afterHours": "after_hours",

    }

    _attribute_is_primitive = {
        "symbol": True,
        "open": False,
        "close": False,
        "after_hours": False,

    }

    _attributes_to_types = {
        "symbol": "str",
        "open": "HistTrade",
        "close": "HistTrade",
        "after_hours": "HistTrade",

    }

    def __init__(self):
        self.symbol: str
        self.open: HistTrade
        self.close: HistTrade
        self.after_hours: HistTrade


# noinspection SpellCheckingInspection
class StocksEquitiesConditionMappingsApiResponse(Definition):
    _swagger_name_to_python = {
        "conditiontypemap": "conditiontypemap",

    }

    _attribute_is_primitive = {
        "conditiontypemap": False,

    }

    _attributes_to_types = {
        "conditiontypemap": "ConditionTypeMap",

    }

    def __init__(self):
        self.conditiontypemap: ConditionTypeMap


# noinspection SpellCheckingInspection
class StocksEquitiesSnapshotAllTickersApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",

    }

    _attribute_is_primitive = {
        "status": True,
        "tickers": False,

    }

    _attributes_to_types = {
        "status": "str",
        "tickers": "List[StocksSnapshotTicker]",

    }

    def __init__(self):
        self.status: str
        self.tickers: List[StocksSnapshotTicker]


# noinspection SpellCheckingInspection
class StocksEquitiesSnapshotSingleTickerApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "ticker": "ticker",

    }

    _attribute_is_primitive = {
        "status": True,
        "ticker": False,

    }

    _attributes_to_types = {
        "status": "str",
        "ticker": "StocksSnapshotTicker",

    }

    def __init__(self):
        self.status: str
        self.ticker: StocksSnapshotTicker


# noinspection SpellCheckingInspection
class StocksEquitiesSnapshotGainersLosersApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",

    }

    _attribute_is_primitive = {
        "status": True,
        "tickers": False,

    }

    _attributes_to_types = {
        "status": "str",
        "tickers": "List[StocksSnapshotTicker]",

    }

    def __init__(self):
        self.status: str
        self.tickers: List[StocksSnapshotTicker]


# noinspection SpellCheckingInspection
class StocksEquitiesPreviousCloseApiResponse(Definition):
    _swagger_name_to_python = {
        "aggresponse": "aggresponse",

    }

    _attribute_is_primitive = {
        "aggresponse": False,

    }

    _attributes_to_types = {
        "aggresponse": "AggResponse",

    }

    def __init__(self):
        self.aggresponse: AggResponse


# noinspection SpellCheckingInspection
class StocksEquitiesAggregatesApiResponse(Definition):
    _swagger_name_to_python = {
        "aggresponse": "aggresponse",

    }

    _attribute_is_primitive = {
        "aggresponse": False,

    }

    _attributes_to_types = {
        "aggresponse": "AggResponse",

    }

    def __init__(self):
        self.aggresponse: AggResponse


# noinspection SpellCheckingInspection
class StocksEquitiesGroupedDailyApiResponse(Definition):
    _swagger_name_to_python = {
        "aggresponse": "aggresponse",

    }

    _attribute_is_primitive = {
        "aggresponse": False,

    }

    _attributes_to_types = {
        "aggresponse": "AggResponse",

    }

    def __init__(self):
        self.aggresponse: AggResponse


# noinspection SpellCheckingInspection
class ForexCurrenciesHistoricForexTicksApiResponse(Definition):
    _swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "pair": "pair",
        "ticks": "ticks",

    }

    _attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "pair": True,
        "ticks": False,

    }

    _attributes_to_types = {
        "day": "str",
        "map": "Dict[str, str]",
        "ms_latency": "int",
        "status": "str",
        "pair": "str",
        "ticks": "List[Forex]",

    }

    def __init__(self):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.pair: str
        self.ticks: List[Forex]


# noinspection SpellCheckingInspection
class ForexCurrenciesRealTimeCurrencyConversionApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "from": "from_",
        "to": "to_currency_symbol",
        "initialAmount": "initial_amount",
        "converted": "converted",
        "lastTrade": "last_trade",
        "symbol": "symbol",

    }

    _attribute_is_primitive = {
        "status": True,
        "from_": True,
        "to_currency_symbol": True,
        "initial_amount": True,
        "converted": True,
        "last_trade": False,
        "symbol": True,

    }

    _attributes_to_types = {
        "status": "str",
        "from_": "str",
        "to_currency_symbol": "str",
        "initial_amount": "float",
        "converted": "float",
        "last_trade": "LastForexTrade",
        "symbol": "str",

    }

    def __init__(self):
        self.status: str
        self.from_: str
        self.to_currency_symbol: str
        self.initial_amount: float
        self.converted: float
        self.last_trade: LastForexTrade
        self.symbol: str


# noinspection SpellCheckingInspection
class ForexCurrenciesLastQuoteForACurrencyPairApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",

    }

    _attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,

    }

    _attributes_to_types = {
        "status": "str",
        "symbol": "str",
        "last": "LastForexQuote",

    }

    def __init__(self):
        self.status: str
        self.symbol: str
        self.last: LastForexQuote


# noinspection SpellCheckingInspection
class ForexCurrenciesSnapshotAllTickersApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",

    }

    _attribute_is_primitive = {
        "status": True,
        "tickers": False,

    }

    _attributes_to_types = {
        "status": "str",
        "tickers": "List[ForexSnapshotTicker]",

    }

    def __init__(self):
        self.status: str
        self.tickers: List[ForexSnapshotTicker]


# noinspection SpellCheckingInspection
class ForexCurrenciesSnapshotGainersLosersApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",

    }

    _attribute_is_primitive = {
        "status": True,
        "tickers": False,

    }

    _attributes_to_types = {
        "status": "str",
        "tickers": "List[ForexSnapshotTicker]",

    }

    def __init__(self):
        self.status: str
        self.tickers: List[ForexSnapshotTicker]


# noinspection SpellCheckingInspection
class CryptoCryptoExchangesApiResponse(Definition):
    _swagger_name_to_python = {
        "cryptoexchange": "cryptoexchange",

    }

    _attribute_is_primitive = {
        "cryptoexchange": False,

    }

    _attributes_to_types = {
        "cryptoexchange": "List[CryptoExchange]",

    }

    def __init__(self):
        self.cryptoexchange: List[CryptoExchange]


# noinspection SpellCheckingInspection
class CryptoLastTradeForACryptoPairApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "symbol": "symbol",
        "last": "last",
        "lastAverage": "last_average",

    }

    _attribute_is_primitive = {
        "status": True,
        "symbol": True,
        "last": False,
        "last_average": True,

    }

    _attributes_to_types = {
        "status": "str",
        "symbol": "str",
        "last": "CryptoTick",
        "last_average": "Dict[str, str]",

    }

    def __init__(self):
        self.status: str
        self.symbol: str
        self.last: CryptoTick
        self.last_average: Dict[str, str]


# noinspection SpellCheckingInspection
class CryptoDailyOpenCloseApiResponse(Definition):
    _swagger_name_to_python = {
        "symbol": "symbol",
        "isUTC": "is___utc",
        "day": "day",
        "open": "open",
        "close": "close",
        "openTrades": "open_trades",
        "closingTrades": "closing_trades",

    }

    _attribute_is_primitive = {
        "symbol": True,
        "is___utc": True,
        "day": True,
        "open": True,
        "close": True,
        "open_trades": False,
        "closing_trades": False,

    }

    _attributes_to_types = {
        "symbol": "str",
        "is___utc": "bool",
        "day": "str",
        "open": "int",
        "close": "int",
        "open_trades": "List[CryptoTickJson]",
        "closing_trades": "List[CryptoTickJson]",

    }

    def __init__(self):
        self.symbol: str
        self.is___utc: bool
        self.day: str
        self.open: int
        self.close: int
        self.open_trades: List[CryptoTickJson]
        self.closing_trades: List[CryptoTickJson]


# noinspection SpellCheckingInspection
class CryptoHistoricCryptoTradesApiResponse(Definition):
    _swagger_name_to_python = {
        "day": "day",
        "map": "map",
        "msLatency": "ms_latency",
        "status": "status",
        "symbol": "symbol",
        "ticks": "ticks",

    }

    _attribute_is_primitive = {
        "day": True,
        "map": True,
        "ms_latency": True,
        "status": True,
        "symbol": True,
        "ticks": False,

    }

    _attributes_to_types = {
        "day": "str",
        "map": "Dict[str, str]",
        "ms_latency": "int",
        "status": "str",
        "symbol": "str",
        "ticks": "List[CryptoTickJson]",

    }

    def __init__(self):
        self.day: str
        self.map: Dict[str, str]
        self.ms_latency: int
        self.status: str
        self.symbol: str
        self.ticks: List[CryptoTickJson]


# noinspection SpellCheckingInspection
class CryptoSnapshotAllTickersApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",

    }

    _attribute_is_primitive = {
        "status": True,
        "tickers": False,

    }

    _attributes_to_types = {
        "status": "str",
        "tickers": "List[CryptoSnapshotTicker]",

    }

    def __init__(self):
        self.status: str
        self.tickers: List[CryptoSnapshotTicker]


# noinspection SpellCheckingInspection
class CryptoSnapshotSingleTickerApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "ticker": "ticker",

    }

    _attribute_is_primitive = {
        "status": True,
        "ticker": False,

    }

    _attributes_to_types = {
        "status": "str",
        "ticker": "CryptoSnapshotTicker",

    }

    def __init__(self):
        self.status: str
        self.ticker: CryptoSnapshotTicker


# noinspection SpellCheckingInspection
class CryptoSnapshotSingleTickerFullBookApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "data": "data",

    }

    _attribute_is_primitive = {
        "status": True,
        "data": False,

    }

    _attributes_to_types = {
        "status": "str",
        "data": "CryptoSnapshotTickerBook",

    }

    def __init__(self):
        self.status: str
        self.data: CryptoSnapshotTickerBook


# noinspection SpellCheckingInspection
class CryptoSnapshotGainersLosersApiResponse(Definition):
    _swagger_name_to_python = {
        "status": "status",
        "tickers": "tickers",

    }

    _attribute_is_primitive = {
        "status": True,
        "tickers": False,

    }

    _attributes_to_types = {
        "status": "str",
        "tickers": "List[CryptoSnapshotTicker]",

    }

    def __init__(self):
        self.status: str
        self.tickers: List[CryptoSnapshotTicker]


StockSymbol = str
ConditionTypeMap = Dict[str, str]
SymbolTypeMap = Dict[str, str]
TickerSymbol = str
