from src.command.command_handler import CommandHandler
from src.network.request import Request
from src.network.response import Response


class DefaultHandler(CommandHandler):
    def handle(self, request: Request):
        print('Default handler')
        return Response()