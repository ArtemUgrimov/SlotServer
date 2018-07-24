from src.core.engine.actions import BET, IDLE_TO_IDLE
from src.core.engine.engine import Engine
from src.core.engine.state import State
from src.core.engine.states import IDLE
from src.slot.calculator import SlotIdleCalculator
from src.slot.transition_processor import SlotIdleProcessor


class SlotEngine(Engine):
    def __init__(self, game):
        super(SlotEngine, self).__init__(game)

        idle_state = State(IDLE)
        self.state = idle_state
        self.add_state(idle_state)
        self.add_transition_condition(IDLE, BET, SlotIdleProcessor(self.game, SlotIdleCalculator()))
        self.add_transition(IDLE, IDLE_TO_IDLE, IDLE)