import random

class Session:
	def __init__(self, user_key, game):
		self.id = random.randrange(9999, 99999999)
		self.user_key = user_key
		self.game = game