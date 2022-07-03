from typing import Dict

import pandas as pd


class PeRatio:

    def __init__(self, stock_data: pd.DataFrame, price: float) -> None:
        self.__stock_data = stock_data
        self.__price = price

    def calculate_pe_ratio(self) -> float:
        return round((self.__price / self.__stock_data["last_dividend"]), 4)
