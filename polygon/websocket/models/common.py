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
    A = "A"
    AM = "AM"
    CA = "CA"
    XA = "XA"
    T = "T"
    XT = "XT"
    Q = "Q"
    C = "C"
    XQ = "XQ"
    NOI = "NOI"
    LULD = "LULD"
    XL2 = "XL2"
