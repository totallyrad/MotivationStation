# MotivationStation
This code supports the MotivatioStation Project. The intent is to create interactive art where individuals can share inspirational and motivational moments.

Ideally someone will walk up to your creation, press a button (or some other interaction) and receive words of positivity, encouragement and inspiration from others.

Recordings are sourced from around the world, with individuals able to record and submit anywhere in the world. 

For more remote locations the recordings can be updated on site, using simple software on Android devices to record, edit and add files to the directory.

This code is built for the Raspberry Pi on Raspbian Lite (Jesse)

*Preparing for install

  sudo apt-get update

  sudo apt-get upgrade

*Installing Software on Pi

  sudo apt-get install alsa-utils mpg321 python-dev python-rpi.gpio

We specify "/home/pi/Motivation" in the code, this can be changed if you would like, but to use in it's default setting:

*Create a folder named "Motivation" in "/home/pi/"using 

  mkdir -m 777 Motivation 

while in "/home/pi/"

*copy motivation.py to "/home/pi/" or

  sudo nano motivation.py

and copy/paste code

*Run at Startup
We want the script to run at launch so we create a cron job by typing

  sudo crontab -e

'sudo' gives us the admin cron

add:

  @reboot python /home/pi/motivation.py &

This tells Cron that every boot (or reboot or start-up) we want to run Python with the script MyScript.py. The “&” at the end of the line means the command is run in the background and it won’t stop the system booting up as before.

"/home/pi/Motivation"

This folder is where you house your audio recordings.

I tend to access this folder via sftp as it's ready to go with stock Raspbian
Copying any files to this folder adds them to the potential lsit of files played. 

I used GPIO 18, you can feel free to adjust the code to your liking. 

The button should have a 10k Pull Up Resistor.

CURRENT ISSUES:

NONE THE FUCKER WORKS

NEXT STEPS:

At some point i want to integrate the LEDs. For now they are going to run separate with an arduino or ws2811 controller. 
