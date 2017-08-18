Title: How to make a Raspberry Pi Soundboard
Author: Alex Noll
Date: 2017-08-10
category: Notes
Tags: computer science, raspberry pi, hardware, wiring

***

### How to Setup a Soundboard

For this tutorial, you'll need a Raspberry Pi, Breadboard, bunches of cables and buttons, and an output speaker (through HDMI or the 3.5mm output). Once you have everything, you're good to go. You'll have a lot of code to input, but you can also find the code here: [http://cdn.makezine.com/make/33/soundboard.py](http://cdn.makezine.com/make/33/soundboard.py)

as for the many lines of code...

```bash
 import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

sndA = pygame.mixer.Sound(".wav")
sndB = pygame.mixer.Sound(".wav")
sndC = pygame.mixer.Sound(".wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print "Sampler Ready."

while True:
   try:
      if (GPIO.input(23) == True):
         soundChannelA.play(sndA)
      if (GPIO.input(24) == True):
         soundChannelB.play(sndB)
      if (GPIO.input(25) == True):
         soundChannelC.play(sndC)
      sleep(.01)
   except KeyboardInterrupt:
      exit()
      ```

After putting the code into a text editor, you'll need to get some .wav files to have play each time you hit a button, one place for some funny .wav files is: [http://cdn.makezine.com/make/33/pd_sound_effects.zip](http://cdn.makezine.com/make/33/pd_sound_effects.zip). After downloading, or creating you own .wav files, just put their file names on lines 13, 14, & 15. After completing these steps, you have some wiring to do.

![wiring](images/wiring.jpg)

In the diagram shown, no breakout boards were used, but you can see the positive coming off of the 3v3 pin to the positive rail of the breadboard. After the positive, you'll need a ground, in the diagram, it's the 3rd pin on the right. Now you'll want to place down all of your buttons. After placing down all of your buttons, you'll need a positive from the positive rail connect to each button at the top pin of the button. After connecting the positives for each button, you'll need the GPIO cables for each button, as well as a 10K resistor, both of which are connected to the bottom pin of the button. The resistors have to connect to the negative rail, while the GPIO cables connect to pins 23, 24, and 25. After wiring everything up, you can return to the Terminal.

![our wiring](images/IMG_0547.JPG)

You need to make sure to have all of your .WAV files and your .py file all in the same folder, preferably on your desktop. For this tutorial, we named our folder "soundboard", in the Terminal, you'll need to change your directory to the Desktop, and then to your folder, using: ```cd Desktop``` and ```cd soundboard```, after this, run ``` sudo python soundboard.py```. After running, wait until your Terminal says Sampler Ready and then you're good to go!

![Sampler Ready](images/IMG_0551.JPG)

---
