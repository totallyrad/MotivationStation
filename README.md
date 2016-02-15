# MotivationStation
This code supports the MotivatioStation Project. The intent is to create interactive art where individuals can share inspirational and motivational moments.

Ideally someone will walk up to your creation, press a button (or some other interaction) and receive words of positivity, encouragement and inspiration from others.

Recordings are sourced from around the world, with individuals able to record and submit anywhere in the world. 

For more remote locations the recordings can be updated on site, using simple software on Android devices to record, edit and add files to the directory.

This code is built for the Raspberry Pi on Raspbian (Jesse)

Installing Software on Pi

sudo apt-get install alsa-utils mpg123 python-dev python-rpi.gpio

We specify "/home/pi/Motivation" in the code, this can be changed if you would like, but to use in it's default setting:

Create a folder named "Motivation" in "/home/pi/". 
This folder is where you house your audio recordings.
I tend to access this folder via sftp as it's ready to go with stock Raspbian
Copying any files to this folder adds them to the potential lsit of files played. 

You may need to run raspi-config to ensure that the desired audio output is selected. 

I used GPIO 18, you can feel free to adjust the code to your liking. 

The button should have a 10k Pull Up Resistor.

CURRENT ISSUES:

Currently you have to hold the button in for a moment for the code to run. Not ideal.

NEXT STEPS:



After that will be figuring out how to control LEDs to do something when the button is pressed.

https://learn.adafruit.com/neopixels-on-raspberry-pi/software
