import time
import pandas as pd
from data.constants import Constants


class VolumeWeightedStockPrice:

    def __init__(self, stock_symbol: str, trades_file_path: str = Constants.trade_file_path) -> None:
        self.__stock_symbol = stock_symbol
        self.__trades_file_path = trades_file_path

    def calculate_volume_weighted_stock_price(self) -> float:
        """Returns volume weighted stock price to 4 decimal places"""
        df = self.get_trades_in_last_five_mins()
        quantity_sum = df['quantity'].sum()
        sum_product_traded_price_and_quantity = ((df['quantity']) * df['price']).sum()
        volume_weighted_stock_price = round((sum_product_traded_price_and_quantity / float(quantity_sum)), 4)
        return volume_weighted_stock_price

    def get_trades_in_last_five_mins(self) -> pd.DataFrame:
        """Returns trades that occur in last 5 mins for stock"""
        df = self.__read_trades()
        # Assume trading test_data sorted by timestamp i.e. trade test_data immutable
        timestamps = list(df.loc[:, 'timestamp'])
        time_five_mins_ago = int(time.time()) - (5 * 60)
        closest_time = min(timestamps, key=lambda x: abs(x - time_five_mins_ago))
        return df.iloc[:timestamps.index(closest_time) + 1] \
            if closest_time > time_five_mins_ago \
            else df.loc[:timestamps.index(closest_time)]

    def __read_trades(self) -> pd.DataFrame:
        """Read trades test_data as pandas dataframe"""
        with open(self.__trades_file_path) as f:
            df = pd.read_csv(f, index_col=False)
            return df.loc[df['stock_symbol'] == self.__stock_symbol]
