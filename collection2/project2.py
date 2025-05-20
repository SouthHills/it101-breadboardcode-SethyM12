# Description : Control LED with Photoresistor
from pathlib import Path
import sys
from gpiozero import LED
import time
from math import floor

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

ADC = ADCDevice() # Define an ADCDevice class object
LED1 = LED(21)
LED2 = LED(20)
LED3 = LED(26)
LED4 = LED(19)
LEDS = (LED1, LED2, LED3, LED4)

def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
    
def loop():
    global ADC, LEDS
    while True:
        value = ADC.analogRead(0)   # read the ADC value of channel 0   # Mapping to PWM duty cycle        

        lights = int(floor(value / 51))
        for i in range(lights):
            LEDS[i].on()
        for i in range(lights, 4):
            LEDS[i].off()
        time.sleep(0.1)

def destroy():
    global ADC, LEDS
    ADC.close()
    for i in LEDS:
        i.off()
    
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        
