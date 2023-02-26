import os
from pyautogui import *




script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'images')
region = (10, 32, 490 - 10, 671 - 32)

def imgCheck(str, confidence=0.95, grayscale=True, region=region):
    image_pos = locateCenterOnScreen(
        image_path + '/' + str + '.png', confidence=confidence, grayscale=grayscale, region=region)
    return image_pos


def locateColorOnScreen(rgbHex,region=region):
    # Define the color you want to search for (in RGB format)
    color = decCovert(rgbHex)
    image = screenshot(region=region)
    print(image.width,image.height)
    for x in range(image.width):
        for y in range(image.height):
            # Get the RGB color of the pixel at (x, y)
            x1,y1 = x+region[0], y+region[1]
            pixel_color = image.getpixel((x,y))
            if pixel_color == color:
                print(f"Found color {color} at position ({x1}, {y1})")
                return (x1,y1)
                # break
                
    return None

def decCovert(hex_color):
    hex_color = 0x2548ff
    red = (hex_color >> 16) & 0xff
    green = (hex_color >> 8) & 0xff
    blue = hex_color & 0xff
    return (red,green,blue)