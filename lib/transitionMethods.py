from lib.imageProc import *
from lib.utils import *
import lib.coord
import time
import random


class transitionMethods:

    def __init__(self, early_retreats, emu):
        self.current_state = 'START_TURN'
        self.early_retreats = early_retreats
        self.emu = emu
        self.lastPos = [0, 0]
        self.lastLoc = 0
        if (emu):
            self.region = (0, 0, 403, 718)
            self.coord = lib.coord.emu
        else:
            self.region = (10, 32, 490 - 10, 671 - 32)
            self.coord = lib.coord.PC
        return

    def play_cards_transition(self):
        # turn start
        button_position = imgCheck(
            'startTurn', confidence=0.97, grayscale=False, emulator=self.emu, region=regionRawConvert(self.coord['REGION_LOWER_RIGHT_RAW']))
        if (button_position is not None):
            time.sleep(0.5)
            return True
        button_position2 = imgCheck(
            'startTurn2', confidence=0.97, grayscale=False, emulator=self.emu, region=regionRawConvert(self.coord['REGION_LOWER_RIGHT_RAW']))
        if (button_position2 is not None):
            time.sleep(0.5)
            return True
        return False

    def battle_transition(self):
        # play all cards
        for i in range(5):
            button_position = locateColorOnScreen(
                0x2548ff, region=regionRawConvert(self.coord['REGION_DRAG_CARDS_RAW']))
            if (button_position is not None):
                # dest = random.randint(0, 2)
                dest = self.tmp(button_position, 3)
                swipe(button_position[0]+20, button_position[1] +
                      20, self.coord['DRAG_TO'][dest], self.coord['DRAG_TO'][3], 50)
                tap(self.coord['IDLE_MOUSE_POSITION'])
                self.lastLoc = dest
                self.lastPos = button_position
                time.sleep(0.5)
            else:
                break
        tap_away(self.coord['END_TURN_BUTTON'])
        return True
    # remember last unsuccessful drag position so it won't make the same mistake again
    def tmp(self, button_position, x):
        if (button_position[0] == self.lastPos[0] and button_position[1] == self.lastPos[1]):
            bannedPos = self.lastLoc
            dest = random_int_exclude(bannedPos, list(
                range(x))) if bannedPos < x else 0
        else:
            dest = random.randint(0, x-1)
        return dest

    def retreat_transition(self):
        # check if I can retreat
        if (self.early_retreats == True):
            button_position = imgCheck(
                'playing36', confidence=0.97, emulator=self.emu, region=regionRawConvert(self.coord['REGION_LOWER_RIGHT_RAW']))
            if (button_position is not None):
                tap(self.coord['RETREAT_BUTTON_1'])
                time.sleep(0.3)
                tap(self.coord['RETREAT_BUTTON_2'])
                time.sleep(2)
                return True
        return False

    def snap_transition(self):
        # true if I'm winning lanes. skip
        return False

    def collect_rewards_transition(self):
        # check collect button, ret t
        button_position = imgCheck(
            'collectRewards', confidence=0.9, emulator=self.emu, region=regionRawConvert(self.coord['REGION_LOWER_RIGHT_RAW']))
        if (button_position is not None):
            tap_away(button_position)
            return True
        return False

    def start_turn_transition(self):
        # check start turn button
        button_position = imgCheck(
            'startTurn', emulator=self.emu, region=regionRawConvert(self.coord['REGION_LOWER_RIGHT_RAW']))
        if (button_position is not None):
            return True
        return False

    def next_transition(self):
        # check next button
        button_position = imgCheck('next', emulator=self.emu, region=regionRawConvert(
            self.coord['REGION_LOWER_RIGHT_RAW']))
        if (button_position is not None):
            tap(button_position)
            return True
        return False

    def main_menu_transition(self):
        # check play button
        button_position = imgCheck('mission', emulator=self.emu, region=regionRawConvert(
            self.coord['REGION_MISSION_RAW']))
        if (button_position is not None):
            for i in range(4):
                tap(self.coord['PLAY_BUTTON'])
                time.sleep(1)
            time.sleep(1)
            return True
        return False

    def start_game_transition(self):
        # ?
        return True
