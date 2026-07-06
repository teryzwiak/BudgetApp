class Category:
	def __init__(self, name):
		self.name = name
		self.ledger = []

	def deposit(self, amount, description=""):
		self.ledger.append({"amount": amount, "description": description})
def create_spend_chart(categories):
    pass


food = Category('Food')
print(food)
food.deposit(1000)
print(food.ledger)
