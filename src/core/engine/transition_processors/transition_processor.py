import abc


class TransitionProcessor(metaclass=abc.ABCMeta):
    def __init__(self, game, calculator=None):
        self.calculator = calculator
        self.game = game

    @abc.abstractmethod
    def process(self):
        raise BaseException('Not implemented')
