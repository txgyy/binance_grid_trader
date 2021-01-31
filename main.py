# -*- coding:utf-8 -*-

import time
import logging
from trader.binance_trader import BinanceTrader
from utils import config

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format, filename='grid_trader_log.txt')
logger = logging.getLogger('binance')

if __name__ == '__main__':

    config.loads('./config.json')

    trader = BinanceTrader()

    orders = trader.http_client.cancel_open_orders(config.symbol)
    print(f"cancel orders: {orders}")

    while True:
        try:
            trader.grid_trader()
            time.sleep(20)

        except Exception as error:
            print(f"catch error: {error}")
            time.sleep(5)
