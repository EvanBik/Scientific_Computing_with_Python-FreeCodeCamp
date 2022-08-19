class Category:

	def __init__(self,category):
		self.category = category
		self.ledger = []

	def __str__(self):
		s = self.category.center(30,"*") + "\n"
		for x in self.ledger:
			temp = f"{x['description'][:23]:23}{x['amount']:7.2f}"
			s += temp + "\n"
		s += "Total: " + str(self.get_balance())
		return s

	def deposit(self,amount,description=""):
		temp = {}
		temp['amount'] = amount
		temp['description'] = description
		self.ledger.append(temp)


	def withdraw(self,amount,description=""):
		if self.check_funds(amount):
			temp = {}
			temp['amount'] = 0 - amount
			temp['description'] = description
			self.ledger.append(temp)
			return True
		return False
		
	def get_balance(self):
		balance = 0
		for x in self.ledger:
			balance += x['amount']
		return balance
	
	def transfer(self,amount,to_category):
		if self.check_funds(amount):
			self.withdraw(amount, f'Transfer to {to_category.category}')
			to_category.deposit(amount, f'Transfer from {self.category}')
			return True
		return False

	def check_funds(self,amount):
		if amount > self.get_balance():
			return False
		return True

def create_spend_chart(categories):
	spend = []
	for c in categories:
		temp = 0 
		for x in c.ledger:
			if x['amount'] < 0:
				temp += abs(x['amount'])
		spend.append(temp)
	total = sum(spend)
	percentage = [i/total*100 for i in spend]
	s = 'Percentage spent by category'
	for i in range(100,-1,-10):
		s += "\n" + str(i).rjust(3) + "|"
		for j in percentage:
			if j > i:
				s += " o "
			else:
				s += "   "
		s += " "
	s += "\n    ----------"

	category_length = []
	for c in categories:
		category_length.append(len(c.category))
	max_length = max(category_length)

	for i in range(max_length):
		s += "\n    "
		for j in range(len(categories)):
			if i < category_length[j]:
				s += " " + categories[j].category[i] + " "
			else:
				s += "   "
		s += " "
	return s