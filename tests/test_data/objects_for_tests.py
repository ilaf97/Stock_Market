import pandas as pd
import os


class DataObjectsForTests:
    base_path = os.path.dirname(os.path.abspath(__file__))
    test_volume_weighted_stock_prices = {
        'TEA': 100.0,
        'POP': 150.0,
        'ALE': 40.0,
        'GIN': 80.0,
        'JOE': 200.0
    }

    def stocks_data(self, loc: int) -> pd.DataFrame:
        return pd.read_json(os.path.join(self.base_path, 'test_stocks_data.json')).iloc[loc]

    def trades_data(self) -> str:
        return os.path.join(self.base_path, 'test_trades_data.csv')


