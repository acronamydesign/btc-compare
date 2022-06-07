from coinbase import *
import os
from coinbasev2.wallet.client import Client
from arbitrage.credentials import AuthManager


class Miner:
    def __init__(self):
        credentials = AuthManager().authenticate()
        self.client = Client(credentials["api"], credentials["secret"])

    def get_all_coins(self):
        fiat = self.client.get_currencies()
        fiat_ids = []
        for item in list(fiat["data"]):
            fiat_ids += [item["id"]]
        coins = self.client.get_exchange_rates(currency='GBP').rates.keys()

        # return fiat_ids + list(coins)
        return list(coins)

    def convert_to_btc(self, coin: str):
        to_btc = "BTC-" + coin
        return 1 / float(self.client.get_sell_price(currency="GBP",currencey_pair= to_btc).amount)

    def to_gbp(self, coin: str):
        to_gbp = coin + "-GBP"
        return float(self.client.get_sell_price(currencey_pair= to_gbp).amount)

    def from_gbp(self, coin: str):
        to_gbp = coin + "-GBP"
        return 1 / float(self.client.get_sell_price(currencey_pair= to_gbp).amount)

    def btc_to_gbp_quote(self, btc: float):
        sell_price = self.to_gbp('btc')
        return float(sell_price) * float(btc)  # caution may produce errors!