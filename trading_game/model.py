import pandas as pd
from wrapper import Markit
import orm

'''
#class model:
	#def __init__(self, username, password, name):
		#self.id = id
		#self.username = username
		#self.password = password
		#self.name = name
'''		
		  	
def retrive_symbols(stock_symbol):
	object = Markit()
	companylist = pd.DataFrame.from_dict(object.company_search(stock_symbol))
	return(companylist)

def retrieve_company_data(stock_symbol):
	object = Markit()
	companyquote = object.get_quote(stock_symbol)
	return(companyquote)
	
def sign_verify(username, password):
	return orm.sign(username, password)

def username_available(username):
	return orm.username_available(username)

def create_user(username, password, portfolio):
	orm.create_users(username, password, portfolio)

def sell_stocks(shares, price):

def selling_stocks(check_balance, stock_exchange,stock_symbol,stock_price,username):
	# selling stocks
	
	print("\n\nTo acess any function below, enter the corresponding key")
	print("""To:
		want to sell stocks,press 1.
		check Balance, press 2.
		withdraw cash, press 3.
		exit service, press 4\n
		:""")
	status = input("")
	
	if status == '1':
		sell_stock(stock_name, check_balance, stock_exchange,symbols,stock_price,username,password,portfolio)
		
	if status == '2':
		passcheck(get_password)
		checkbalance(balance)
	elif status == '3':
		passcheck(get_password)
		withdraw()
	elif status == '4':
		print("Thank you for using our services")


def buy_stocks(username,shares,password,stock_exchange, stock_symbol,volume,stock_price):
	orm.check_balance(username)
	for cash in balance:
		if cash[balance'] == '0':
			print("insufficient balance") 
		if balance > (shares * stock_price):
			orm.buying_stocks(username,password,stock_exchange, stock_symbol,volume,stock_price)
	
	def buying_stocks(check_balance, stock_exchange, stock_symbol, stock_price, volume, username,password):
	#Check the balance
		print("\n\nTo access any function below, enter the corresponding key")
		print ('''To:
		want to buy stocks,press A.
		check Balance, press B.
		deposit cash,  press D.
		exit service,  press E\n
		:''')
		status = input("")
	
		if status == 'A':		
			passcheck(get_password,username)
			check_balance(balance)
	
		if status=='B':
			check_balance = orm.get_balance(username)
			
		  
		elif status=='D':
			passcheck(get_password,username)
			depositcash(stock_price*stock_symbol)

		elif status=='E':
			print ("Thank you for using our Services")
	# if enough balance, buy stocks, else return insufficient funds
	def buy(check_balance,shares,stock_price):
		number_of_shares = input("Enter number of shares: ")
		object = Markit()
		price = object.get_quote(stock_symbol)
		enter_price = input("Enter the price to purchase shares: ")

		if get_stock(stock) == None:
			stock_to_buy = {}
			stock_to_buy['shares'] = shares
			stock_to_buy['value'] = "{0:.2f}".format(float(stock_price))
		
		else:
			stock_to_buy = get_stock(stock)
			stock_to_buy['value'] = "{0:.2f}".format(float(enter_price) * int(number_of_shares)) 
			stock_to_buy['shares'] = str(int(stock_to_buy['shares']) + int(shares))
#return "Your balance is " + ({0:.2f}".format(float(enter_price) * int(number_of_shares) - balance)

def check_balance(username):
	balance = ORM.check_balance(username)
	return balance	

'''               

	
	pass

def sell_stocks(shares, price):
sale_price = input("Enter sale price: ")
	
	for stock in portfolio:
	    if stock['portfolio']
	    portfolio.remove(stock)
	pass	
	
'''
if __name__ == '__main__':
	buy_stocks(username,shares,password,stock_exchange, stock_symbol,volume,stock_price)