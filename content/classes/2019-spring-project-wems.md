Title: WEMS Project Summer 2019
Date: 2019-02-17
Curriculum: make-em
Class: projects
Session: Spring
Hours:
SectionId:
Year: 2019
Tags: computer science, github, raspberry pi
Illustration: intel-inside.jpg
Author: Wray Mills
Summary: WEMS Projects
Status: draft

# Description
Students will collaborate to design and create a group project to be placed on display.

February 21st to May 2 (9 sessions)

# Instructors

## Lead Instructor
Chris Kefalas

# Class Session Learning Objectives

 * All students understand design thinking and how to apply to planning software.
 * All students know how to examine simple programs to understand how they work and how to alter.
 * All students know how to deal with runtime errors and how to resolve.
 * All students know the different tools needed for coding -- editors, interpreters and execution (runtime).
 * All students create CLI program(s).
 * All students learn how to work on a join project.
 * All students learn how to run Python programs on a Raspberry Pi
 * All students learn how a basic chat bot (on slack) works
 * All students learn about led (output) and temp/humidity (input) on a device

# Day by Day High Level Plan

Planning for 8 days. Last day can be final project wrap-up etc. if needed.

 - cloud9 basic python programs (continuation from code em)
 - python programs (CLI) and make sure kids are on student slack
 - very high level CI (intro to Travis)
 - very high level shared/open python libraries (intro to PyPy)
 - raspberry pi … run code on the py via pypy
 - raspberry pi … leds and temp humidity
 - slackbot
 - slackbot plus led/temp code


# Materials

 * Class raspberry pi
 * Student Slack Account
 * AWS Cloud9 accounts

# Class References
 
# On the line Resources

 * [MyFirstWebsite Repo](https://github.com/techemstudios/MyFirstWebsite)
 * [Techem Github!](https://github.com/techemstudios)

## On the line Presentations

## Repos

 * [MyFirstWebsite Repo](https://github.com/techemstudios/MyFirstWebsite)

## Related Blog Notes
 <!--* [Github Part One](/github-part-one.html)-->
 <!--* [Github Part Two](/github-part-two.html)-->

## (GitHub) Assignments

* [Homework Assignment #1](https://github.com/techemstudios/MyFirstWebsite/blob/master/homework/my-first-assignment.md)

## External References

# Day 1

## Topic - Raspberry Pi & Clouds

Class will start with students recieving a piece of paper with their login information. Using Chromebooks they will navigate to http://wems.techemstudios.com and using the proper user name and class password will log into their accounts. Once their Cloud9 workspace has loaded, they will open a Terminal and <code>git pull</code>. As a class we will go through the README.md and briefly discuss the plan for the next couple weeks. The remainder of class will consist of working through a couple small Python programs, running them, and making changes. This should put us in a good position for what is planned next week.

## Out of Desk - Laptop In The Clouds

Moving over to the _multi-purpose area_ we will use human repositories and paper folders to reanact the life cycle of our code as it travels through the Clouds of the Internet and into it's proper home on Github. As our code travels through the wire, at each stop we will go over the different <code>git</code> commands that are required to get us to the next step. 

- <code>git pull</code>
- <code>git add</code>
- <code>git commit -m "A Commit Message"</code>
- <code>git push</code>
- <code>git status</code>

## Hands-On/coding

Using the Chromebooks students will log into their AWS Cloud9 editor, and start with opening a Terminal. They will issue the command <code>cd MyFirstWebsite</code> and press the *ENTER* key. Next they will type in <code>git pull</code>, they should spend some time quickly reading the output of that command to see if it worked correctly. One way to check if the command has been successful is by see if they have a new folder called *python-exercises*. If they see that folder, they are ready to type <code>cd python-exercises</code> into the Terminal. Finally, using the mouse they should click open the folder, and open the file called *START-HERE.py*. 

## One thing to remember

Students should leave class with a good understanding of what our _beginning of class_ routine is, and the basic things that we do in Cloud9 like open, save, create a file. As well as how we run, and debug our Python programs. 

_Beginning of Class_ routine:
    - Navigate with the Chrome browser to *http://wems.techemstudios.com*
    - Find your name on the list of AUTHORIZED USERS and click the link to open your AWS Cloud9 login web page.
    - Type in your username and class password, then click the login button. 
    - If the Cloud9 editor doesn't load when you click login, look for a *Services* button at the top of the web page, after clicking it you should see a link for *Cloud 9*

## Setup

- Student username and login paper printed output
- Eight _fully charged_ Chromebooks, always one extra in case of chaos
- One teacher laptop for example and instruction
- One whiteboard for writing commands, and Python syntax


## Actual

We are totally making some progress on AWS Cloud9, using a classroom password, and putting the Chrome web browser into _incognito_ mode has made the beginning routine a bit quicker. Still a bit of confusion with the file manager in Cloud 9, and navigating around via the Terminal. But I'm confident with practice each week they will have no problem picking it up. **Homework Assignment #1** was sent home with students, it simply asks them to make an attempt to log into their Cloud 9 _Laptop in the Clouds_ from home. also talk to their parents about an e-mail address that we can use for Slack, our classroom code collaboration software. 

