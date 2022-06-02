import sqlite3


class Db:
    def __init__(self, database: str = 'test'):
        self.con = sqlite3.connect(database)  # database

    def create_database_if_not_exists(self):
        self.con.execute("CREATE TABLE IF NOT EXISTS main.quotes (coin TEXT NOT NULL,gbp_to_coin float NOT NULL,coin_to_btc_exchange_rate float NOT NULL,exchanged_btc_worth_in_gbp float NOT NULL,profit_in_gbp float NOT NULL);")
        self.con.commit()

    # coin is the coin to convert to btc and
    def insert_quote(self, coin:str, gbp_to_coin:float, coin_to_btc_exchange_rate:float, exchanged_btc_worth_in_gbp:float, profit_in_gbp:float):
        self.con.execute("INSERT INTO quotes(coin ,gbp_to_coin,coin_to_btc_exchange_rate,exchanged_btc_worth_in_gbp,profit_in_gbp) VALUES(?,?,?,?,?)", (coin, gbp_to_coin, coin_to_btc_exchange_rate, exchanged_btc_worth_in_gbp, profit_in_gbp))
        self.con.commit()

    def sort_by_gbp_difference(self):
        self.con.execute("SELECT * FROM quotes ORDER BY profit_in_gbp ASC")
        self.con.commit()

    def truncate_table(self):
        self.con.execute("DELETE FROM quotes")
        self.con.commit()
