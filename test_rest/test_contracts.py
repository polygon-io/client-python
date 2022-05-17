from polygon.rest.models import OptionsContract
from base import BaseTest


class ContractsTest(BaseTest):
    def test_get_options_contract(self):
        contract = self.c.get_options_contract("OEVRI240119C00002500")
        expected = OptionsContract(
            additional_underlyings=None,
            cfi="OCASPS",
            correction=None,
            exercise_style="american",
            expiration_date="2024-01-19",
            primary_exchange="BATO",
            shares_per_contract=100,
            strike_price=2.5,
            size=None,
            ticker="O:EVRI240119C00002500",
            underlying_ticker="EVRI",
        )
        self.assertEqual(contract, expected)
