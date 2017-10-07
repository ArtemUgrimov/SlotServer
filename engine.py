import random

#states
S_NONE = 'none'
S_IDLE = 'idle'

#actions
A_CONNECT = 'connect'
A_SPIN = 'spin'
A_LOGOUT = 'logout'

REELS = 5
SYMBOLS = 3

class Engine:
	def __init__(self, game, user):
		self.state = 'none'
		self.game = game
		self.user = user
		self.request = {}
		self.transitions = {}
		self.actions = {}
		
		self.transitions[Engine.transition(S_NONE, A_CONNECT)] = S_IDLE
		self.transitions[Engine.transition(S_IDLE, A_SPIN)] = S_IDLE
		self.transitions[Engine.transition(S_IDLE, A_LOGOUT)] = S_NONE
		
		self.actions[Engine.transition(S_NONE, A_CONNECT)] = self.__connect
		self.actions[Engine.transition(S_IDLE, A_SPIN)] = self.__spin

	def before_play(self, command):
		if command == A_CONNECT:
			transition = Engine.transition(self.state, A_CONNECT)
			if transition not in self.transitions:
				self.transitions[transition] = self.__connect


	def play(self, command, request):
		self.before_play(command)
		self.request = request

		transition = self.state + '_' + command
		if transition not in self.transitions:
			raise BaseException("No such transition from state : " + self.state + " with command " + command)
		if transition in self.actions:
			self.actions[transition]()

		self.state = self.transitions[transition]

	def __connect(self):
		self.context.symbols = list(range(1, 11))
		self.__create_window()

	def __spin(self):
		bet_value = int(self.request['bet'])
		if not self.__check_bet(bet_value):
			raise BaseException('Not enough money!')
		self.__calc_window()
		self.__calc_wins(bet_value)
		self.user.decreace_money(bet_value * len(self.rule.paylines.get_array()))
		self.user.increace_money(self.context.win)

	def __create_window(self):
		self.context.window = []
		for i in range(REELS):
			reel = []
			for j in range(SYMBOLS):
				reel.append(random.randrange(1, 11))
			self.context.window.append(reel)

	def __calc_window(self):
		for i in range(REELS):
			for j in range(SYMBOLS):
				self.context.window[i][j] = random.randrange(1, 11)

	def __calc_wins(self, bet_value):
		self.context.wins = self.paylines.get_wins(self.context.window, self.paytable, bet_value)
		self.context.win = 0
		for win in self.context.wins:
			self.context.win += win['win']

	def __check_bet(self, bet_value):
		return self.user.is_enough_to_bet(bet_value)

	@staticmethod
	def transition(state, action):
		return str(state) + '_' + str(action)

	@property
	def context(self):
		return self.game.context

	@property
	def rule(self):
		return self.game.rule

	@property
	def paytable(self):
		return self.rule.paytable

	@property
	def paylines(self):
		return self.rule.paylines