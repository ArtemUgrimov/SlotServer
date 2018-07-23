from src.command.command_handler import CommandHandler
from src.network.request import Request
from src.network.response import Response
from src.network.server import Server


class PingHandler(CommandHandler):
    def handle(self, request: Request, server: Server):
        return Response()