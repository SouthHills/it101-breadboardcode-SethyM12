from gpiozero import Button, RGBLED as RGB
import time
import random
from signal import pause
# active_high must be true because it is a common anode RGBLed
LED = RGB(red=17, green=18, blue=27, active_high=True)
BUTTON = Button(12)
green = False

button_pressed = False

COLORS = ((1,0,0), (0,0,1), (0,1,0), (1,1,0))

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def check():
    global LED, BUTTON, button_pressed
    button_pressed = True
    if green == True:
        LED.blink(n = 5, on_color = (1, 0, 1))
        SystemExit
    if green == False:
        LED.blink(n = 5, on_color = (0, 1, 1))
        SystemExit

def loop():
    global COLORS, green, BUTTON, button_pressed
    while button_pressed == False :
        r=random.randint(0, 3)
        set_color(COLORS[r][0], COLORS[r][1], COLORS[r][2]) # Colors should be between 0 and 1
        if r == 2:
            green = True
            break
        ##print (f'r={r}% \tg={g}% \tb={b}%')
        time.sleep(1)
        
def destroy():
    LED.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        BUTTON.when_pressed = check
        loop()
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
