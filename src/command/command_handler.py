import abc

from src.network.request import Request


class CommandHandler(metaclass=abc.ABCMeta):
    def __init__(self, server):
        self.server = server

    @abc.abstractmethod
    def handle(self, request: Request):
        raise NotImplemented()