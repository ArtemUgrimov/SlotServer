from responses import ConnectResponse, SpinResponse
from engine import Engine, S_NONE, S_IDLE, A_CONNECT, A_SPIN, A_LOGOUT

class Protocol:
	def __init__(self):
		self.responses = {}
		self.responses[Engine.transition(S_NONE, A_CONNECT)] = ConnectResponse()
		self.responses[Engine.transition(S_IDLE, A_CONNECT)] = ConnectResponse()
		self.responses[Engine.transition(S_IDLE, A_SPIN)] = SpinResponse()

	def get(self, engine, command):
		transition = Engine.transition(engine.state, command)
		if transition in self.responses:
			return self.responses[transition]
		raise BaseException('There is no response for state ' + str(engine.state) + ' and action ' + str(command))