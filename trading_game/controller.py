from wrapper import Markit
import model, orm

"""
def get_username(username):
	self.username= username
	return input("Username: ")

def get_password(self):
	self.password =password
	return input("Password: ")
"""

def search_companies():
	user_input = input("Which company are you trying to lookup?\n")
	print("\nRetrieving company information...\n")
	print(model.retrieve_company_data(user_input))
	
def retrieve_market_data():
	user_input = input("Enter the ticker symbol (all caps) for the stock you are looking at.\n")
	print("\nRetrieving market data...\n")
	print(model.retrieve_company_data(user_input))

def buy_sell_stocks(check_balance,shares,stock_price):
	pass
	user_input = input("\nDo you want to buy or sell a stock?\n1. Buy\n2. Sell\n")
	if user_input == '1':
		model.buy_stocks(check_balance,shares,stock_price)
	elif user_input == '2':
		model.sell_stocks()
	else:
		print("Please enter a valid selection.")
		invalid_selection(buy_sell_stocks)
		
def def_options():
	print("\nWhat do you want to do today?")		
	print("1. Search companies")
	print("2. Retrieve market data for a stock")
	print("3. Buy or Sell stocks")
	print("4. View your portfolio")
	print("5. Exit")

	user_input = input()

	if user_input == '1':
		search_companies()
	elif user_input == '2':
		retrieve_market_data()
	elif user_input == '3':
		buy_sell_stocks()
	elif user_input == '4':
		view_portfolio()
	elif user_input == '5':
		user_exit()		
	else:
		print("Please enter a valid selection")
	def_options()
				
def trading():                                                                         
	print ("Welcome to tradingplatform, We care for you\n")  
	                                  
	prompt=int(input("""To open a new trading account, Press 1\n"""+                                        
                        """To access your existing account & transact press 2\n"""))    
	if prompt == 1:    
		username = input("Enter username \n") 
		password = input("Enter password \n")
		name = input("Enter your name \n")                                                                  
		orm.create_users(username,password)
		                                
	elif prompt == 2:
		username = input("Enter username\n")
		password = input("Enter password\n")
		                                                                     
		if (orm.username_available(username)):
			def_options() 
		else:
			print("User Does not exist")
			trading()                           
	
if __name__ == '__main__':
	trading()