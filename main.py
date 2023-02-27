from transitionMethods import *
from imageProc import *
from transitions import transitions
import win32gui
from botState import botState


win32gui.MessageBox(None, "Press OK to start.", "", 0)
hwnd = win32gui.FindWindow(None, "SNAP")
win32gui.SetForegroundWindow(hwnd)
width, height = 405, 720
win32gui.MoveWindow(hwnd, 0, 0, width, height, True)
time.sleep(2)

button_position = imgCheck('mission') 
if (button_position is not None):
    tap_away(coord.PLAY_BUTTON)
    time.sleep(4)

bot = botState()
bot.add_state(transitions)
while True:
    bot.printstates()
    bot.run_state()
    time.sleep(1)
