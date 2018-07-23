from src.command.command_handler import CommandHandler
from src.network.request import Request
from src.network.response import Response
from src.network.server import Server


class DefaultHandler(CommandHandler):
    def handle(self, request: Request, server: Server):
        print('Default handler')
        return Response()