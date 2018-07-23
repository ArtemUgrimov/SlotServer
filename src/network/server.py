from http.server import HTTPServer

from src.command.connect_handler import ConnectHandler
from src.command.default_handler import DefaultHandler
from src.command.ping_handler import PingHandler
from src.engine.rules.rule_reader import RuleReader
from src.network.request import Request


class Server(HTTPServer):
    def __init__(self, server_address, request_handler_class):
        HTTPServer.__init__(self, server_address, request_handler_class)

        self.command_handlers = {
            'connect': ConnectHandler(self),
            'ping': PingHandler(self)
        }
        self.default_handler = DefaultHandler(self)

        self.games = {}

        self.read_rules()

    def handle(self, request):

        request_obj = Request(request)
        handler = self.command_handlers.get(request_obj.command, self.default_handler)
        response = handler.handle(request_obj, self)

        return response

    def error(self, msg):
        return {'status': 'error', 'message': msg}

    def read_rules(self):
        reader = RuleReader()
        reader.read()