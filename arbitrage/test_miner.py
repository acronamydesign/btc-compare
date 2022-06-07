from unittest import TestCase
from arbitrage.miner import Miner


class TestMiner(TestCase):
    def test_get_all_coins(self):
        assert isinstance(Miner().get_all_coins(), list)

    def test_to_gbp(self):
        assert float(Miner().to_gbp('BTC')) >= 1

    def test_convert_to_btc(self):
        assert float(Miner().convert_to_btc('GBP')) <= 1
