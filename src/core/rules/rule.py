
class GameRule:
    def __init__(self, description: dict):
        # self.description = description
        self.game_type = description['game_type']
        self.set_rule_as_attributes(self, description)

    def set_rule_as_attributes(self, obj, description):
        for k, v in description.items():
            if isinstance(v, dict):
                setattr(obj, k, lambda: None)
                self.set_rule_as_attributes(getattr(obj, k), v)
            else:
                if isinstance(v, list):
                    setattr(obj, k, [])
                    for item in v:
                        if isinstance(item, dict):
                            getattr(obj, k).append(lambda: None)
                            self.set_rule_as_attributes(getattr(obj, k)[-1], item)
                        else:
                            setattr(obj, k, v)
                else:
                    setattr(obj, k, v)