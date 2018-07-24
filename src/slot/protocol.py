from src.core.engine.actions import BET
from src.core.engine.states import IDLE
from src.core.protocol.protocol import Protocol
from src.slot.response import SlotResponse


class SlotProtocol(Protocol):
    def __init__(self, game):
        super().__init__(game)

        self.add_response_obj(IDLE, BET, SlotResponse())