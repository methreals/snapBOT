# retreat early
from transitionMethods import *
from imageProc import *
from transition import transitions_retreat
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
    tap(coord.PLAY_BUTTON)
    time.sleep(4)

bot = botState()
bot.add_state(transitions_retreat)
while True:
    bot.printstates()
    bot.run_state()
    time.sleep(1)
