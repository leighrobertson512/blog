Title: Some Notes for Homeschool Level 2 Computer Science and Tween/Teen Intro to Coding
Date: 2014-10-21
Category: Notes
Tags: computer science, python
Author: Wray Mills
Summary: Some notes and assignments

Remember, we have been doing two things when coding in our classes:

1) Using a command or terminal window to run python3. So far, we typically accomplish this by opening a terminal or command prompt and then using this command:

~~~~~~
cd your_project/working_directory
~~~~~~

What is "your_project/working_directory" ? Well, that depends on what you are using to edit the program files. If you are using Aptana then your project directory may be something like "Documents/Aptana Studio 3 Workspace/wray". Once you find it, remember that directory (write it down maybe). And once you have changed directory (using the cd command) into that area, you don't need to move out of that directory for the remainder of your session. So, to run the python interpreter and test your python code, you will use a command like this:

~~~~~~
python3
~~~~~~

This will start the python interpreter -- you know you are in the interpreter because you will get the triple greater-than prompt. When you see that you can start testing your code like this:

~~~~~~
>>> from your_cool_python_file import *
>>> call_your_cool_python_function(your_parameter1, your_parameter2)
>>> your_object = YourClass(init_paramater1,init_parameter2)
>>>
~~~~~~


2) The second thing we do when coding is actually edit your python files. Using your favorite editor (e.g. Aptana, Eclipse, nano, vi), you will edit your python source files to be tested in the terminal window. Don't forget to save your changes. And you should restart the python interpreter every time and re-import your file, like this (in the python terminal):

~~~~~
>>> quit()
your_command_prompt$ python3
>>> from your_cool_python_file import *
~~~~~

### Homework/Final Assignment

I've been threatening homework for the past two weeks. So, let me post some here for you all. First, please review the instructions above and make sure you are proficient at editing python files and testing them. If nothing else, I want you to be very comfortable doing this so that you can continue to code and be ready for follow-up courses. Secondly, I want you to look at a "case study" in your book: go to page 399 and look at case study 12.3. This is the project I would like you all to do. There is a text-based version and then a graphics version if you are up to that challenge. In order to do the latter, you will likely need to start on the first part before Wednesday. Please come in Wednesday with any questions or issues you may have with this. It is very challenging, but I know you all are up to it. If you do want a bit more background (i.e. if you want something relatively dry to read to help you sleep) you can actually read the first part of Chapter 12 that starts on page 385. This material is very advanced so don't be discouraged if it doesn't make sense, but please email or post a question/discussion here on the blog.

Oh, and the link to some of the materials (like graphics.py) is [here](http://mcsp.wartburg.edu/zelle/python/).
