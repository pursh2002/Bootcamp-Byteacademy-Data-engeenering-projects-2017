import requests

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

	def company_search(self,s):
		stock = requests.get(self.lookup_url+s)
		return stock.json()
		

	def get_quote(self,string):
		stock = requests.get(self.quote_url+string)
		return stock.json()

#search = Markit()
#print(search.company_search("AAPL"))
#print(search.get_quote('AAPL'))

