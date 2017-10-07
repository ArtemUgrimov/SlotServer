class User:
	def __init__(self, key):
		self.__balance = 10000
		self.__key = key

	@property
	def balance(self):
		return self.__balance

	@property
	def key(self):
		return self.__key

	def increace_money(self, amount):
		self.__balance += amount

	def decreace_money(self, amount):
		if self.is_enough_to_bet(amount):
			self.__balance -= amount
		else:
			raise BaseException('There is not enough money')

	def is_enough_to_bet(self, bet_value):
		return self.__balance >= bet_value

