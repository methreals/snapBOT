from collections import namedtuple
from lib.transitionMethods import transitionMethods


class botState(transitionMethods):
    tok_next_t = namedtuple('tok_next_t', ['func', 'next_state'])

    def __init__(self,early_retreats=False,emu=False):
        self.tok_next = {}
        super().__init__(early_retreats,emu)
        self.transitions = {
            'START_TURN': [
                (self.play_cards_transition, 'PLAY_CARDS'),
                (self.snap_transition, 'SNAP'),
                (self.collect_rewards_transition, 'COLLECT_REWARDS'),
            ],
            'PLAY_CARDS': [
                (self.battle_transition, 'IN_BATTLE'),
                (self.collect_rewards_transition, 'COLLECT_REWARDS'),
            ],
            'IN_BATTLE': [
                (self.start_turn_transition, 'START_TURN'),
                (self.collect_rewards_transition, 'COLLECT_REWARDS'),
                # (retreat_transition,'RETREAT'),
            ],
            'COLLECT_REWARDS': [
                (self.next_transition, 'NEXT'),
            ],
            'NEXT': [
                (self.main_menu_transition, 'START_TURN'),
            ],
            'SNAP': [
                (lambda: True, 'PLAY_CARDS'),
                (self.collect_rewards_transition, 'COLLECT_REWARDS'),
            ],
            'RETREAT': [
                (self.collect_rewards_transition, 'COLLECT_REWARDS'),
            ],
            'MAIN': [
                (self.start_game_transition, 'START_TURN'),
            ],
        }
        self.transitions_retreat = self.transitions
        self.transitions_retreat['IN_BATTLE'].append((self.retreat_transition, 'RETREAT'))

        self.add_state()

    def add_state(self):
        if (self.emu):
            transitions = self.transitions_retreat
        else:
            transitions = self.transitions
        for state in transitions:
            if state not in self.tok_next:
                self.tok_next[state] = []
            for tuple in transitions[state]:
                self.tok_next[state].append(
                    self.tok_next_t(tuple[0], tuple[1]))

    def printstates(self):
        print(f"State: {self.current_state}")

    def run_state(self):
        state_transitions = self.tok_next[self.current_state]
        for condition_function, target_state in state_transitions:
            # Check the condition
            if condition_function():
                self.current_state = target_state
                break
