import usb_hid
import time
import math
import random
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from time import sleep

keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
radius = 5
angle = 0

def move_mouse_randomly(mouse):
    global angle
    
    x = int(radius * math.cos(math.radians(angle)))
    y = int(radius * math.sin(math.radians(angle)))
    mouse.move(x, y, 0)

    # Adds randomness to the circular mouse movements.
    angle += random.uniform(1, 10)
    if angle >= 360:
        angle = 0
        
def press_scroll_lock_randomly(keyboard):
    if random.random() < 0.1:
        keyboard.press(Keycode.SCROLL_LOCK)
        keyboard.release(Keycode.SCROLL_LOCK)        

while True:
    move_mouse_randomly(mouse)
    press_scroll_lock_randomly(keyboard)
        
    sleep(0.025)
