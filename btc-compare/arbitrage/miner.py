from coinbase import *
import os
from coinbase.wallet.client import Client
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

        return fiat_ids + list(coins)

    def convert_to_btc(self, coin: str):
        to_btc = coin + "-btc"
        return self.client.get_sell_price(currencey_pair= to_btc).amount

    def to_gbp(self, coin: str):
        to_gbp = "gbp-" + coin
        return self.client.get_sell_price(currencey_pair= to_gbp).amount

    def btc_to_gbp_quote(self, btc: float):
        sell_price = self.client.get_sell_price(currency_pair= 'BTC-GBP').amount
        return float(sell_price) * float(btc)  # caution may produce errors!
