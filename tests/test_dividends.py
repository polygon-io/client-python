from polygon.rest.models import Dividend
from mocks import BaseTest

class DividendsTest(BaseTest):
    def test_list_dividends(self):
        dividends = [d for d in self.c.list_dividends()]
        expected = [
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2025-06-12', frequency=4, pay_date='2025-06-30', record_date='2025-06-15', ticker='CSSEN'),
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2025-03-13', frequency=4, pay_date='2025-03-31', record_date='2025-03-15', ticker='CSSEN'),
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2024-12-12', frequency=4, pay_date='2024-12-31', record_date='2024-12-15', ticker='CSSEN'),
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2024-09-12', frequency=4, pay_date='2024-09-30', record_date='2024-09-15', ticker='CSSEN'),
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2024-06-13', frequency=4, pay_date='2024-06-30', record_date='2024-06-15', ticker='CSSEN'),
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2024-03-14', frequency=4, pay_date='2024-03-31', record_date='2024-03-15', ticker='CSSEN'),
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2023-12-14', frequency=4, pay_date='2023-12-31', record_date='2023-12-15', ticker='CSSEN'),
            Dividend(cash_amount=0.5, declaration_date='2022-02-10', dividend_type='CD', ex_dividend_date='2023-11-13', frequency=4, pay_date='2023-11-15', record_date='2023-11-14', ticker='AIRTP'),
            Dividend(cash_amount=0.59375, declaration_date='2020-09-09', dividend_type='CD', ex_dividend_date='2023-09-14', frequency=4, pay_date='2023-09-30', record_date='2023-09-15', ticker='CSSEN'),
            Dividend(cash_amount=0.5, declaration_date='2022-02-10', dividend_type='CD', ex_dividend_date='2023-08-11', frequency=4, pay_date='2023-08-15', record_date='2023-08-14', ticker='AIRTP')
        ]
        self.assertEqual(dividends, expected)