import model
import sqlite3
import orm
from wrapper import Markit

conn = sqlite3.connect("Terminal_Trader_Game.db")
cur = conn.cursor()
		
def sign_verify(username, password):
	users = cur.execute("SELECT id FROM users WHERE username=(?) and password=(?)", (username, password))
	users = cur.fetchone()
	conn.commit()
	return users 
	
def username_available(username):
	cur.execute("SELECT username FROM users WHERE username = (?)",(username,))
	data = cur.fetchone()
	if data: 
		return True
	else:
		return False
	#conn.commit()
    
def create_users(username, password):
	cur.execute('INSERT INTO users(username, password) VALUES(?,?)', (username, password))
	conn.commit()
	
def create_balance(username,password)
	cur.execute('INSERT INTO users(username,balance) VALUES(?,?)'(pursh,1000000)
	
def check_balance(username):
	cur.execute('SELECT balance FROM users where username = ?',(username))
	balance = cur.fetchone()
	return balance	

def buying_stocks(username,password,stock_exchange,stock_name, stock_symbol,volume,price):
	cur.execute(('SELECT portfolio FROM stocks where username="{}".format(username))
	portfolio = cur.fetchone()[0]
	portfolio = portfolio + (shares * stock_price)
	cur.execute('INSERT INTO stocks(stock_name,stock_price,stock_exchange,portfolio) VALUES (?,?,?,?,?)',(stockname,symbol,price,exchange,portfolio))
	
def sell_stocks():
	pass	   
		


