from gpiozero import LED as LEDClass, Button
from signal import pause

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
checker = False

def toggleFlash():
    global checker; LED
    checker = not checker
    if checker:
        LED.blink(0.2, 0.2)
    else:
        LED.off()

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = toggleFlash
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

