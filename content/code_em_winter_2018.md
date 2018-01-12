Title: Code Em Winter 2018    
Author: Josef Seiler  
Date: 2018-01-09  
category: Classes  
Tags: computer science, coding, github, slack, raspberry pi, technology  
Illustration: raspberry-pi.jpg  

## Day One  

`Week of January 8th, 2018`  

This blog will be used for both the Tuesday and Thursday night class. I will try to clearly show separations between each night where needed.  

### Happy New Year!  

During this winter session of Code Em we will learn by doing! We will learn new concepts and solidify concepts we have come across before by taking a project-based approach during the twelve weeks. To name a few, project topics can include (not limited to): device building and programming with the [Raspberry Pi](https://www.raspberrypi.org/), robot creations, 3D printing, [Pi Soundboard](http://blog.techemstudios.com/how-to-make-a-raspberry-pi-soundboard.html), Python game design with [Pygame](http://pygame.org/news), web applications, ethical hacking with Pi Zero or [Kali Linux](https://www.kali.org/), Minecraft Modding with Java, Alexa skills, [PiLexa](http://blog.techemstudios.com/make-a-raspberry-pi-powered-alexa.html) and visual-based programming projects like [Scratch](https://scratch.mit.edu/) and [Hopsctoch](https://www.gethopscotch.com/).  

The goal is to have one or several awesome projects by the end of our twelve weeks together. After completing projects, we will make sure we are comfortable enough with the stuff we learn to continue beyond the class.  

While working on projects, students will have the opportunity to gain or expand their knowledge through a variety of programming languages and projects based on experience level, building from visual-based languages to text-based, like Python etc. They will learn source code control, software design, reverse engineering, bug resolution, and coding environments. [^1]  

Whether we work in groups or individually during the weeks, we will always work with someone, i.e. instructors/mentors. To ensure this, we will use two key resources for help and teamwork: [Slack](http://blog.techemstudios.com/slack.html) & [GitHub](https://github.com/); both great tools for team collaboration. Slack is a messaging app and GitHub will serve as a place to save and keep track of all project work. We will use Slack to ask questions and collaborate on projects. We will use GitHub to save all our work to, keep track of projects, as well as help one another to solve any issues. **You will need an accessible email account.** Which bring us to our first assignment!  

### Assignment 1  
Create a new account for [Slack](https://slack.com/) and [GitHub](https://github.com/join?source=header-home) --you will need to verify the email address you sign up with for both. Don't forget your usernames and passwords! Once you have your own Slack and GitHub account, email your usernames to class-info@techemstudios.com or joe@techemstudios.com, so we can add you to the class' Slack team. For those that already have both accounts, just make sure you can log into them! For more direction on joing the team on Slack, check out the intro to slack blog [here](http://blog.techemstudios.com/slack.html).  

Next week, we will narrow down project ideas and get our hands dirty.  

## Random Number Game  

On Thursday night, we took the random number game we have all played before and put it into a Python program using the chromebooks. Think of *code* or *coding* as a way to represent one thing, just in a different way. Here, we simply took a real-world game and used Python to represent it.  

We briefly talked about the fastest way to guess the correct, by dividing the range of numbers in half on each guess. If the range is between 1 and 100, we can guess 50 first. If 50 is higher than the number picked, we now know the number is between 1 and 50, so we cut the range of possibilities in half! Then we can divide the range further by asking if the number is 25, and so on. This technique is how computers search through an ordered list, **binary search**.  

```python  
import random

number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
GameRunning = True

while GameRunning:
    guess = int(raw_input("Guess a number between 1-100: "))

    if guess == number:
        GameRunning = False
        print("You guessed correctly!")
        
    elif guess > number:
        GameRunning = True
        print("Your guess was too high!")
        
    elif guess < number:
        GameRunning = True
        print("Your guess was too low!")
```  

When you begin to write a program, it can seem overwhelming at first. We will get used to breaking up problems into small parts, and tackle them individually. We'll do a deep dive into all the syntax, methods, data types etc. involved with programming languages throughout the session. For now, I'll try to lay out each part of the program in a plain way:  

Looking at the program above...  
`number = random.randint(1, 100)` tells the program to choose a random integer between the range of 1 and 100 and put it into a variable, `number`.  
The next line uses Python's `print()` function. This function tells the program to display to the screen whatever is inside the parentheses. So, when the program is executed, the user understands the computer is *thinking* of a number between 1 and 100.  
`GameRunning = True` is a variable equal to True. We will use this to either end the game or keep playing the game.  
`while GameRunning:` is a loop (something that repeats). Any indented line underneat this will repeat as long as GameRunning is True.  
`guess = int(raw_input("Guess a number between 1-100: "))` Displays to the user what is in between the quotes, pauses the program, and waits for the user to enter an integer.  

The next three *blocks of code* are **conditional statements**. These check whether the user chooses the correct number, a number higher, or a number lower than the random number originally picked. The program will keep waiting for the user to enter a number, until they enter the exact number chosen by the program in the beginning. Then the program will end, because of our condition: **if** the `guess` is exactly equal to `number`, **then** `GameRunning = False`.  

**Python -** a programming language relatively easy to understand and write.  
**Variable -** associates a name (variable) to a value (expression), so `<variable> = <expr>`  
**Loop -** Something that repeats.  
**Condition -** Tells the program to make a decision based on if something is True or False.  
**Binary Search -** How a computers searches through an ordered list.  

**Relational Operators -** Python compares what's on the left to what's on the right, usually used in a condition statement. Below is a table of the operators found in Python we used tonight:  

|   Python  |    Mathematics   |    Meaning  |
|-----------|------------------|-------------|
|   <       |       <          | Less than   |
|   >       |       >          | Greater than|
|   ==      |       =          | Equal to    |  

***  

[^1]: http://register.techemstudios.com/item/code-em   
