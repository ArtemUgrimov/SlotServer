import abc

from src.network.request import Request
from src.network.server import Server


class CommandHandler(metaclass=abc.ABCMeta):
    def __init__(self, server: Server):
        self.server = server

    @abc.abstractmethod
    def handle(self, request: Request, server: Server):
        raise NotImplemented()