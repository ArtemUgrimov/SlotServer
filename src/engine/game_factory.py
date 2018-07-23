from src.engine.game import Game


class GameFactory:
    class __OnlyOne:
        def __init__(self):
            self.factory = {}

        def register_game(self, game_name: str, components):
            self.factory[game_name] = (components[0], components[1], components[2])

        def get_game(self, game_name):
            parameters = self.factory[game_name]
            return Game(game_name, parameters[0], parameters[1], parameters[2])

    instance = None

    def __init__(self):
        if not GameFactory.instance:
            GameFactory.instance = GameFactory.__OnlyOne()

    def __getattr__(self, name):
        return getattr(self.instance, name)