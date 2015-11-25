# outline of project
# - wait for input from user + attract mode led
# - on input play jingle mp3 + led animation (this will likely need to be timed to coordinate)
# - then play a random mp3 from a specific folder and sets LEDs back to attract mode
# - at end of mp3 goes back to top of loop

# right now we are using mpg321 for mp3 playback. 
# may want to look at other options that allow code to be run when an mp3 is done
# this would allow for greater flexibility in running LEDs

# LEDs the plan at the moment is to run ws2801 LEDs off an arduino
# which receives commands to run specific sequences from a raspberry pi
# for now the plan is to do it over digital pin hi/lo
# but I should investigate spi/serial options down the road

#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

#setup buttons as inputs
GPIO.setmode(GPIO.BCM)
#Sets up GPIO pin 23 as input. This can be changed later to another input type if desired. 
GPIO.setup(23, GPIO.IN)

#sets "playing" to false
#this lets us stop the player
#on a press if the sound is playing  
#this is from a p revious project and MAY not be needed in this one

playing=0

#runs the indented code forever
#"while" tells the program to keep 
#doing something until the second 
#part is false. I made it "True" so 
#it will loop forever

while True:
        #if a sounds is not playing do this
        if ( playing == 0):
                #if someone pressons button one play a randomly selected mp3 from folder /Motivation/Quote/
                if ( GPIO.input(23) == False ):
                        os.system('sudo mpg321 -Z /Motivation/Quote/* ')
                        #set 'playing' value to 'true'
                        playing = 1

        #if a sound is not playing do this
        else:
                #if either button is pressed and a sound is playing STOP IT!
                if( GPIO.input(23) == False or GPIO.input(24) == False or GPIO.input(25) == False):
                        #stops the sound
                        os.system('sudo pkill -SIGKILL mpg321 #force exit')
                        #sets my "playing" variable to false
                        playing=0
        #waits half of a second before starting over again 
        #at the top of my while loop 
        sleep(0.5);
