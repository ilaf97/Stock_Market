import unittest
from src.exchange_metrics.all_share_index import AllShareIndex
from tests.test_data.objects_for_tests import DataObjectsForTests as Data


class TestExchangeMetrics(unittest.TestCase):

    def setUp(self) -> None:
        self.all_share_index = AllShareIndex(Data.test_volume_weighted_stock_prices)

    def test_calculate_geometric_mean(self) -> None:
        all_share_index = self.all_share_index.calculate_all_share_index()
        self.assertAlmostEqual(all_share_index, 99.1869)

