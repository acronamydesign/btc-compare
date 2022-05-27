from coinbase import *
import os
from coinbase.wallet.client import Client
from arbitrage.credentials import AuthManager


class Miner:
    def __init__(self):
        credentials = AuthManager().authenticate()
        self.client = Client(credentials["api"], credentials["secret"])

    def get_all_coins(self):
        return self.client.get_currencies()

    def convert_to_doge(self, coin: str):
        to_doge = coin + "-doge"
        return self.client.get_spot_price(currencey_pair= to_doge)

    def to_gbp(self, coin: str):
        to_gbp = coin + "-gbp"
        return self.client.get_sell_price(currencey_pair= to_gbp)

    def doge_to_gbp_quote(self, doge: float):
        sell_price = self.client.get_sell_price(currency_pair= 'DOGE-GBP')
        return sell_price * doge  # caution may produce errors!
