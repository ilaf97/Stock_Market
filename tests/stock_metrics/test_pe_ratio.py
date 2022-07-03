import unittest
from src.stock_metrics.pe_ratio import PeRatio
from tests.test_data.objects_for_tests import DataObjectsForTests as Data


class TestPeRatio(unittest.TestCase):

    def setUp(self) -> None:
        d = Data()
        self.pe_ratio = PeRatio(
            d.stocks_data(2),
            50
        )

    def test_calculate_pe_ratio(self) -> None:
        result = self.pe_ratio.calculate_pe_ratio()
        self.assertEqual(result, 2.1739)
