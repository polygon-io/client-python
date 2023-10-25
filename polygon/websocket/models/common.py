from enum import Enum


class Feed(Enum):
    Delayed = "delayed.polygon.io"
    RealTime = "socket.polygon.io"
    Nasdaq = "nasdaqfeed.polygon.io"
    PolyFeed = "polyfeed.polygon.io"
    PolyFeedPlus = "polyfeedplus.polygon.io"
    StarterFeed = "starterfeed.polygon.io"
    Launchpad = "launchpad.polygon.io"
    Business = "business.polygon.io"
    EdgxBusiness = "edgx-business.polygon.io"
    DelayedBusiness = "delayed-business.polygon.io"
    DelayedEdgxBusiness = "delayed-edgx-business.polygon.io"
    DelayedNasdaqLastSaleBusiness = "delayed-nasdaq-last-sale-business.polygon.io"
    DelayedNasdaqBasic = "delayed-nasdaq-basic-business.polygon.io"
    DelayedFullMarketBusiness = "delayed-fullmarket-business.polygon.io"
    FullMarketBusiness = "fullmarket-business.polygon.io"
    NasdaqLastSaleBusiness = "nasdaq-last-sale-business.polygon.io"
    NasdaqBasicBusiness = "nasdaq-basic-business.polygon.io"


class Market(Enum):
    Stocks = "stocks"
    Options = "options"
    Forex = "forex"
    Crypto = "crypto"
    Indices = "indices"


class EventType(Enum):
    EquityAgg = "A"
    EquityAggMin = "AM"
    CryptoAgg = "XA"
    CryptoAggSec = "XAS"
    ForexAgg = "CA"
    ForexAggSec = "CAS"
    EquityTrade = "T"
    CryptoTrade = "XT"
    EquityQuote = "Q"
    ForexQuote = "C"
    CryptoQuote = "XQ"
    Imbalances = "NOI"
    LimitUpLimitDown = "LULD"
    CryptoL2 = "XL2"
    Value = "V"
    """Launchpad* EventTypes are only available to Launchpad users. These values are the same across all asset classes (
    stocks, options, forex, crypto).
    """
    LaunchpadValue = "LV"
    LaunchpadAggMin = "AM"
    """Business* EventTypes are only available to Business users. These values are the same across all asset classes (
    stocks, options, forex, crypto).
    """
    BusinessFairMarketValue = "FMV"
