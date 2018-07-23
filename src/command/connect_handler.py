from src.command.command_handler import CommandHandler
from src.engine.game_factory import GameFactory
from src.network.request import Request
from src.network.response import Response
from src.network.server import Server


class ConnectHandler(CommandHandler):
    def handle(self, request: Request, server: Server):

        user_id = request['user_id']
        game_id = request['game_id']

        game = getattr(GameFactory.instance, 'get_game', game_id)

        server.games['{}_{}'.format(user_id, game_id)] = game

        response = Response()
        response.raw_response = {
            'status': 'ok',
            'command': 'connect',
            'state': 'idle'
        }

        return response