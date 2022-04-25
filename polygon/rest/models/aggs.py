from dataclasses import dataclass


@dataclass
class Agg:
    open: float
    high: float
    low: float
    close: float
    volume: float
    vwap: float
    timestamp: int
    transactions: int

    @staticmethod
    def from_dict(d):
        return Agg(d["o"], d["h"], d["l"], d["c"], d["v"], d["vw"], d["t"], d["n"])
