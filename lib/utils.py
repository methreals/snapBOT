import pyautogui
import time
import random
import lib.coord

# duration in ms
def swipe(x1, y1, x2, y2, duration):
    maxRandNum = 5
    x1 = x1+random.randint(0, maxRandNum)
    x2 = x2+random.randint(0, maxRandNum)
    y1 = y1+random.randint(0, maxRandNum)
    y2 = y2+random.randint(0, maxRandNum)
    pyautogui.mouseDown(x1, y1)
    pyautogui.moveTo(x2, y2, duration=duration/1000)
    pyautogui.mouseUp()
    time.sleep(0.08)
    pyautogui.moveTo(
        lib.coord.IDLE_MOUSE_POSITION[0], lib.coord.IDLE_MOUSE_POSITION[1])
    pyautogui.click()


def tap(pos):
    maxRandNum = 5
    x, y = pos[0]+random.randint(0, maxRandNum), pos[1] + \
        random.randint(0, maxRandNum)
    pyautogui.click(x, y)


def tap_away(pos):
    tap(pos)
    pyautogui.moveTo(
        lib.coord.IDLE_MOUSE_POSITION[0], lib.coord.IDLE_MOUSE_POSITION[1])

def tap_away_tap(pos):
    tap(pos)
    tap(lib.coord.IDLE_MOUSE_POSITION)

def regionRawConvert(raw_region):
    return (raw_region[0],raw_region[1],raw_region[2]-raw_region[0],raw_region[3]-raw_region[1])

def random_int_exclude(a, options):
    options.remove(a)
    return random.choice(options)