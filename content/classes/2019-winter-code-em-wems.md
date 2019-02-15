Title: WEMS Coding Winter 2019
Date: 2019-02-04
Curriculum: code-em
Class: coding
Session: Winter
Hours:
SectionId: 326
Year: 2019
Tags: computer science, coding, github
Illustration: intel-inside.jpg
Author: Chris Kefalas
Summary: WEMS Coding

# Jump to [Current Lesson](#day-9)

# Description
Students will gain or expand their coding knowledge through a variety of programming languages and projects based on experience level, building from visual-based languages to Python. They will apply practical computer science skills such as source code control, software design, reverse engineering, bug resolution, and coding environments.

# Instructors
## Lead Instructor
Chris Kefalas

# Class Session Learning Objectives

 * All students have a GitHub account and understand basic GitHub concepts of clone, pull, commit and push.
 * All students can create and run a Python program on their own.
 * All students understand design thinking and how to apply to planning software.
 * All students know how to examine simple programs to understand how they work and how to alter.
 * All students know how to deal with runtime errors and how to resolve.
 * All students know the different tools needed for coding -- editors, interpreters and execution (runtime).
 * All students create CLI program(s).
 * Repeat students know how to branch and PR in GitHub.
 * Repeat students will complete an appropriate level assignment.
 
# Materials

# Class References
 
# On the line Resources

 * [Techem Github!](https://github.com/techemstudios)

## On the line Presentations

## Repos
 * [MyFirstWebsite](https://github.com/techemstudios/MyFirstWebsite)

## Related Blog Notes
 * [Github Part One](/github-part-one.html)
 * [Github Part Two](/github-part-two.html)

## (GitHub) Assignments

## External References

# Previous Classes
The summary of [our previous classes]({filename}/class-reflections/2019-winter-code-em-wems-summaries.md).

# Day 6
## GitHub - your online portfolio
We'll discuss GitHub, what it is and create an account.

The students will setup their GitHub account. We'll cover how GitHub is also a public/social place and therefore our "Internet Safety" rules apply to GitHub as well. Also, because GitHub can become a digital portfolio that is used by future schools and employers during an application process, it is actually even more important to maintain a serious presence on GitHub since it is a real-time personal resume.

![Git it?](images/github_screenshots/one.jpg)

## Out of Desk
Using physical paper and file folders, our class activity will be a real-world analogy for GitHub. GitHub maintains all versions of the document (or code) you are editing -- for the activity the "GitHub" person will hold on to many file folders (a *repository*), each one representing previous versions with the one on top being the most recent.

When a student wants to edit the latest, she requests the latest from "GitHub", who will actually present a COPY of the latest for the student to edit.

She takes the paper from the folder and makes some edits.

She puts the paper back in the folder, *committing* those changes to her copy of the folder.

She then hands the folder back to "GitHub", *pushing* those changes so that they can be included in the latest version of the folder.


## Hands-On/coding
Using a prepared GitHub repository, students will use the GitHub web editor to make changes to a website. Since GitHub also supports the publishing of websites, the students can immediately make see their changes on a live website. Their take-away from this class is a live website they can edit!

## One thing to remember
GitHub is your online Digital Portfolio.

## Setup
Create a repo with gh-pages turned on (pointing to /docs). Add a simple HTML/CSS website for the students to edit. We can go ahead and use a custom domain like wems.techemstudios.com to make it easier for the students/parents to access.

## Actual
This is the
[play by play]({filename}/class-reflections/2019-winter-code-em-wems-day6.md) for day 6!

# Day 7
## Cloud9 - Coding in the Clouds
The students will do some text-based programming using the Python programming language. They will be using Python in an environment they can access from anywhere (with an Internet connection and browser) -- an environment aptly named Cloud9.

![Py in the clouds](images/py-clouds.jpg)

## Out of Desk
Starting with a discussion about the origin of the term "Cloud 9", we'll discuss how coding today is actually quite different than it was even 5 years ago. There are more computing services available "on the cloud" while the speed and availability of the Internet has increased. So, using students to represents "computers in the cloud", we can act out how we will be accessing "desktops" in the cloud to do our work.

## Hands-On/coding
Each student will have his/her own Cloud9 environment. They will each use a separate Tech Em AWS (Amazon Web Services) login to access this environment -- a virtual desktop loaded with everything they need to code in Python (and many other languages), pre-configured so we can focus on learning the language and typing programs. Initially, they need to get used to accessing a code editor and a computer console in their browser. They will learn how to create new Python files, run them, and even learn what to do when there are errors.

[//]: # (write, edit what Python code? I suggest you focus on a simple piece of code -- not even sure you want to talk about cloning since that happens in the terminal and may be a lot to handle. I would suggest you focus more on code editors and what cloud9 is, an editor in the cloud, and how it is like having their own laptop in the cloud, etc. It will take some time for them to learn how to work in that environment and create files and use the runner. I do think the focus should be on the coding and debugging. If they don't know some basic coding terms, you'll need to cover that. Some objectives would be some coding terms, relate back to lightbot and/or math: literals, operators, expressions, variables, assignment, statements, functions, just calling them at this point. And to drive it back home -- focused, one thing to remember: How to create a python module, program file and run it. Then pick back up with GitHub the following week. By that time, we can brainstorm on a way that better ties the cloud9 python and the github website.)

## One thing to remember
They should know how to create a Python file and run it (in their environment) -- *coding is bliss in the cloud*.

## Setup
Prior to class, we created each student's Cloud9 environment. In doing so we also create them an AWS (Amazon Web Services) login in the Tech Em account. They will have a username and a beginning default password along with a unique link to their Cloud9 environment. The first time they access their environment they will need to provide their username and password and immediately change their password.

## Actual
As was to be expected, one of the biggest challenges here is "traditional" typing. The students were using our Chromebooks to access Cloud 9. So, while the Chromebooks and Wi-Fi held up nicely, lots of typing on a traditional keyboard can be a challenge. We are often seeing students who can likely type faster using a phone-thumb input than a full-sized qwerty keyboard. We imagine computer input will evolve and for now (much as it evolved from separate keypunch operators to programmings typing in their own code), For now, typing without touchscreen input is an area where programming is like a musical instrument or sport and the key is practice, practice, practice.

# Day 8
## GitHub + Cloud9
Different clouds working together. Now we have a "laptop in the cloud" with its own set of folders -- we will learn how to "git" our code from the GitHub cloud onto our Cloud9 environment. Students will explore how to *commit*, *push* and *pull* their changes from Cloud9 to/from GitHub.

![Git it?](images/github-repos-flow.jpg)

## Out of Desk
We will revisit the GitHub activity with a new twist, err, umm. cloud. We have a new player now, Cloud9. This player is not all that different than using a desktop or laptop and Git. We'll continue with the students acting as themselves, Cloud9 and GitHub to pass along documents (code) in folders in order to continue providing that physical representation of all this virtual activity!

## Hands-On/coding
Students will go back to the Website HTML -- this time, in their Cloud9 environment. They will use the same editing skills from last week and add some new skills to *pull* (update) the code from GitHub to Cloud9; *commit* their code in their Cloud9 environment and then *push* that new code to Cloud9. The "latest in wins" game from 2 weeks ago will continue, but with a twist. Their *pushes* will be blocked if they don't have the most recent code. This is intended to drive home the fact that GitHub maintains the primary repository for their code; each of their Cloud9 environments has a copy of what is in GitHub and it is actually up to them to keep their copy up-to-date.

The passive intent here is to have students experience the issues a team has working on "the same document" at the same time. We will come back to that in future classes to discuss how team organization and additional Git capabilities can be used together to overcome these issues.

## One thing to remember
A pull a day keeps the conflicts away!

## Setup
For Day 7 setup, the Cloud9 environments that were setup included a copy (clone) of the website repo. Therefore, students will already have that code available. They'll need to immediately *pull* from the repo as a start to this lesson.

## Actual
Lots of typing, but the students are getting used to coding in a "text-based" environment while also using a text-based command-line interface as part of a development workflow.

<h1><a name="day-9">Day 9</a></h1>
## Cloud9 + Python
We will go back to coding in the clouds. Practice makes perfect and we want to ensure the students remember how to access their coding environment and create their own Python files so they can practice coding at home. They'll work more on running and debugging within the cloud environment. And finally, they'll do a `git pull` to grab some python _web app_ code we have ready for them to test.

![Python!](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## Out of Desk
This time, it is up to the students to explain to us all the different sites we use in the cloud and how they fit together. Where is GitHub? Where is Cloud9? Where is the chromebook? We can use this as an opportunity to introduce the concept of a computer process so we can talk a bit more specifically about each process and where that process is running (_locally_ on their chromebook, in the cloud in AWS or in the cloud on GitHub).

## Hands-On/coding
Students will follow along while we create another Python file, edit it and run it. We'll review some basic Python terms and syntax: literals, expressions and statements. We'll review code blocks and how they are delineated in Python. Then we'll review conditions, conditional blocks as well as functions and function definition blocks.

## One thing to remember
``` python
if True:
  print("Python is great!")
```

## Setup
For Day 9 setup, they'll need to get back on their Cloud9 environment and *pull* from the MyFirstWebstie repo to make sure they are in sync.

## Actual
Overall it went pretty well, still our biggest slow down is getting everyone signed in. Cloud9 and really any IDE has been a little bit overwhelming for kids with all the buttons, and options, and areas that it has information. But we have tried to focus soley on the File Manager to the left, the Terminal along the bottom, and the text editor in the middle. I don't think most of them have really grasped what is happening with regards to a Python file, and a website. We could probably take a step back, and do a little bit of an easier Python exercise in Cloud9 before doing the dynamic website. Maybe I will try signing in the laptops before hand so that when we get there we can just jump right to the code. The logging in process doesn't bring as much entertainment as I'd hoped it would, and we keep forgetting our passwords.

I'm not concerned though! I think that after next week they will all feel much more comfortable in Cloud9, and we can start really focusing on the code. I think the process is a bit distracting right now, and not as fun. But once they get it down, it's EZ PZ. We will all just use the same password for now though to limit difficulty on that front.
