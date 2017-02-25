Title: Adafruit Gemma Musical Notes
Date: 2014-05-29
Category: Notes
Tags: arduino, adafruit, gemma, speaker output
Author: Wray Mills
Summary: Arduino (Gemma) Sketch for musical output

This entry documents my attempt at mapping out some musical notes to be used by students to create their own sounds.

I went ahead and created a header file to define the notes. I based the frequencies on arduino code from this [site](http://arduino.cc/en/Tutorial/Tone), which in turn references this [table](http://www.phy.mtu.edu/~suits/notefreqs.html). Essentially, dividing 1,000 by the frequency.


notes.h
~~~~~~
/*
Note frequencies to be used by the playTone method found in the Adafruit Chirp Owl written by
Becky Stern and T Main.

Created 29 May 2014
by Wray Mills
based on Sound Effects with Arudino - http://www.mycontraption.com/sound-effects-with-and-arduino
These frequencies differ from those provided on the Arduino Tone Tutorial - 
http://arduino.cc/en/Tutorial/Tone and the true note accuracy has not been verified, 
but the relative differences are such that simple melodies can be constructed.
*/
const long note_C = 956;
const long note_D = 851;
const long note_E = 758;
const long note_F = 716;
const long note_G = 638;
const long note_A = 568;
const long note_B = 506;
const long note_hiC = 478;
const long note_hiD = 426;
const long note_hiG = 319;
~~~~~~


You can then use the notes in calls to playTune (provided in the Gemma tutorials) to create music like the Star Wars Theme:

~~~~~~
// Generate the first few measures of the Star Wars Theme
void starwars(){
  playTone(note_D,100);
  delay(50);
  playTone(note_D,100);
  delay(50);
  playTone(note_D,100);
  delay(50);
  playTone(note_G,600);
  delay(50);
  playTone(note_hiD,600);
  delay(50);
  playTone(note_hiC,100);
  delay(50);
  playTone(note_B,100);
  delay(50);
  playTone(note_A,100);
  delay(50);
  playTone(note_hiG,600);
  delay(50);
  playTone(note_hiD,600);

}
~~~~~~

We are prepping for a birthday party -- doing a variation on this [adafruit project](https://learn.adafruit.com/chirping-plush-owl-toy/overview), so I'll post all the different functions we create. Oh, and of course, I'll post the kids creations as well, I can't wait to see what they design.
