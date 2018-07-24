from src.engine.game import Game


class GameFactory:

    __instance = None

    def __init__(self):
        self.factory = {}

    @staticmethod
    def instance():
        if GameFactory.__instance is None:
            GameFactory.__instance = GameFactory()
        return GameFactory.__instance

    def register_game(self, game_name: str, components):
        self.factory[game_name] = (components[0], components[1], components[2])

    def get_game(self, game_name):
        parameters = self.factory[game_name]
        return Game(game_name, parameters[0], parameters[1], parameters[2])