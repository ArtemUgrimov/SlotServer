from src.command.command_handler import CommandHandler
from src.core.game_factory import GameFactory
from src.network.request import Request
from src.network.response import Response


class ConnectHandler(CommandHandler):
    def handle(self, request: Request):

        user_id = request['user_id']
        game_id = request['game_id']

        game = GameFactory.instance().get_game(game_id)
        self.read_context(game.context)

        self.server.games['{}_{}'.format(user_id, game_id)] = game

        response = Response()
        response.raw_response = {
            'command': 'connect',
            'state': 'idle'
        }

        return response

    def read_context(self, context):
        # read from DB
        data = {
            'balance': 1000
        }
        context.attributes = data