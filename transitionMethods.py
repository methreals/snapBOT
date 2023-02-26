import pyautogui
from imageProc import *
from utils import *
from coord import *
import time
import random


def play_cards_transition():
    # check if any cards playable?
    button_position = imgCheck('startTurn',confidence=0.98,grayscale=False) 
    if (button_position is not None):
        time.sleep(0.5)
        return True
    button_position2 = imgCheck('startTurn2')
    if (button_position2 is not None):
        time.sleep(0.5)
        return True
    return False


def battle_transition():
    # play all cards, ret true when all finished 
    for i in range(5):
        button_position = locateColorOnScreen(0x2548ff)
        if (button_position is not None):
            dest = random.randint(0, 2)
            swipe(button_position[0]+20,button_position[1]+20,coord.DRAG_TO[dest],coord.DRAG_TO[3],50)
            tap(coord.IDLE_MOUSE_POSITION)
            time.sleep(0.5)
        else:
            break
        # return False
    tap_away(coord.END_TURN_BUTTON)
    return True


def retreat_transition():
    # check if im losing , or after 3rd turn
    button_position = imgCheck('playing36',confidence=0.97) 
    if (button_position is not None):
        tap(RETREAT_BUTTON_1)
        time.sleep(0.5)
        tap(RETREAT_BUTTON_2)
        time.sleep(2)
        return True
    return False


def snap_transition():
    # true if I'm winning lanes. skip
    return False


def collect_rewards_transition():
    # check collect button, ret t
    button_position = imgCheck('collectRewards',confidence=0.9) 
    if (button_position is not None):
        tap_away(button_position)
        return True
    return False


def start_turn_transition():
    # check start turn button, ret t
    button_position = imgCheck('startTurn') 
    if (button_position is not None):
        return True
    return False


def next_transition():
    # check next button
    button_position = imgCheck('next') 
    if (button_position is not None):
        tap(button_position)
        return True
    return False


def main_menu_transition():
    # check play button
    button_position = imgCheck('mission') 
    if (button_position is not None):
        for i in range(3):
            tap(coord.PLAY_BUTTON)
            time.sleep(1)
        time.sleep(1)
        return True
    return False


def start_game_transition():
    # ?
    return True