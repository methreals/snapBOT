from lib.transitionMethods import *
from lib.imageProc import *
from lib.botState import botState
import lib.coord
import win32gui
import time


win32gui.MessageBox(None, "Press OK to start.", "", 0)
hwnd = win32gui.FindWindow(None, "SNAP")
win32gui.SetForegroundWindow(hwnd)
width, height = 405, 720
win32gui.MoveWindow(hwnd, 0, 0, width, height, True)
time.sleep(2)

button_position = imgCheck('mission') 
if (button_position is not None):
    tap_away(lib.coord.PC['PLAY_BUTTON'])
    time.sleep(4)

bot = botState(early_retreats=True)

while True:
    bot.printstates()
    bot.run_state()
    time.sleep(1)
