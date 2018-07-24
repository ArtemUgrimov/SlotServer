from src.engine.engine.state_machine import StateMachine


class Engine(StateMachine):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def play(self):
        pass

    def finalize(self):
        pass