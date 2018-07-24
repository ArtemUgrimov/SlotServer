from src.core.game import Game
from src.slot.context import SlotContext
from src.slot.engine import SlotEngine
from src.slot.protocol import SlotProtocol


class GameFactory:

    __instance = None

    def __init__(self):
        self.factory = {
            'aj_slot': (SlotEngine, SlotProtocol, SlotContext)
        }

    @staticmethod
    def instance():
        if GameFactory.__instance is None:
            GameFactory.__instance = GameFactory()
        return GameFactory.__instance

    def get_game(self, game_name):
        parameters = self.factory[game_name]
        return Game(game_name, parameters[0], parameters[1], parameters[2])