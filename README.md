# MotivationStation
This code supports the MotivatioStation Project. The intent is to create interactive art where individuals can share inspirational and motivational moments.

Ideally someone will walk up to your creation, press a button (or some other interaction) and receive words of positivity, encouragement and inspiration from others.

Recordings are sourced from around the world, with individuals able to record and submit anywhere in the world. 

For more remote locations the recordings can be updated on site, using simple software on Android devices to record, edit and add files to the directory.

This code is built for the Raspberry Pi on Raspbian Lite (Jesse)

*Preparing for install

  sudo apt-get update

  sudo apt-get upgrade

*Wireless AP for uploading recordings

-References:
http://www.novaspirit.com/2015/12/16/raspberry-pi-wifi-hotspot-router-file-share-media-server/
http://www.daveconroy.com/turn-your-raspberry-pi-into-a-wifi-hotspot-with-edimax-nano-usb-ew-7811un-rtl8188cus-chipset/

Remove WPA Supplicant

  sudo apt-get purge wpasupplicant

install dhcp server

  sudo apt-get install isc-dhcp-server



setup dhcp

  sudo nano /etc/dhcp/dhcpd.conf

and add the following:

  subnet 10.10.0.0 netmask 255.255.255.0 {
  range 10.10.0.25 10.10.0.50;
  option domain-name-servers 8.8.4.4;
  option routers 10.10.0.1;
  interface wlan0;
  }

setup hostapd

sudo apt-get install hostapd

  wget http://www.daveconroy.com/wp3/wp-content/uploads/2013/07/hostapd.zip
  unzip hostapd.zip 
  sudo mv /usr/sbin/hostapd /usr/sbin/hostapd.bak
  sudo mv hostapd /usr/sbin/hostapd.edimax 
  sudo ln -sf /usr/sbin/hostapd.edimax /usr/sbin/hostapd 
  sudo chown root.root /usr/sbin/hostapd 
  sudo chmod 755 /usr/sbin/hostapd
  
  
  sudo nano /etc/hostapd/hostapd.conf
  
  interface=wlan0
  driver=rtl871xdrv
  bridge=br0
  ssid=INSERT NAME OF AP HERE
  channel=1
  wmm_enabled=0
  wpa=1
  wpa_passphrase=CHANGE THIS PASSWORD
  wpa_key_mgmt=WPA-PSK
  wpa_pairwise=TKIP
  rsn_pairwise=CCMP
  auth_algs=1
  macaddr_acl=0
  
setup interfaces

  sudo nano /etc/network/interfaces
  
  #looopback adapter
  auto lo
  iface lo inet loopback
  #wired adapter
  iface eth0 inet dhcp
  #wlan
  allow-hotplug wlan0
  iface wlan0 inet static
  address 10.10.0.1
  netmask 255.255.255.0
  
Test for errors

  sudo ifconfig wlan0 10.10.0.1
  sudo /etc/init.d/isc-dhcp-server restart
  sudo hostapd -d /etc/hostapd/hostapd.conf
  
Make wireless AP persistent

  sudo nano /etc/network/interfaces
  
and add the following:
  
  auto wlan0
  iface wlan0 inet static
  address 10.10.0.1
  netmask 255.255.255.0
  
  sudo nano /etc/rc.local  

and add the following:

  hostapd -B /etc/hostapd/hostapd.conf
  iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
  
  sudo nano /etc/sysctl.conf
  
And add the following:

  net.ipv4.ip_forward = 0

*Installing MotivationStation on Pi

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
