from polygon import RESTClient
import unittest
import httpretty  # type: ignore

mocks = [
    (
        "/v2/aggs/ticker/AAPL/range/1/day/2005-04-01/2005-04-04",
        '{"ticker":"AAPL","queryCount":2,"resultsCount":2,"adjusted":true,"results":[{"v":6.42646396e+08,"vw":1.469,"o":1.5032,"c":1.4604,"h":1.5064,"l":1.4489,"t":1112331600000,"n":82132},{"v":5.78172308e+08,"vw":1.4589,"o":1.4639,"c":1.4675,"h":1.4754,"l":1.4343,"t":1112587200000,"n":65543}],"status":"OK","request_id":"12afda77aab3b1936c5fb6ef4241ae42","count":2}',
    ),
    (
        "/v2/aggs/grouped/locale/us/market/stocks/2005-04-04",
        '{"queryCount":1,"resultsCount":1,"adjusted": true,"results": [{"T":"GIK","v":895345,"vw":9.9979,"o":9.99,"c":10.02,"h":10.02,"l":9.9,"t":1602705600000,"n":96}],"status":"OK","request_id":"eae3ded2d6d43f978125b7a8a609fad9","count":1}',
    ),
    (
        "/v1/open-close/AAPL/2005-04-01",
        '{"status": "OK","from": "2021-04-01","symbol": "AAPL","open": 123.66,"high": 124.18,"low": 122.49,"close": 123,"volume": 75089134,"afterHours": 123,"preMarket": 123.45}',
    ),
    (
        "/v2/aggs/ticker/AAPL/prev",
        '{"ticker":"AAPL","queryCount":1,"resultsCount":1,"adjusted":true,"results":[{"T":"AAPL","v":9.5595226e+07,"vw":158.6074,"o":162.25,"c":156.8,"h":162.34,"l":156.72,"t":1651003200000,"n":899965}],"status":"OK","request_id":"5e5378d5ecaf3df794bb52e45d015d2e","count":1}',
    ),
]


class BaseTest(unittest.TestCase):
    setup = False

    def setUp(self):
        if self.setup:
            return
        httpretty.enable(verbose=True, allow_net_connect=False)
        c = RESTClient("")
        for m in mocks:
            httpretty.register_uri(httpretty.GET, c.BASE + m[0], m[1])
        self.setup = True
