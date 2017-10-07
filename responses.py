class Response:
	def __init__(self):
		self.response = {}

	def fill(self, game):
		pass

	def get(self):
		return self.response


class ConnectResponse(Response):
	def fill(self, game):
		self.response = {}
		
		# self.response['session'] = game.session()
		self.response['state'] = game.engine.state
		self.response['window'] = game.context.window
		self.response['symbols'] = game.context.symbols
		self.response['paylines'] = game.rule.paylines.get_array()

class SpinResponse(Response):
	def fill(self, game):
		self.response = {}

		self.response['state'] = game.engine.state
		self.response['window'] = game.context.window
		if len(game.context.wins):
			wins = {}
			wins['lines'] = game.context.wins
			wins['total_win'] = game.context.win

			self.response['wins'] = wins

		print('\n\t\tWINS!!!')
		print(game.context.wins)

