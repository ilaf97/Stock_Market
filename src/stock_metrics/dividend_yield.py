import pandas as pd


class DividendYield:

    def __init__(self, stock_data: pd.DataFrame, price: float) -> None:
        self.__stock_data = stock_data
        self.__price = price

    def calculate_dividend_yield(self) -> float:
        return self.__calculate_common_dividend_yield() \
            if self.__stock_data["type"].lower() == "common" \
            else self.__calculate_preferred_dividend_yield()

    def __calculate_preferred_dividend_yield(self) -> float:
        return round(((self.__stock_data["fixed_dividend"] * self.__stock_data["par_value"]) / self.__price), 4)

    def __calculate_common_dividend_yield(self) -> float:
        return round((self.__stock_data["last_dividend"] / self.__price), 4)

