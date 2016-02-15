#!/usr/bin/env python

from time import sleep
import os, random
import RPi.GPIO as GPIO

#setup buttons as inputs
GPIO.setmode(GPIO.BCM)
#Sets up GPIO pins
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):  
  randomfile = random.choice(os.listdir("/home/pi/Motivation"))
  file = '/home/pi/Motivation/' + randomfile
  os.system('sudo mpg321 ' + file)

GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback, bouncetime=300)

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit 
GPIO.cleanup()           # clean up GPIO on normal exit
