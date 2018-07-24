from src.core.engine.actions import IDLE_TO_IDLE
from src.core.engine.transition_processors.transition_processor import TransitionProcessor


class SlotIdleProcessor(TransitionProcessor):
    def process(self):
        self.check_availability()
        self.consume_bet()
        self.calculator.calculate(self.game)
        self.consume_win()
        return self.get_transition_action()

    def consume_bet(self):
        context = self.game.context
        bet = self.game.protocol.request['bet']
        lines = len(self.game.rule.paylines)
        context.bet = bet * lines
        context.balance = context.balance - context.bet

    def consume_win(self):
        context = self.game.context
        context.balance = context.balance + context.total_win

    def check_availability(self):
        context = self.game.context
        bet = self.game.protocol.request['bet']
        lines = len(self.game.rule.paylines)
        if context.balance < bet * lines:
            raise BaseException('Not enough money({})'.format(context.balance))

    def get_transition_action(self):
        return IDLE_TO_IDLE