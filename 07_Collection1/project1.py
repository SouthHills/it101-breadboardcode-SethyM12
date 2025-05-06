from gpiozero import Button
import subprocess
from time import sleep

BUTTON1 = Button(12)
BUTTON2 = Button(21)

chromium_bool = False
firefox_bool = False

process1 = subprocess
process2 = subprocess

def open_chromium():
    global chromium_bool, process1
    chromium_bool = not chromium_bool
    if chromium_bool:
        print("Starting chromium...")
        process1 = subprocess.Popen(["chromium"])
        sleep(3)
    else:
        print("Closing chromium...")
        process1.terminate()

def open_firefox():
    global firefox_bool, process2
    firefox_bool = not firefox_bool
    if firefox_bool:
        print("Starting firefox")
        process2 = subprocess.Popen(["firefox"])
        sleep(3)
    else:
        print("Closing firefox...")
        process2.terminate()

def destroy():
    print("Exiting program...")

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        while True:
            BUTTON1.when_pressed = open_chromium
            BUTTON2.when_pressed = open_firefox
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
