import csv
import os.path
import data.constants as constants


class RecordTrade:
    tradeType = [[str, int, int, str, float]]

    def __init__(self) -> None:
        self.__field_names = constants.Constants.trades_headers
        self.__trades_file_path = constants.Constants.trade_file_path

    def save_trade(self, trades_list: tradeType) -> None:
        """Will check if file exists. If so, will append test_data; if not, will create a new file"""
        if os.path.exists(self.__trades_file_path):
            operation = 'a'
        else:
            operation = 'w'

        self.__write_to_file(trades_list, operation)

    def __write_to_file(self, trades_list: tradeType, operation: str) -> None:
        with open(self.__trades_file_path, operation, newline='') as f:
            writer = csv.writer(f)
            if operation == 'w':
                writer.writerow(self.__field_names)
            writer.writerows(trades_list)



