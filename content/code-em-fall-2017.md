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

### Git  

We made our first repository on GitHub! This will be the place where we can upload all of our projects, so we can get to it beyond the class.  

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

### Day Three    

`10/03/2017`  

We did a quick review of what we've learned so far by typing *snippets* of code into the Python interpreter, to get quick results. At the end of class we went though a brain teaser activity together to summarize everything.  

### User Input  

We can easily take input from the user in a program. This can add a bit of fun while coding and running your program. We have all at one point used an app or game that handles input from the user, i.e. a website requesting your username/email and password, etc. In Python, there is a built-in function to handle user input:  

```python  
# Python 2.7
raw_input()

# Python 3+
input()
```  
This command pauses your program and waits for the user to enter some text. After the user hits enter, we can have Python conveniently store it in a variable to make it easy to work with. Here's the example from class:  

```python  
name = raw_input("What is your name?")
height = raw_input("How tall are you?")
animal = raw_input("What is your favorite animal?")
```
Our challenge was to handle all the information the user types in by returning a set a statements that makes sense of it all using concatenation (what we learned last week).  

```python  
print("So, you are named " + name + ", you are " + height + " tall")
print("and your favorite animal is a " + animal + ".")
```  
When we use the function `input()` or `raw_input()`, Python automatically thinks the information entered by the user is a string. For instance, what if we wanted to add two numbers typed in by the user:  

```python  
number1 = raw_input("Give me a number")
number2 = raw_input("Give me another number")
print(number1 + number2)
```
Let's say the user typed in the number `5` and the number `10`. This returns...
```python  
510
```  
Not quite the answer we were looking for! Instead of adding the numbers, Python *squished* them together. Why? Python thinks the numbers are strings. We can easily fix this by using another built-in function, `int()`, short for integer. Maybe you remember INT from the first day. INT, or integer is one of four data types found in just about every programming language; it is a whole number, so it does not have a decimal point.  

### Assignment Two    

See if you can create a simple program that takes two numbers from the user and adds them together. Use the `int()` function to do this. We'll go over the answer in class next week.  

***  

### Day Four        

`10/12/2017`  

Happy Ada Lovelace Day!!!  

### Computational Thinking  

Essentially, a useful way to approach and solve any problem. We will learn how to take real-world problems and make them "computable", or put them in program form in order to solve it. We started with an example on cleaning a whole house. Let's say your house is a complete mess! You are tasked with cleaning your whole house by a certain time. At first, this may seem overwhelming. However, if we take a computational thinking approach, we can *systematically* begin to tackle this problem. Below are the general steps we took to how we could complete the task of cleaning the whole house.  

* Computational Thinking  

  * Decomposition  
    - Decompose: break down: divide & conquer  
    - Break down a problem into smaller problems  
  * Generalize   
    - Be able to see the big picture  
    - See how the smaller tasks make up the larger task  
  * Recognize Patterns  
    - Look for familiar things  
    - Be able to see parts that repeat  
    - Don't Repeat Yourself --> **DRY**  
  * Algorithm Design  
    - Make a plan to tackle the problem  
    - Carry out the plan  

### Computer System Layers  

When we are working in one layer, we do not need to concern ourselves with the information in the surrounding layers. This way, we can just focus on what needs to be done in the moment. Think of abstraction as a mental model; a way to think about something. Have the unnecessary details hidden, so we can leave only the information we need to complete our goal.  

Abstraction Examples:  

* A Person Driving a Car  
  - The only thing they need to focus on is the road ahead.  
  - It is unnecessary to worry about details of how the engine or electronics of the car work.  

* Fast Food Restaurant  
  - At many restaurants, the names of meals have corresponding numbers.  
  - The food prep has been trained to recognize the meal number, not worry about the full name.  

### Functions     

We've already seen functions in action. For example, one of Python's built-in functions (already made and ready to be used), the `print()` function, which we know returns the information we put inside of the parentheses:

* `print("Hello World")` --> returns, `Hello World`  

* `print(123)` --> returns, `123`  

A function is like a mini program that goes off and performs a specific task. The task of the `print()` function is to display a value, or sequence of values. We can **call** a function by using the function's name, followed by a set of parentheses.  

For another example, when we create a variable that holds a value, we can display that value using the print() function.  

```python  
message = "Greetings!"
print(message)
```  

Same goes for the `raw_input()` function; which we know from Day Three, pauses the program and waits for the user to type in some information. The values we give (or **pass**) to a function inside the parentheses, are called **arguments**.  

### Turtle Graphics  

#### Interface Design  

Python's turtle program (or **module**), is a program that holds a slew of functions waiting to be used. All we have to do is put `import turtle` towards the top of any python file we create and now, we can write instructions that display images using turtle graphics! Rather than explain the turtle module from scratch, take a look at the official python documentation on Turtle Graphics:  

*"Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an import turtle, give it the command turtle.forward(15), and it moves (on-screen!) 15 pixels in the direction it is facing, drawing a line as it moves. Give it the command turtle.right(25), and it rotates in-place 25 degrees clockwise."* -[Python 3.3.7 Doc](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)  

Here's the first program we wrote together using turtle graphics:  

```python  
import turtle

# name your turtle
frank = turtle.Turtle()

# tell your turtle where to go
frank.fd(100)
frank.lt(90)
frank.fd(100)

# so the window doesn't disappear right away, add:
turtle.mainloop()
# or turtle.exitonclick()
```  
*Think of the "turtle" as a pen, marker, etc. We are giving this writing tool instructions to draw lines on a separate window (or piece of paper) --similar to our brain giving instructions to our hand to write or draw*  

Above, we called **methods** to tell our turtle where to go. Methods are like functions, but use different syntax. Calling a method is like making a request (*or command*). You are telling frank (or whatever you named your turtle) to move forward, x-amount and turn, x-amount, and so on.  

### Assignment Four  
The example above creates a right angle. Create a python program that uses turtle graphics to make a complete square. You may at first, find your are repeating a set of instructions. Remember to stay **DRY**, don't repeat yourself. You can use a loop function holding the instructions that repeat; making the amount you type, less.  

***  

### Day Five          

`10/17/2017`  

Solution to assignment four:  

```python  
import turtle
frank = turtle.Turtle()

### With a "for" loop ###
for i in range(4):
  """repeats the indented instructions underneath, 4 times."""
  frank.fd(100)
  frank.lt(90)
turtle.mainloop()

### Get the same solution with a "while" loop ###

while True:
  frank.fd(100)
  frank.lt(90)

# However, this while loop repeats forever
# a while loop runs, as long as...
# we'll learn later a few techniques to stop while loops
```  

### Loops  

A `for` statement is a loop, because the flow of execution runs through the body (anything indented below it), then loops back to the top. In the case above, the loop repeats four times.  

A `while` loop runs as long as, or *while*, a certain condition is *True*.  

### Encapsulation  

This is where we'll practice recognizing patterns. What if we wanted to reuse our code that draws a square, more than once? Our challenge is to put our square code into a reusable function. So, we'll define our own function rather than using a built-in one i.e. one of the "powers" of programming, we can create anything we want! First, we'll start by giving our function a name, "square".  

```python  
import turtle
frank = turtle.Turtle()

# name the function, with a generic parameter so we can use the function for more than one turtle
def square(t):
  """Reusable function to draw a square."""
  for i in range(4):
    t.fd(100)
    t.lt(90)

# call the function, with the name of the turtle as the argument
square(frank)
# create a new turtle to see how we can use the same function
ally = turtle.Turtle()
square(ally)

turtle.mainloop()
```  

Above, we used **encapsulation** by wrapping up a piece of code (or for loop *code block*), then placed it inside a function. Why encapsulate? To stay **DRY**, reuse code. "t" can now be any turtle. We call the same function; except, we pass the new turtle's name as an argument inside the parentheses of the new function. When we get to having more than one turtle use the function we created, we don't need to concern ourselves at this point with the code that makes the function do what it does; we're just happy it works. We only need to concern ourselves with creating multiple turtles which use the same function, and pass the arguments we want. We are communicating just the information that needs to be exchanged. In other words, we *encapsulate* the details *inside* the function. This is a useful tool to keep in mind as we get into larger programs. This idea of **hiding the unnecessary details to focus on the goal at hand** is familiar to us, because it is the idea of abstraction.  

### Generalization  

We added a new parameter, "length" to the `square()` function. Instead of specifying a set length, `100` in the loop, we leave the value open to change. In other words, we'll make the function more "general" and less specific.  

```python  
import turtle

# tell python the names of your turtles
frank = turtle.Turtle()
ally = turtle.Turtle()
albert = turtle.Turtle()

def square(t, length):
  """Reusable function to draw a square."""
  for i in range(4):
    t.fd(length)   # changed 100 to the generic term, length
    t.lt(90)

# call the function like last time, now with two arguments:
# turtle name, length of the line
square(frank, 400)
square(ally, 250)
square(albert, 600)

turtle.mainloop()
```  

Adding a parameter to a function is called generalization. This way, we can use it across more situations. Before, the square was always the same size. Now, we can make it any size we want; moreover, have several different "turtles" to draw several different squares of varying sizes.  

### Assignment Five  
Use turtle graphics to *draw* the answer in a simple calculator program. Here's what the program needs (the "specs"):  

* take the user's input for two different numbers  
* take the user's input on what to do with the two numbers i.e. which operator?
* handle the user's input above with condition statements
* display the answer to the user with turtle graphics  

***   

### Day Six  

`10/24/2017`  

We ensured our programming talents so far by walking through steps to fire up a Python program, display text to screen, create/handle variables, and define our own function.    

### Slackbot  

We briefly saw a demo of the Slackbot, *Sirexa*. We can sum up Sirexa to be a simple command-response program housed in a few python files. We can type commands to the bot via Slack (the messaging app we are using to collaborate) and it will return the response we programmed it to! We will fully dive into this project next week during class.  

Example code for the calculator program using turtle graphics:  

<script src="https://gist.github.com/joetechem/8dab08f959052ea0d13f6285e5bdb1d4.js"></script>  

***  




