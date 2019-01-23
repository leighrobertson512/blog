Title: NFES Winter Session
Date: 2015-03-24
Category: Classes
Tags: computer science, led, gemma, arduino, coding
Author: Wray Mills
Summary: Follow up on the LED pendant projects

### Thank you!

I want to pass on my enthusiastic thanks for letting us provide
Technology Enrichment to NFES! Joe and I thoroughly enjoyed the kids
and the class and look forward to providing more enrichment at
NFES. [Let us know](mailto:info@techemstudios.com?subject=NFES-feecback)
if you (and your kids) have any additional feedback for us.

### LED Pendant Information

Here is some more information about the LED pendants your kids coded
for our class.

The pendant consists of three main parts: the 8x8 LED matrix display;
a microcontroller (it's actually a ["Gemma" microcontroller from
Adafruit](https://www.adafruit.com/products/1222)); and the lithium polymar ([lipo](https://www.adafruit.com/products/1578)) rechargeable battery. There
is no "on/off" switch -- you simply plug the battery in to start the
display and unplug to stop. The battery plugs into the bottom of the
microcontroller in the off-white receptacle.

![Gemma battery socket]({filename}/images/gemma-battery.jpg)

On the top of the microcontroller is a mini USB receptacle which is
used to transfer the code to the microcontroller (any USB connector
will work to connect a laptop/desktop to the
microcontroller). However, this plug does not charge the battery. See
the section below if you and your kid would like to get the software
necessary to refine their code or re-code their LED.

![Gemma mini usb socket]({filename}/images/gemma-usb.jpg)

Your child should also have a very [small charger](https://www.adafruit.com/products/1304) for the battery. This
charger plugs into a USB port and will charge the lipo battery. There
is a red light when charging and a green light that indicates the
battery is fully charged.


### LED Coding information

There are detailed tutorials available at adafruit if you would like
to know how we constructed the pendant and all the component
specifications. However, this is a quick overview to get your child
(re)coding the LED frame designs:

* Download the [Arduino IDE v1.05 with Gemma software](https://learn.adafruit.com/introducing-gemma/setting-up-with-arduino-ide) for your computer or laptop.
* Configure the Arduino IDE to use the Gemma 8MHz and tinyISP.
    * Tools -> Board -> Adafruit Gemma 8MHz
    * Tools -> Programmer -> USBtinyISP
* Download the required
 [LED library](https://github.com/adafruit/TinyWireM/archive/master.zip),
  unzip and put it in the Adafruit Arduino
libraries directory.
    * Put the TinyWireM directory in your Documents/Arduino/libraries directory.
* [Login](https://secure.techemstudios.come/enrolled_children) to our website and download your kid's code.
* Unzip your kid's code into a directory.
* Go into that directory and double-click on the file named for your
kid with a .ino suffix. This will launch Adafruit Arduino.
* The LED design is in the "bmo.h" file that will be automatically
loaded on the second tab when you launch Arduino (for those of you who
have programmed in C or C++ this is simply a header file). Your child
should know how to edit this file to enhance or change their design.
* Anywhere there is a "//" is a code comment and the text after it
    is for explanation and not used in the design.
* Each "frame" of the design consists of 8 lines of 8 1's and 0's
    preceded by a "B" and followed with a ",". Thus, the lines
    correspond to the rows in the matrix and a 1 will light the led at
    that position and a 0 will turn off the led at that position.
* Each frame concludes with a decimal number on the 9th line
      followed by a comma. This decimal number represents the delay in
      hundredths of a second for this frame. For example, if you want
      the first frame to display for half a second, use 50. If you
      want it to display for a whole second, use 100. This value can
      only go up to 255 (a little over 2.5 seconds).
* The file has some statements at the beginning of the file that you
    shouldn't change and the file must conclude with a "};" on the last line.
* Once you are happy with your design, you should compile it to make
sure there are no errors.
* After an error-free compile, plug in your microcontroller and you
have about 10 seconds to click on the "upload" icon (on the top left
of the IDE, there is a right arrow for upload) to transfer the
code to the microcontroller.
* Make sure you are happy with the design -- if you are, you may unplug
  the USB and use the battery to power the microcontroller.
* If you want to change the design again, it is easiest to unplug the
  usb until you have re-compiled the code and plug in when you are
  ready to try again.
* Wait a few seconds for the code to transfer and the microcontroller
to reboot and display the frames in your design.

And, feel free to comment here or shoot us an email if you have ANY
questions or issues.