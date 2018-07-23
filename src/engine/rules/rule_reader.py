from src.engine.rules.rule import GameRule


class RuleReader:
    rules = {}

    def read(self):
        # select * from game_rules ...
        # fill RuleReader.rules dictionary
        pass

    @staticmethod
    def get(game_name: str) -> GameRule:
        return RuleReader.rules[game_name]