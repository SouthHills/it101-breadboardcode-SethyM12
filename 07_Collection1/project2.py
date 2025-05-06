from gpiozero import LED
from time import sleep

RED = LED(23)
YELLOW = LED(25)
GREEN = LED(21)

def destroy():
    global RED, YELLOW, GREEN
    RED.off()
    YELLOW.off()
    GREEN.off()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print("Traffic light")
    try:
        while True:
            RED.on()
            sleep(5)
            RED.off()
            GREEN.on()
            sleep(7)
            GREEN.off()
            YELLOW.on()
            sleep(2)
            YELLOW.off()
    except KeyboardInterrupt:
        destroy()