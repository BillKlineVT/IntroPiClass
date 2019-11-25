# Simple Python Program to read a button input

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if (GPIO.input(23) == False):
        # wait until button released before registering a "press"
	while (GPIO.input(23) == False):
            print "button being held... waiting..."
            time.sleep(0.1)
        print "button released!"
    time.sleep(0.3)
