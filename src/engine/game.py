from src.engine.rules.rule_reader import RuleReader


class Game:
    def __init__(self, game_name, engine, protocol, context):
        self.rule = RuleReader.get(game_name)

        self.game_name = game_name
        self.context = context()
        self.engine = engine(self)
        self.protocol = protocol(self)

    def play(self):
        self.engine.play()
        response = self.protocol.get_response()

        self.engine.finalize()
        self.protocol.finalize()

        return response