from BaseHTTPServer import HTTPServer
from game import Game
from session import Session
from user import User
import json


class Server(HTTPServer):
	def __init__(self, server_address, RequestHandlerClass):
		HTTPServer.__init__(self, server_address, RequestHandlerClass)
		
		# user_key to user
		self.users = {}
		# session_id to session
		self.sessions = {}
		# user to session
		self.user_sessions = {}

	def handle(self, request):
		if 'session' in request:
			if request['session'] in self.sessions:
				session = self.sessions[request['session']]
				game = session.game
				user = self.users[session.user_key]
			else:
				return self.error('No such session')
		else:
			if 'user' in request:
				user_key = request['user']
				if user_key in self.user_sessions:
					session = self.user_sessions[user_key]
					game = session.game
					user = self.users[user_key]
				else:
					user = User(user_key)
					game = Game(request['game_id'], user)
					session = Session(user_key, game)
					
					self.users[user_key] = user
					self.sessions[session.id] = session
					self.user_sessions[user_key] = session
			else:
				return self.error('cannot connect')

		response = game.process(request['command'], request)
		self.complete_response(response, session, user)
		return json.dumps(response, indent=4)

	def complete_response(self, response, session, user):
		response['session'] = session.id

		usr = {}
		usr['balance'] = user.balance
		usr['key'] = user.key
		response['user'] = usr


	def error(self, msg):
		return {'status': 'error', 'message': msg}