from polygon.rest.models import OptionsContract
from base import BaseTest


class ContractsTest(BaseTest):
    def test_get_options_contract(self):
        contract = self.c.get_options_contract("OEVRI240119C00002500")
        expected = [
        ]
        self.assertEqual(contract, expected)