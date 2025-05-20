from gpiozero import LED as LEDClass # Alias
import time
import subprocess

LED = LEDClass(17)  # define led
LED2 = LEDClass(12)

def loop():
    global LED
    while True:
        if is_internet_connected():
            LED2.on()
            LED.off()
        else:
            LED2.off()
            LED.on()

def is_internet_connected():
    try:
        # Run the ping command with a timeout of 2 seconds and count 1 packet
        subprocess.check_output(['ping', '-c', '1', '-W', '2', 'www.google.com'])
        return True
    except subprocess.CalledProcessError:
        return False

def destroy():
    global LED, LED2
    # Release resources
    LED.close()
    LED2.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pins {LED.pin} and {LED2.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
