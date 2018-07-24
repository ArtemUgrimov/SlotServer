from src.engine.engine.reaction import Reaction
from src.engine.engine.state import State


class StateMachine:
    def __init__(self):
        self.prior_state = None
        self.state = None

        self.states = {}
        self.transitions = {}

    def add_state(self, state: State):
        self.states[state.state_name] = state

    def add_transition(self, state: str, action: str, new_state: str, reaction: Reaction = None):
        transition_desc = '{}_{}'.format(state, action)
        self.transitions[transition_desc] = (new_state, reaction)

    def remove_transition(self, state: str, action: str, new_state: str):
        transition_desc = '{}_{}'.format(state, action)
        if transition_desc in self.transitions:
            transition = self.transitions[transition_desc]
            if transition[0] == new_state:
                del self.transitions[transition_desc]

    def process(self, action):
        transition_desc = '{}_{}'.format(self.state.state_name, action)
        if transition_desc in self.transitions:
            transition = self.transitions[transition_desc]
            self.state = self.states[transition[0]]
            reaction = transition[1]
            if reaction is not None:
                reaction.react()
        else:
            raise BaseException('No such transition. State {}, action {}'.format(self.state.state_name, action))