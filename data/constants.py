import os.path


class Constants:
    """
    This class defines commonly used variables in the application.
    It is used to make tracking and changing values easier.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    trade_file_path = os.path.join(base_path, 'trades_data.csv')
    trades_headers = ['stock_symbol', 'timestamp', 'quantity', 'buy_sell', 'price']
    stocks_data = os.path.join(base_path, 'stocks_data')
    stocks_headers = ['stock_symbol', 'type', 'last_dividend', 'fixed_dividend', 'par_value']
