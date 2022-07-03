from functools import reduce
from typing import Dict


class AllShareIndex:

    def __init__(self, all_stock_volume_weighted_stock_price: Dict[str, float]) -> None:
        self.__volume_weighted_stock_prices_list = list(all_stock_volume_weighted_stock_price.values())

    def calculate_all_share_index(self) -> float:
        return self.__calculate_geometric_mean()

    def __calculate_geometric_mean(self) -> float:
        root_factor = len(self.__volume_weighted_stock_prices_list)
        price_product = reduce(lambda x, y: float(x)*float(y), self.__volume_weighted_stock_prices_list)
        geometric_mean = round(price_product ** (1 / float(root_factor)), 4)
        return geometric_mean
