from collections import namedtuple
import types
import imp
import os
import os.path


tok_next_t = namedtuple('tok_next_t', ['func', 'next_state'])
class botState:
    current_state = 'START_TURN'
    early_retreats = False
    def __init__(self):
        self.tok_next = {}

    def add_state(self,transitions):
        for state in transitions:
            if state not in self.tok_next:
                self.tok_next[state] = []
            for tuple in transitions[state]:
                self.tok_next[state].append(tok_next_t(tuple[0],tuple[1]))

    def printstates(self):
        print(self.current_state)

    def run_state(self):
        state_transitions = self.tok_next[self.current_state]
        for condition_function, target_state in state_transitions:
            # Check the condition
            if condition_function():
                self.current_state = target_state
                break