Title: Code Em Fall 2017  
Author: Josef Seiler  
Date: 2017-09-27  
category: Classes  
Tags: coding, github, slack, computer science, raspberry pi  
Illustration: gears.jpg  

### Day One  

`09/21/2017`  

### Code Em Kick Off  

We started with the usual introductions to break the ice. Code Em has newcomers as well as veterans, so we'll work together to get everyone on the same page of our computer science adventures. Throughout the fall, we will learn effective ways to think (best approaches to tackle problems), become affluent with coding via the Python programming language, and we will learn how to apply the same tools, used by software engineers in the real world.  

#### GitHub & Slack  

We will be harnessing GitHub during each class. This is a site used by software developers to collaborate on the build and upkeep of projects. For Code Em, you will *push* all files/projects you are working on to your own repository (folder). Your repository will continuously be updated as we move forward in the class. When you use GitHub, you essentially have a portfolio of your work you can access outside of class. This will be a great start to feel comfortable on how to use GitHub. Especially when we begin working on the same projects together, we'll get a feel for how real software engineers develop applications. Visit [GitHub.com](https://github.com/), sign up with your email account, create a GitHub username/password (write it down somewhere, so you remember it!), and click **Sign Up for GitHub**. GitHub will send you a verification email to the email you signed up with. Click the link to verify and you will be ready to git!  

*More detailed instructions can be found on the [Tech Em blog page](http://blog.techemstudios.com/github-part-one.html)*  

[Slack](https://slack.com/) is a messaging app for teams of large companies, i.e. Google; and small startups, i.e. Tech Em Studios. Slack will be used in class for questions about material we are learning in class, questions on projects, and communicating with your peers. You will not only have the current instructors as your resource, you will have the whole [Tech Em Team](http://techemstudios.com/about-us.html)! You will receive an email from Slack, which holds an invitation to join the Tech Em Students Slack team.  

*More details on joining Slack can be found on the [Tech Em blog page](http://blog.techemstudios.com/slack.html)*.  

### What we Learned  

#### How to Think     

More than learning to code, we will learn how to think, or how to approach and solve problems (in general) in efficient ways.  

#### Quick Computer History    

What are computers? Early computers were "tools" (mechanical devices) people used to them solve math problems. Modern computers are devices that can be programmed to carry out a task. We started at the *prehistory* era with Tally Sticks. We ended with the Babbage Machine (marked transition from calculation to computation) and Ada Lovelace, considered to be the first computer programmer. We discussed the difference of hardware to software and what makes a program, a program.  

#### Python  

Python is a programming language that is easy to write, understand and used for a growing variety of applications. We dove into Python, by creating small snippets of code in the interpreter, a place to quickly test ideas rather than creating and executing an entire program. We explored data types (found in all languages) and created a program with variables.  

##### Download Python

To practice at home, you can download Python for free from [python.org](https://www.python.org/downloads/). On the chromebooks/[crouton](https://github.com/dnschneid/crouton) we are using thi session, we will focus on **Python 2.7**. If you download the latest Python (3.6), there are a few changes we can easily handle for what we are performing in class. So, it is up to you, which version you would like.  

***  

### Day Two    

`09/26/2017`  

### Fetch, Decode, Execute  

What happens when you fire up your favorite program? Consider a CD with your favorite game on it. This CD has tons of instructions already written on it, waiting to be read by your computer. When you insert the game, the CPU follows this process: **Fetch** the first instruction; **Decode** the instruction, translated into binary for the computer to understand; and finally, **Execute** The computer carries out the instruction. Since there is more than one instruction, this process repeats to get the rest. The process repeats, from the moment you turn on your computer and does so with lightning-fast speed!  

```python  
# In Python, a line that begins with a pound sign (#)  
# is known as a comment.  
# Comments are ignored by the program and are  
# considered "notes" to the programmer(s).
```  


### Expressions & Statements  

We already saw this last week, but we'll put *names to faces*. `print("Hello World!")` is an example of a statement, a complete thought. A statement is a unit of code that does something, like creating a variable or returning the value of the variable. An expression is a combination of values, variables, and operators.  

```python  
# example of a statement  
>>> n = 17  
>>> print(n)  
17

# examples of Expressions  
>>> 24
24
>>> 5 + 22
27
>>> "lamb"
'lamb'
```  

### Variable and String Concatenation  

```python  
# Set two variables, first_name and last_name each equal to a string:  
first_name = "ada"  
last_name = "lovelace"  
# Now combine the values using string CONCATENATION
full_name = first_name + " " + last_name  
# Next, we'll make a new variable that has a custom message for its value.  
message = "Hello, " + full_name.title() + "!")
print(message)
```  
 The final output:

```python  
'Hello Ada Lovelace!'
# title() is a built-in function we used to capitalize the first letters of the strings in the full_name variable
```

### Assignment One  

Make an account on GitHub, and verify it from the email you received from GitHub. Create another Python program that concatenates variables and strings (similar to what we did above).  

***  
