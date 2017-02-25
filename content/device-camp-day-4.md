Title: Rpi Temp. and Humidity sensing
Date: 2014-06-19
Category: Notes
Tags: raspberry pi, adafruit, python
Author: Wray Mills
Summary: Some notes and code


Login to your pi and enter some commands:

~~~~~~
sudo apt-get update
sudo apt-get install build-essential python-dev
git clone git://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT
sudo python setup.py install
~~~~~~

Now, we'll look at an example to test reading your sensor from Python.

Once everyone has their sensors working again via Python. Copy in this new mailit.py:

~~~~~~
# Simple smtp mail utility to be used by Tech Em students.
# This will run on the r-pi with the Occidentals install.
# Thus, it is a nice utility to use along with adafruit sensors
#
# Tech Em Studios, Gnu GPL
#
# 201406 Wray Mills
#

import subprocess
import smtplib
import socket

from email.mime.text import MIMEText
import datetime

###
# Change to your settings
###
pi_name = 'your-pi'
to = 'somebody@somewhere.com'

## Feel free to reuse, but please don't abuse the techem student relay
mail_user = 'xxx@techemstudios.com'
mail_password = 'pword'
smtp_server = 'smtp.somwhere.net'
smtp_port = 3535 # Use 587 for gmail

def deliver ( message, subject = 'RPi output' ):
    smtpserver = smtplib.SMTP(smtp_server,smtp_port) # Use 587 for gmail
    smtpserver.ehlo()
    #smtpserver.starttls() # Uncomment this line for gmail
    smtpserver.ehlo
    smtpserver.login(mail_user, mail_password)
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = '(%s)%s' % (pi_name,mail_user)
    msg['To'] = to
    smtpserver.sendmail(mail_user, [to], msg.as_string())
    smtpserver.quit()
~~~~~~

And create a new file called temp_humidity_emailer.py and copy this code into it:

~~~~~~
#
# Template code for emailing temperature and humidity from an Adafruit DHT22
# sensor. Don't forget to update this file if you connect the DHT22 to another data pin,
# want to change the delay, or logic for mailing. For example, you may only want to
# send notifications when certain thresholds are exceeded.
# 
# Code provided for Tech Em students and open under Gnu GPL
#
# Wray Mills
# 20140618
#

import os
import time
import Adafruit_DHT
# Tech Em mail utility
from mailit import *
 
sensor = Adafruit_DHT.DHT22
pin = 4 
 
def read_temp_humidity():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	temp_f = temperature * 9.0 / 5.0 + 32.0
	return temperature, temp_f, humidity
	

deliver('The current temp is %0.2f C, %0.2f F, with a humidty of %0.2f%%' % (read_temp_humidity()))
~~~~~~

Then we'll talk about "cron" and look at how you can setup your pi such that whenever you power it up on a network, it will start sensing temp and humidity every x minutes. Of course, don't forget to adjust your mailit.py in order to configure who gets notified via email or text.

~~~~~~
sudo crontab -e
~~~~~~

Use the nano editor to add a line like this:

~~~~~~
0,15,30,45 * * * * /usr/bin/python /home/pi/temp_humidity_emailer.py >> /home/pi/log/cron.log 2>&1
~~~~~~

To exit, ctrl-x, answer yes and then hit enter.

Don't forget, this is your pi and your code so you should try to modify the code (in temp_humidity_emailer.py) to only send notifications when the temp and/or humidity goes below or above some set levels. Ask me if you want to discuss how to properly create those conditions.

Now, if you want to "permanently" attach your sensor to the board to plug into the top of the pi, let's solder!!

![RPi with DHT22 sensor on top board]({filename}/images/pi-with-dht22.jpg)


