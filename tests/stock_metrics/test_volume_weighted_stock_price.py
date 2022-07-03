import unittest
from unittest.mock import patch
from src.stock_metrics.volume_weighted_stock_price import VolumeWeightedStockPrice
from tests.test_data.objects_for_tests import DataObjectsForTests as Data
from data.constants import Constants


class TestVolumeWeightedStockPrice(unittest.TestCase):

    def setUp(self) -> None:
        """
        Set the current time as 01/01/2022 00:00:00
        and get trades falling in previous 5 minutes in test data
        """
        d = Data()
        self.curr_time = 1640995200
        self.volume_weighted_stock_price = VolumeWeightedStockPrice(
            'POP',
            d.trades_data()
        )

    @patch('time.time', unittest.mock.MagicMock(return_value=1640995200))
    @patch('data.constants.Constants', new=Constants)
    def test_calculate_volume_weighted_stock_price(self):
        result = self.volume_weighted_stock_price.calculate_volume_weighted_stock_price()
        self.assertEqual(result, 388.9289)
