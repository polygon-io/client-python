from polygon import RESTClient
import unittest
import httpretty

mocks = [
    (
        "/v2/aggs/ticker/AAPL/range/1/day/2005-04-01/2005-04-04",
        '{"ticker":"AAPL","queryCount":2,"resultsCount":2,"adjusted":true,"results":[{"v":6.42646396e+08,"vw":1.469,"o":1.5032,"c":1.4604,"h":1.5064,"l":1.4489,"t":1112331600000,"n":82132},{"v":5.78172308e+08,"vw":1.4589,"o":1.4639,"c":1.4675,"h":1.4754,"l":1.4343,"t":1112587200000,"n":65543}],"status":"OK","request_id":"12afda77aab3b1936c5fb6ef4241ae42","count":2}'
    )
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

