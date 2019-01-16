Title: LED demo code
Date: 2015-03-03
Category: Notes
Tags: adafruit, arduino
Author: Wray Mills
Summary: Some notes and code

Just dropping in some code for instructors, students, and everyone.


```c
// Animation data for Trinket/Gemma + LED matrix backpack jewelry. 

#define REPS 255 // Number of times to repeat the animation loop (1-255)

const uint8_t PROGMEM anim[] = {

  B11111111, // 1 frame
  B11111111,
  B11111111,
  B11111111,
  B11111111,
  B11111111,
  B11111111,
  B11111111,
  50, // 0.5 second delay
    
  B00000000, // 2 frame
  B00000000,
  B00000000,
  B00000000,
  B00000000,
  B00000000,
  B00000000,
  B00000000,
  50, // 0.5 second delay

  B10010010, // 3 frame
  B01001001,
  B00100100,
  B10010010,
  B01001001,
  B00100100,
  B10010010,
  B01001001,
  25, // 0.25 second delay

  B00100100,
  B10010010,
  B01001001,
  B00100100,
  B10010010,
  B01001001,
  B00100100,
  B10010010,
  25, // 0.25 second delay
  
};

```
