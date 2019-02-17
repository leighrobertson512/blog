Title: Studio Code Em Padawans Winter 2019
Date: 2019-02-18
Curriculum: code-em
Class: studio-code-em
Session: Winter
Hours:
SectionId:
Year: 2019
Tags: computer science, coding, github, slack, raspberry pi, technology  
Illustration: raspberry-pi.jpg  
Author: Wray Mills  
Summary: Studio Code Em Class

# Jump to [Current Lesson](#current)

# Description

12-week Session
Tuesdays, February 5 - April 30, 6:30-7:30pm
(no class April 2)

Students will gain or expand their coding knowledge through a variety of programming languages and projects based on experience level, building from visual-based languages to Python. They will apply practical computer science skills such as source code control, software design, reverse engineering, bug resolution, and coding environments.

# Instructors

## Lead Instructor
Wray Mills
## Youngling's Instructor
Chris Kefalas
## Padawan's Instructor
Wray Mills
## Additional Interns/Instructors
Alex Noll

# Pre-Requisites
The Padawan section requires previous Code Em experience including these concepts:

 * Binary Number System
 * Boolean Logic
 * Python programming: conditionals, loops, functions and Classes
 * Introduction to Git
 * Introduction to Linux
 * Device Engineering
 
This class will require 2+ hours of time outside the class. Several sessions will be flipped -- students will be given an assignment to review online (lecture) materials before the next class so that we can spend the time in class actually applying the concepts correctly.

# Learning Objectives

 * GitHub account and understand basic GitHub concepts of clone, pull, commit and push.
 * Can create and run a Python program on their own.
 * Understand design thinking and how to apply to planning software.
 * Know how to examine simple programs to understand how they work and how to alter.
 * Know how to deal with runtime errors and how to resolve.
 * Know the different tools needed for coding -- editors, interpreters and execution (runtime).
 * Create CLI program(s).
 * Know how to branch and PR in GitHub.
 * Complete an appropriate level assignment.
 * Work in Cloud9
 * Work in Jupyter notebooks

# Day by Day Topics

  * Review Hardware and Software
    * Leave with GitHub and Cloud9 config
  * Flipped - (Python) Programming terms
    * In class assignment
  * Flipped - (Python) Data Structures and intro to Jupyter.
    * In class assignment
  * Flipped - Boolean logic
    * In class assignment (Python coded full adder)
  * Flipped - Using (Python) Data structures
    * In class assignment
  * Python on a device -- packaging and deployment
  * Come to class with project ideas
    * Design Thinking project design
  * Flipped Jupyter Notebooks
    * In class assignment
  * Project -- Finalize scope
  * Project -- Demo 1
  * Project -- Demo 2
  * Project -- Final Demo
    * Presentation and blog write up

# Materials
Students should bring their own laptops if possible.
Students should have access to a Cloud9 capable browser outside of class.

# On the line Resources

## On the line Presentations
* [Intro to Code without notes](decks/intro-to-code.html)

## Repos

## Related Blog Notes

## (GitHub) Assignments

## External References

# Day 1
## Computer Science Review
Tubes to Gates, Ada to Python, what do you remember?

## Out of Desk
Whiteboard truth tables.

## Hands On
Setup with access to this blog, slack, GitHub and Cloud9 environment created.

## One Thing to Remember
Writing code that other humans can understand is pretty much the point of programming languages.

## Assignment
Flipping next class, so review [this](decks/intro-to-code.html) before the next class. This
presentation does not include the notes -- see if you remember the
terms and look them up if necessary. Fire up the Python interpreter if
needed to remember lists, tuples, classes and functions (methods).

## Setup
Cloud9 environments.

## Actual
We started off reviewing this blog and its purpose during this session -- the intent being that we use class time to "code" while we are together to help get students "unstuck". We quickly went through the review -- great recollection of Python programming basics and navigating within the Cloud9 environment. We got new AWS IAM accounts setup and Cloud9 environments.
We'll need to work through some assignments that reinforce earlier binary number system and boolean algebra learnings! We were a little rusty there, but eventually remembered the primary gates and that they can be used to perform mathematical operations. We used paper instead of the whiteboard.

# Day 2
## Diagram your Code
It is like English class, but your prose is code.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Peternaur.JPG/90px-Peternaur.JPG" width="90" height="120">

## Out of Desk
Musical Pair Programming. Starting with a base sketch of a program on paper, students will swap the paper to finish the challenge. Part of the challenge will be to label the code with the terms reviewed in the assignment deck.

## Hands On
We'll work on the challenge to only use boolean operators to perform mathematical operations. This challenge will include methods for `half_adder` and `full_adder`. And we'll also use this to introduce some unit testing concepts. In fact, since we started working some on the challenge to add numbers without use `+`, we are going to stop all that coding to write our tests first!

## One Thing to Remember
The sum of A + B = (not A and B) or (A and not B)

## Assignment
Data Structures with a focus on Classes -- the GitHub assignent link is in the class slack channel.

## Setup
Musical Code worksheet and tests for full/half adder. GitHub Classroom data assignment.

## Actual
We actually jumped around a lot to make sure everyone: 1) is following this blog, 2) has access to slack, 3) can get back on their Cloud9, 4) can run Python code on Cloud9 and 5) can run a Jupyter Notebook server on Cloud9. And we got all this done while also reviewing terms and discussing the binary adder challenge and prepping for this week's assignment which will be posted here soon! We discussed test driven development and I proposed starting with this test for the final binary adder function:

```python
import unittest

from binary_adder import *

class TestAdder(unittest.TestCase):

    def test_adder(self):
        ''' Test a binary_adder function.
        
        Add two binary digits (input as strings). The solution must not use the '+' operator.
        
        '''
        
        self.assertEqual(binary_adder('1','1'),'10')
        self.assertEqual(binary_adder('101','1010'),'1111')
        self.assertEqual(binary_adder('1101','11100101010'),str(bin(0b1101 + 0b11100101010)[2:]))

if __name__ == '__main__':
    unittest.main()
```

As part of the challenge you should add tests for your `half_adder(a,b)` and your `full_adder(carry_in, a, b)`. Next time we'll discuss the difference between black box testing and clear box testing -- what type of test the above is and why this challenge also needs a clear box text.

<h1><a name="current">Day 3</a></h1>

## Data
What is it good for? Absolutely everything!

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Collegiate_Dictionary.jpg/1024px-Collegiate_Dictionary.jpg" width="200">

## Out of Desk
Back to the books: dictionaries and indexes. Python dictionaries and keys are rooted in real-world books. We'll take some time to revisit physical books to reinforce programming language data structure terms.

## Hands On
We'll continue work on the Elementary Data 1 assignment in class. If the students get through the basic assignment, they can create unit tests to verify their solutions!

## One Thing to Consider
Is a 3D dictionary an actual Webster's Dictionary or a Python dictionary of dictionaries of dictionaries?

## Assignment
Elementary Data 2 will be the assignment -- link will be in our slack channel when ready.

## Setup
Elementary Data 1 assignment.

## Actual

