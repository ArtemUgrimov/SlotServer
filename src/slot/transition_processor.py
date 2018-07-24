from src.core.engine.actions import IDLE_TO_IDLE
from src.core.engine.transition_processors.transition_processor import TransitionProcessor


class SlotIdleProcessor(TransitionProcessor):
    def process(self):
        self.check_availability()

        self.calculator.calculate(self.game)
        return self.get_transition_action()

    def check_availability(self):
        context = self.game.context
        bet = self.game.protocol.request['bet']
        if context.balance < bet:
            raise BaseException('Not enough money({})'.format(context.balance))

    def get_transition_action(self):
        return IDLE_TO_IDLE