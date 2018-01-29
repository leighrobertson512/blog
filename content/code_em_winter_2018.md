Title: Code Em Winter 2018    
Author: Josef Seiler  
Date: 2018-01-09  
category: Classes  
Tags: computer science, coding, github, slack, raspberry pi, technology  
Illustration: raspberry-pi.jpg  

# Day One  

`Week of January 8th, 2018`  

This blog will be used for both the Tuesday and Thursday night class. I will try to clearly show separations between each night where needed.  

## Happy New Year!  

![welcomeoctocat](images/welcometocat.png)  

## What We'll Do  

During this winter session of Code Em we will learn by doing! We will learn new concepts and solidify concepts we have come across before by taking a project-based approach during the twelve weeks. To name a few, project topics can include (not limited to): device building and programming with the [Raspberry Pi](https://www.raspberrypi.org/), robot creations, 3D printing, [Pi Soundboard](http://blog.techemstudios.com/how-to-make-a-raspberry-pi-soundboard.html), Python game design with [Pygame](http://pygame.org/news), web applications, ethical hacking with Pi Zero or [Kali Linux](https://www.kali.org/), Minecraft Modding with Java, Alexa skills, [PiLexa](http://blog.techemstudios.com/make-a-raspberry-pi-powered-alexa.html) and visual-based programming projects like [Scratch](https://scratch.mit.edu/) and [Hopsctoch](https://www.gethopscotch.com/).  

The goal is to have one or several awesome projects by the end of our twelve weeks together. After completing projects, we will make sure we are comfortable enough with the stuff we learn to continue beyond the class.  

While working on projects, students will have the opportunity to gain or expand their knowledge through a variety of programming languages and projects based on experience level, building from visual-based languages to text-based, like Python etc. They will learn source code control, software design, reverse engineering, bug resolution, and coding environments. [^1]  

Whether we work in groups or individually during the weeks, we will always work with someone, i.e. instructors/mentors. To ensure this, we will use two key resources for help and teamwork: [Slack](http://blog.techemstudios.com/slack.html) & [GitHub](https://github.com/); both great tools for team collaboration. Slack is a messaging app and GitHub will serve as a place to save and keep track of all project work. We will use Slack to ask questions and collaborate on projects. We will use GitHub to save all our work to, keep track of projects, as well as help one another to solve any issues. **You will need an accessible email account.** Which bring us to our first assignment!  

## Assignment 1  
Create a new account for [Slack](https://slack.com/) and [GitHub](https://github.com/join?source=header-home) --you will need to verify the email address you sign up with for both. Don't forget your usernames and passwords! Once you have your own Slack and GitHub account, email your usernames to class-info@techemstudios.com or joe@techemstudios.com, so we can add you to the class' Slack team. For those that already have both accounts, just make sure you can log into them! For more direction on joing the team on Slack, check out the intro to slack blog [here](http://blog.techemstudios.com/slack.html).  

<img src="images/slack-logo.jpg" alt="slackin" style="width: 200px;"/> <img src="images/github.jpg" alt="githubin" style="width: 200px;"/>  

Next week, we will narrow down project ideas and get our hands dirty.  

### The Random Number Game  
#### What is Code?  

On Thursday night, we took the random number game we have all played before and put it into a Python program using the chromebooks. Think of *code* or *coding* as a way to represent something, just in a different way. Here, we simply took a real-world game and used Python to represent it. Code is a way for conveying information between people; in this class, between people and machines. Code helps us communicate. You use code everyday without thinking about it, i.e. when you talk with someone, or when you write or read something --speech and text are considered code. So, you have been coding almost all of your life! Throughout class, we'll learn different ways to *code*.  

We briefly talked about the fastest way to guess the correct number in a random number guessing game. We can divide the range of numbers in half on each guess. If the range is between 1 and 100, we can guess 50 first. If 50 is higher than the number picked, we now know the number is between 1 and 50, so we cut the range of possibilities in half! Then we can divide the range further by asking if the number is 25, and so on. This technique is how computers search through an ordered list, **binary search**.  

***  

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

When you begin to write a program, it can seem overwhelming at first. We will learn some techniques in a general software development process and learn how to break up large problems into small parts to tackle them individually. We'll do a deep dive into all the syntax, methods, data types and more, involved with programming languages throughout the session. For now, I'll try to lay out each part of this program in a plain way:  

Looking at the program above...  
`number = random.randint(1, 100)` tells the program to choose a random integer between the range of 1 and 100 and put it into a variable, `number`.  

The next line uses Python's `print()` function. This function tells the program to display to the screen whatever is inside the parentheses. So, when the program is executed, the user understands the computer is *thinking* of a number between 1 and 100.  

`GameRunning = True` is a variable equal to True. We will use this to either end the game or keep playing the game.  

`while GameRunning:` is a loop (something that repeats). Any indented line underneat this will repeat as long as GameRunning is True.  

`guess = int(raw_input("Guess a number between 1-100: "))` Displays to the user what is in between the quotes, pauses the program, and waits for the user to enter an integer.  

The next three *blocks of code* are **conditional statements**. These check whether the user chooses the correct number, a number higher, or a number lower than the random number originally picked. The program will keep waiting for the user to enter a number, until they enter the exact number chosen by the program in the beginning. Then the program will end, because of our condition: **if** the `guess` is exactly equal to `number`, **then** `GameRunning = False`.  

***  

* **Python -** a programming language relatively easy to understand and write.  
* **Variable -** associates a name (variable) to a value (expression), so `<variable> = <expr>`  
* **Loop -** Something that repeats.  
* **Condition -** Tells the program to make a decision based on if something is True or False.  
* **Binary Search -** How a computers searches through an ordered list.  

* **Relational Operators -** Python compares what's on the left to what's on the right; usually used in a condition statement.  

    - Equal to: `==` 
    - Less than: `<`  
    - Greater than: `>`  

Don't worry if this all seems foreign to you (or you feel rusty)! Together, we'll learn by doing and practice, until it becomes second-nature.  


***  

[^1]: [Register.TechEmStudios.com](http://register.techemstudios.com/item/code-em)     

***  


# Day Two    

`Week of January 15th, 2018`  

[MLK Day](https://www.google.com/doodles/martin-luther-king-jr-day-2018)  

## Start Projects  

This week, we started work on a few different goals. As is the case for almost every Tech Em class, there are varying levels of experience. We broke off into groups based on experience level and interest:  

New students (new to Code Em) started work on a *starter* project to create a calculator program in Python with the end goal of using [Turtle graphics](https://docs.python.org/2/library/turtle.html) to *draw* out the result. Students started work on their foundation in computer science and coding with an introduction to coding using the [Python](https://www.python.org/) programming language.  

[Here is a link to the calculator program on GitHub](https://gist.github.com/joetechem/c72df34a62fd416e1a0dc122bffa3335)  

We will be working with Python quite a bit throughout class. It is free and available at [python.org](https://www.python.org/). You can continue to work on this project and/or practice more with Python at home by downloading Python from the link.  

Returning Code Em students grouped up to either work on building a minecraft server on a Raspberry Pi, or started plans for a hands-on hardware project involving the [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/).  

Other students started work on a visual-based coding app, [Scratch](https://scratch.mit.edu/).  

***  

## General Objective Outline    

Every project needs a plan. To ge the most out of each project, each day we will work on following an objective list. Another end-goal for each project is to create an easy-to-follow tutorial on whatever project you are working on. After each project is finished, we will publish these tutorials to the [Tech Em blog page](http://blog.techemstudios.com/) so others can replicate the steps you took!  

Documenting your projects as you work on them will do a few useful things; help you understand what your are doing, keep track of where you are in the process, and help validate your project. The key is to log your work, so that other interested folks can learn what you did by following steps you took to get the same result. Similar to science experiments! --which you may have learned about already.  

***  

## Assignment 2  

Make sure you have a GitHub and Slack account you can log into, and that you have been added to our class Slack Team. If you need help getting on the team, send an email to class-info@techemstudios.com.  

Once on the Slack team, post your first message to break the ice! Post a relevant tech fact or personal experience in the `# code_em` channel (e.g. I have been learning HTML on my own, or I prefer to use an iPad over a laptop, or my basketball team won a game recently, etc.)  

Next week, we'll get started on creating our own GitHub repositories for each group to contribute to.  

Enjoy the snow!!!  

***  

# Day Three  

`week of 01/22/2018`  

## Practice!  

If you do not have access to Python at home, you can download it free from [python.org](https://www.python.org/), or in an internet browser via [PythonAnywhere.com](https://www.pythonanywhere.com/). For either options, you can follow instructions on help setting up your environment to practice at home [here](http://www.allendowney.com/wp/books/think-python-2e/).  

### Project Updates  

* Scratch Project  
    - We continued building our Scratch program portfolio by coding mini interactive games.  

* Python Turtle Calculator    
    - The link to the [GitHub gist](https://gist.github.com/joetechem/e5a213b8d44e8c6ca71fd8224ac64df3). This gist outlines all the steps for the groups working on the Python Turtle Calculator project, completed during class. There are some challenges found here, where the groups from Tuesday and Thursday night can check out for more practice as well. We also took our first steps in learning Version Control via GitHub.  

* Robot Project  
    - We laid out a list of all the materials we need for the project: Pi Zero, pimoroni pHAT, DC motors, wheels, etc. Students create their own sketches of unique design builds. We'll incorporate 3D design and printing for this project  

* Minecraft Pi Server  
    - This group fired up a Raspberry Pi and tested their script setup for a running server. We also tested connecting to the server from other devices; outcome: success! 

All groups continued their documentation of steps taken to help prepare for creation of the project's [README](https://open-source-guide.18f.gov/making-readmes-readable/) and brainstormed their next project endeavour, e.g. website app, minecraft modding, music and sound projects etc.  

***  






