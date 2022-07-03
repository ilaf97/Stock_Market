import unittest
from src.stock_metrics.dividend_yield import DividendYield
from tests.test_data.objects_for_tests import DataObjectsForTests as Data


class TestDividendYield(unittest.TestCase):

    def setUp(self) -> None:
        d = Data()
        self.common_dividend_yield = DividendYield(
            d.stocks_data(1),
            50
        )
        self.preferred_dividend_yield = DividendYield(
            d.stocks_data(3),
            50
        )

    def test_calculate_common_dividend_yield(self) -> None:
        result = self.common_dividend_yield.calculate_dividend_yield()
        self.assertEqual(result, 0.16)

    def test_calculate_preferred_dividend_yield(self) -> None:
        result = self.preferred_dividend_yield.calculate_dividend_yield()
        self.assertEqual(result, 4.0)
