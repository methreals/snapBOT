from conditions import *
transitions = {
    'START_TURN': [
        (play_cards_transition,'PLAY_CARDS'),
        (snap_transition,'SNAP'),
        (retreat_transition,'RETREAT'),
        (collect_rewards_transition,'COLLECT_REWARDS'),
    ],
    'PLAY_CARDS': [
        (battle_transition,'IN_BATTLE'),
        (collect_rewards_transition,'COLLECT_REWARDS'),
    ],
    'IN_BATTLE':[
        (start_turn_transition,'START_TURN'),
        (collect_rewards_transition,'COLLECT_REWARDS'),
    ],
    'COLLECT_REWARDS': [
        (next_transition,'NEXT'),
    ],
    'NEXT': [
        (main_menu_transition,'START_TURN'),
    ],
    'SNAP': [
       (lambda: True,'PLAY_CARDS'),
       (collect_rewards_transition,'COLLECT_REWARDS'),
    ],
    'RETREAT': [
        (collect_rewards_transition,'COLLECT_REWARDS'),
    ],
    'MAIN': [
        (start_game_transition, 'START_TURN'),
    ],
}