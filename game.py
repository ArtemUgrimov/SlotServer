from context import Context
from engine import Engine
from rule import Rule
from protocol import Protocol
import random

class Game:
	def __init__(self, id, user):
		self.game_id = id
		self.engine = Engine(self, user)
		self.context = Context()
		self.rule = Rule()
		self.protocol = Protocol()

	def process(self, command, request):
		try:
			self.engine.play(command, request)
			rsp = self.protocol.get(self.engine, command)
			rsp.fill(self)
			return rsp.get()
		except BaseException, e:
			raise

	def serialize(self):
		pass

	def deserialize(self):
		pass
