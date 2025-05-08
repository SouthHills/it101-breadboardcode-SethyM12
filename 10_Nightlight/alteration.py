# Description : Control LED with Photoresistor
from pathlib import Path
import sys
from gpiozero import LEDBarGraph
import time
from math import floor

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

LED_PINS : list[int] = [6, 19, 26, 23, 24, 25, 12, 16, 20, 21]
LEDS = LEDBarGraph(*LED_PINS, active_high=False)
ADC = ADCDevice() # Define an ADCDevice class object

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
        value = ADC.analogRead(0)   # read the ADC value of channel 0
        
        lights = int(floor(value / 25.5))

        #LED.value = value / 255.0    Mapping to PWM duty cycle        
        voltage = value / 255.0 * 3.3
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} \tLED Value: {LEDS.value:.2f}')

        for i in range(lights):
            LEDS[i].on()
        for i in range(lights + 1, 9):
            LEDS[i].off()

        time.sleep(0.01)

        
        

def destroy():
    global ADC, LEDS
    ADC.close()
    for led in LEDS:  # make led(on) move from left to right
        led.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()