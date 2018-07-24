from src.core.engine.reaction import Reaction
from src.core.engine.state import State
from src.core.engine.transition_processors.transition_processor import TransitionProcessor


class StateMachine:
    def __init__(self):
        self.prior_state = None
        self.state = None

        self.states = {}
        self.transitions = {}
        self.transition_processors = {}

    def add_transition_condition(self, state: str, action: str, transition_processor: TransitionProcessor):
        self.transition_processors['{}_{}'.format(state, action)] = transition_processor

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
        processor_desc = '{}_{}'.format(self.state.state_name, action)
        if processor_desc in self.transition_processors:
            processor = self.transition_processors[processor_desc]
            inner_action = processor.process()
        else:
            raise BaseException('No such processor. State {}, action {}'.format(self.state.state_name, action))

        transition_desc = '{}_{}'.format(self.state.state_name, inner_action)
        if transition_desc in self.transitions:
            transition = self.transitions[transition_desc]
            self.prior_state = self.state
            self.state = self.states[transition[0]]
            reaction = transition[1]
            if reaction is not None:
                reaction.react()
        else:
            raise BaseException('No such transition. State {}, action {}'.format(self.state.state_name, inner_action))