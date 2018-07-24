from src.core.engine.state_machine import StateMachine


class Engine(StateMachine):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def play(self):
        action = self.game.protocol.request.command
        self.process(action)

    def finalize(self):
        pass