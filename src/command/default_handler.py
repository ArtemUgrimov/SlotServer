from src.command.command_handler import CommandHandler
from src.network.request import Request


class DefaultHandler(CommandHandler):
    def handle(self, request: Request):

        game = self.server.games['{}_{}'.format(request.user_id, request.game_id)]
        response = game.play(request)

        return response