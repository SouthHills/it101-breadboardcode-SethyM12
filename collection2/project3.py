from gpiozero import RGBLED
import time
from pathlib import Path

LED = RGBLED(red=20, green=21, blue=12, active_high=True)
FILE = Path('/sys/class/thermal/thermal_zone0/temp')

def loop():
    global LED, FILE
    LED.on()
    while True:
        temp = int(FILE.read_text()) / 1000
        
        print(temp)
        if temp > 80:
            set_color(1, 0, 0)
        elif temp < 20:
            set_color(0, 0, 1)
        else:
            set_color(temp / 100, 0, (100 - temp) / 100)
        time.sleep(1)

def set_color(r, g, b):
    global LED
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def destroy():
    LED.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
