if __name__ == '__main__':
    from arbitrage.database import Db
    from arbitrage.miner import Miner

    miner = Miner()
    db = Db("miner.db")
    db.create_database_if_not_exists()
    db.truncate_table()
    currencies = miner.get_all_coins()
    print(currencies)
    for coin in currencies:
        btc = miner.convert_to_btc(coin)
        coin_rate = miner.from_gbp(coin)
        btc_worth = miner.btc_to_gbp_quote(btc)
        profit = float(btc_worth) - float(coin_rate)
        db.insert_quote(coin, coin_rate, btc, btc_worth, profit)
    print(db.sort_by_gbp_difference())
# btc is not the amount bought by the pair currency