from src.command.command_handler import CommandHandler
from src.network.request import Request
from src.network.response import Response


class PingHandler(CommandHandler):
    def handle(self, request: Request):
        return Response()