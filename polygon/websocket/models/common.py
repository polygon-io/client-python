from enum import Enum


class Feed(Enum):
    Delayed = "delayed.polygon.io"
    RealTime = "socket.polygon.io"
    Nasdaq = "nasdaqfeed.polygon.io"
    PolyFeed = "polyfeed.polygon.io"
    PolyFeedPlus = "polyfeedplus.polygon.io"


class Market(Enum):
    Stocks = "stocks"
    Options = "options"
    Forex = "forex"
    Crypto = "crypto"


class EventType(Enum):
    EquityAgg = "A"
    EquityAggMin = "AM"
    CryptoAgg = "CA"
    ForexAgg = "XA"
    EquityTrade = "T"
    CryptoTrade = "XT"
    EquityQuote = "Q"
    ForexQuote = "C"
    CryptoQuote = "XQ"
    Imbalances = "NOI"
    LimitUpLimitDown = "LULD"
    CryptoL2 = "XL2"
