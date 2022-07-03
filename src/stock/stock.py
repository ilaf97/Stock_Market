import pandas as pd
import src.stock_metrics as metrics
from src.stock.record_trade import RecordTrade


class Stock:

    def __init__(self, stock: pd.DataFrame) -> None :
        self.__stock = stock

    def find_dividend_yield(self, price: float) -> float:
        dividend_yield_obj = metrics.dividend_yield.DividendYield(self.__stock, price)
        return dividend_yield_obj.calculate_dividend_yield()

    def find_pe_ratio(self, price) -> float:
        pe_ratio_obj = metrics.pe_ratio.PeRatio(self.__stock, price)
        return pe_ratio_obj.calculate_pe_ratio()

    @staticmethod
    def record_trade(trade_data: [[str, str, int, str, float]]) -> None:
        """Can record multiple trades at once"""
        record_trade_obj = RecordTrade()
        record_trade_obj.save_trade(trade_data)

    def find_volume_weighted_stock_price(self) -> float:
        stock_symbol = self.__stock['stock_symbol']
        volume_weighted_stock_price_obj = \
            metrics.volume_weighted_stock_price.VolumeWeightedStockPrice(stock_symbol)
        return volume_weighted_stock_price_obj.calculate_volume_weighted_stock_price()


