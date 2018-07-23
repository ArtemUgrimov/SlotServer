import os

from src.engine.rules.rule import GameRule


class RuleReader:
    rules = {}

    def read(self):

        rules_dir = '{}/../res/rules/'.format(os.getcwd())

        for root, dirs, files in os.walk(rules_dir, topdown=False):
            for name in files:
                with open(os.path.join(root, name), 'r') as rule:
                    content = rule.read()
                    print(content)

    @staticmethod
    def get(game_name: str) -> GameRule:
        return RuleReader.rules[game_name]