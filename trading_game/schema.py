import sqlite3
conn = sqlite3.connect('Terminal_Trader_Game.db')

c = conn.cursor()

c.execute('''CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username VARCHAR(128), 
password VARCHAR(128),
balance float
);'''
)

c.execute('''CREATE TABLE stock (
id INTEGER PRIMARY KEY AUTOINCREMENT,
stock_name Varchar,
stock_symbol VARCHAR,
stock_price INTEGER,
stock_exchange Text
portfolio float,
username VARCHAR,
volume INTEGET,
FOREIGN KEY(username) REFERENCES users(username)
);''')


conn.commit()
c.close()
conn.close()
    