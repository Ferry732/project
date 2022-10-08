Import RPi.GPIO as GPIO
import os

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
   
    GPIO.setup(18, GPIO.OUT)
   
def controlLED():
    try:
        while True:
            user_input = input(
                "Turn LED on or off with 1 or 0 (ctrl + c to exit):")
            if user_input is "1":
                GPIO.output(18, GPIO.HIGH)
                print("LED is on")
            elif user_input is "0":
                GPIO.output(18, GPIO.LOW)
                print("LED is off")
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")
       
setupGPIO()
controlLED()
