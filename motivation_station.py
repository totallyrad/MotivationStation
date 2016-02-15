#!/usr/bin/env python

from time import sleep
import os, random
import RPi.GPIO as GPIO


#setup buttons as inputs
GPIO.setmode(GPIO.BCM)
#sSets up GPIO pins
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#sets "playing" to false
#this lets us stop the player
#on a press if the sound is playing

playing=0

#runs the indented code forever
#"while" tells the program to keep
#doing something until the second
#part is false. I made it "True" so
#it will loop forever

while True:
        #if a sound is not playing do this
        if ( playing == 0):
                #if someone pressons button one play one file
                        if ( GPIO.input(23) == False ):
                                randomfile = random.choice(os.listdir("/home/pi/Motivation"))
                                file = '/home/pi/Motivation/' + randomfile

                                os.system('sudo mpg321 ' + file)
                                #set 'playing' value to 'true'
                                playing = 1


        #if a sound is not playing do this
        else:
                #if either button is pressed and a sound is playing STOP IT!
                if( GPIO.input(23) == False):
                        #stops the sound
                        os.system('sudo pkill -SIGKILL mpg321 #force exit')
                        #sets my "playing" variable to false
                        playing=0
        #waits half of a second before starting over again
        #at the top of my while loop
        sleep(0);
