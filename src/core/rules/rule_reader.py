import json
import os
from pathlib import PureWindowsPath, Path

from src.core.rules.rule import GameRule


class RuleReader:
    rules = {}

    def read(self):

        rules_dir = str(Path(PureWindowsPath(r'{}\\res\\rules\\'.format(os.getcwd()))))

        for root, dirs, files in os.walk(rules_dir, topdown=False):
            for name in files:
                full_path = os.path.join(root, name)
                with open(full_path, 'r') as rule:
                    content = rule.read()
                    try:
                        converted_rule = json.loads(content)
                        rule = GameRule(converted_rule)
                        game_name = name.replace('.json', '')
                        RuleReader.rules[game_name] = rule
                    except BaseException as ex:
                        print('Cannot deserialize rule from file {}. \n{}'.format(name, ex))

    @staticmethod
    def get(game_name: str) -> GameRule:
        return RuleReader.rules[game_name]