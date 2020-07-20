#!/usr/bin/ python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

try:
    while True:

        GPIO.output(21,True)
        time.sleep(0.2)
        GPIO.output(21,False)
        time.sleep(1)
        print("111")
        
except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    print("\nexit")
