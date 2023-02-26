import pyautogui
import time
import coord


# duration in ms
def swipe(x1,y1,x2,y2,duration): 
    pyautogui.mouseDown(x1, y1)
    pyautogui.moveTo(x2, y2, duration=duration/1000)
    pyautogui.mouseUp()
    time.sleep(0.08)
    pyautogui.moveTo(coord.IDLE_MOUSE_POSITION[0], coord.IDLE_MOUSE_POSITION[1])
    pyautogui.click()

def tap(pos):
    pyautogui.click(pos[0],pos[1])

def tap_away(pos):
    tap(pos)
    tap(coord.IDLE_MOUSE_POSITION)

