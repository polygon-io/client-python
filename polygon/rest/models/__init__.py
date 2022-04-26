from .aggs import *
from .trades import *
from .quotes import *
from .markets import *
from .tickers import *

from enum import Enum


class Sort(Enum):
    ASC = "asc"
    DESC = "desc"

class Order(Enum):
    ASC = "asc"
    DESC = "desc"

class Locale(Enum):
    US = "us"
    GLOBAL = "global"

class Market(Enum):
    STOCKS = "stocks"
    CRYPTO = "crypto"
    FX = "fx"