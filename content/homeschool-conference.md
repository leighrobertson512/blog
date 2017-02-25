Title: Homeschool Conference (201503)
Date: 2015-03-24
Category: Notes
Tags: computer science, binary, python, raspberry pi, adafruit, gemma, lightbot
Author: Wray
Summary: Highlights from my presentation

Since I covered a bunch of stuff, here are some of the references
and high points from my talk: "Technology in your Homeschool Curriculum"

![Homeschool Student working on code for microcontroller]({filename}/images/hs-talk-40.jpg)

### The links

* [Code.org](http://code.org)
* [Circuit Coder](https://itunes.apple.com/us/app/circuit-coder/id492180472)
* [Lightbot](http://lightbot.com)
* [Scratch](http://scratch.mit.edu)
* [Hopscotch](https://www.gethopscotch.com)
* [Pythonista](http://omz-software.com/pythonista/)
* [GamePress](http://www.gamepressapp.com)
* [Floors](http://www.projectpixelpress.com/floors/)
* [Adafruit](http://www.adafruit.com)
* [RaspberryPi](http://www.raspberrypi.org)

### History

* Prehistoric: Tally Sticks
* 1800's, mechanical: Pascal's Calculator, Arithmometer, Babbage's
* Machines, Ada Lovelace
* 1940's, vacuum tube: ENIAC
* 1970' to today: microchip and the raspberry pi

#### ENIAC vs. Raspberry Pi

![ENIAC vs. Raspberry Pi]({filename}/images/hs-talk-11.jpg)

### Binary Logic
What can one do with billions of transistors?

Start with one transistor, simple switching device (digital). It's on
or off, true or false, 0 or 1. Wire a couple together and you get an
AND gate.

![AND Gate]({filename}/images/hs-talk-15.jpg)

Combine a NOT gate and an AND gate and you can solve the
truth table where you want the output to be true (1) only when B
is 1. That is to say: let there be truth when (NOT A) AND B.

!["Quarter" Adder]({filename}/images/hs-talk-18.jpg)

So, if you wire the A input to a NOT gate and have that go into an AND gate that
B is also wired to, then you have the result. Suppose you now want to add A
and B, then simply use the mirror of (NOT A) AND B and "OR" it: ((NOT A)
AND B) OR (A AND (NOT B)). That gives you the sum, but don't forget
the carry which is simply A AND B.

![Half adder truth table]({filename}/images/hs-talk-19.jpg)
![Half adder circuit]({filename}/images/hs-talk-21.jpg)
![Half adder running circuit]({filename}/images/hs-talk-22.jpg)

Now you have a binary half adder (you can add two digits). Combine two
of those (along with an OR of the CARRY output for each) and you have
a full adder. String together 3 full adders and you can add two 3
digit binary numbers!

![Binary addition]({filename}/images/hs-talk-27.jpg)
![Binary adder circuit]({filename}/images/hs-talk-28.jpg)
![Binary adder running circuit]({filename}/images/hs-talk-29.jpg)

Wasn't that easy??


### Coding

Having gone through lightbot, a teacher can re-iterate the
fundamentals with a language like Python: procedures, overloading,
loops, and conditionals. Futhermore, with concepts learned in Scratch,
Hopscotch, and even game-creation apps like GamePress, variables of
varying data-types can be explained. Start with a simple program to
emulate "Mad Libs" and work up to more complex programs that can
leverage device (pythonista) libraries for accelerometer or screen
input; leverage minecraft (Bukkit server) libraries to build things in
a Minecraft world; leverage GPIO libraries to read sensor input/update
led output from a raspberry pi cobbler kit.


![Make it... Fun]({filename}/images/hs-talk-46.jpg)

This BMO-creeper contains a student coded microcontroller, not TNT.

![BMO-Creeper]({filename}/images/hs-talk-41.jpg)






 
