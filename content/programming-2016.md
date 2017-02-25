Title: Programming (Spring 2016)
Date: 2016-05-09
Category: Classes
Tags: python, pythonista
Author: Wray Mills
Summary: Concepts and Homework

### Spring 2016 Programming, Tuesday mornings and Thursday nights

We'll use this blog page to post some of the code/concepts we learn in class and to post the challenges/homework to ensure you all are practicing in between classes. Just like sports or other schools subjects, practice makes perfect. At this point in your learning to code, the more you practice writing code and testing it and exploring changes and modifications, the better you will get. Remember, by the end of this class, you should be able to write somewhat complex programs to solve problems. Feel free to contact me via email if you have questions or use the comments section below.


### Some more background for parents
For this class we are using Python. Specifically, we have been using Python 2.7 which you can download and install from [python.org](http://www.python.org). Your student should know how to launch Python's editor, IDLE and use that to create and modify programs. They are learning the syntax for the language in our class (as well as the general terms we used to describe part of a program, like: identifier, keyword, literal, expression, statement, conditional, function, etc.) It will take awhile for them to absorb these terms and thats ok -- we'll review them practically every class. You can always take the code from this page and paste it into a new file in IDLE and from the menu, choose Run -> Run Module which will run the program in another window.

### The random sentence code
<script src="https://gist.github.com/wray/4e469b9d87cb8d7e2bbe.js"></script>

### Assignment 1
Using the random sentence code, just as we replaced the nouns with animals, try replacing your verbs with verbs form the random from random lists: https://www.randomlists.com/data/verbs.json .

Then, you can explore replacing the object of your sentence with a noun from the pictionary list from random lists:
https://www.randomlists.com/data/pictionary.json .


### Moon weight code
<script src="https://gist.github.com/wray/a6555c41154642196d9f.js"></script>

### Assignment 2
Take a look at the moon weight code and make sure you understand how to define a function and then use (or call) a function. As we discussed, this is a fundamental concept in many languages, especially Python. Good programmers will break up their code into functions to avoid using the same code (patterns of code) over and over again throughout their program. Remember, this is your primary weapon to support DRY (DO NOT REPEAT YOURSELF).

Now, for the hard part of the assignment. Go back to your random sentence code and assignment 1 where I asked you to use a list of verbs and pictionary. Notice that you will end up repeating 2 lines of code every time you grab a list. And this code is pretty complex and tricky (so it's easy to mistype and introduce a mistake). So, look at those lines and pick out all the parts that are exactly the same and the small part that is different. You should then be able to put that code in a function. And take the one place that HAS TO BE "different" and use that as input into the function. So, try putting that code into a function defined like this:

```python
def random_word(collection_name):

     # Your code goes here
     
     return word
```

So, this function takes in as input (one parameter), the name of the word collection from the randomlists site, and returns a random word from that list. This is a little tricky because your existing code may use a list variable that is specifically named (e.g. animals). When you put this into a function that can be retrieving whatever list is specified by the input, you will want to make that variable less specific (e.g. words) -- in other words, this variable name does not have to change for each collection. The other hint in solving this involved string addition (we call concatenation). You will need to change the url to get the specified list.

```python
'https://www.randomlists.com/data/' + collection_name + '.json'
```

Finally, remember in class we wrote some code where we would use a function on a function (call a function within a function call). For extra credit, you can use this technique to make your function definition just one line of code. Here is an example of that syntax -- note how the parenthesis control the order of the functions (just like in math). The inner function will be called first.

```python
str(int('12'))
```

As always, comment here or email me if you have an issues or questions.


### Assignment 3

Here is a real quick assignment to have you all continue to practice converting a problem to a programmed solution. Create a program that generates the [Fibonacci Sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html). Create the sequence in a Python list. You can simply calculate the first 20 or 30 numbers. For extra credit, use a Python function as part of your solution.

### Assignment 4

To make sure we get some more creativity into the class, we worked on a text-based choose your own adventure game in class. So, keep working on your choose your own adventure game (text version). Here is my short little choose your own adventure, just for your reference. Think about how your adventure design is like an upside down tree with branches. We actually call these blocks of code branches! Think about how to test your program -- you'll want to make sure you visit every branch to ensure all of your code works.

<script src="https://gist.github.com/wray/48cef3a6766ece0d8370.js"></script>


### Assignment 5

Make sure you have your fibonnacci program working with the graph. Explore the matplotlib library by graphing different lists: remember, it will simply plot x,y coordinates when provided a list of x values and a list of y values. The lists should be the same size.

Spoiler alert!! Please make sure your code is working first, before you take a look at this example:

```python
import matplotlib.pyplot as pyplot
import math

x = range(14)

y = [0,1]

for i in range(12):
    y.append(y[i]+y[i+1])

print y

pyplot.plot(x,y)
pyplot.show()
```

### Assignment 6

Because Blaise Pascal is considered an early Computer Scientists and actually created and sold his mechanical "Pascal's Calculater" that is a wonderful example of early mechanical computers. Let's honor him by creating a program to generate [Pascal's Triangle](http://www.mathsisfun.com/pascals-triangle.html). As you think about the steps to create each row in the triangle, see if you can create a function that takes as input a row in the triangle to return the next row.

```python
def pascal(prev_row):

  # Your code goes here

  return row

```

With a simple function to compute the next row  you can create a loop that calls this function repeatedly to build the triangle. One hint  is that you need to start the triangle with a list containing the number 1.

```python
row = [1]
```

Another hint is that the second row is a special case -- youf function could simply return [1,1] when input [1], because the Pascal's triangle pattern is much simpler to implement once you have 2 numbers in your list.

For extra credit, you can test your triangle by making sure that the sum of each row is equal to 2 raised to the row level in the tree, using 0 for the first row. In python, we use \*\* to indicate an exponent. So, the sum of the first row should equal 2\*\*0, which is true cause the first row is simply 1. The second row is [1,1] so the sum is 2, which is equal to 2\*\*1. And so on, and so on. And for super extra credit, you can graph the sums of the row -- use the row level for the y axis and the sum for the x axis.

### Assignment 7

Make sure you understand how we solved Assignment 6 and you are clear on the difference between defining a function and calling (or using) a function. Because we wrote a function that returns the next row in Pascal's triangle based on the current row input, we are able to efficiently generate the triangle.

For the next assignment, I'd like for you all to try and get pyglet installed and run the following simple program. To install pyglet, you can go [here](https://bitbucket.org/pyglet/pyglet/wiki/Home) and actually choose the [download](https://bitbucket.org/pyglet/pyglet/wiki/Download) link.

Once downloaded, you should be able to unzip the download and look for a file in the directory called setup.py. You should be able to run this by double-clicking on it. Or you may have to launch IDLE (python) and open that file and choose run. Running that file will install pyglet on your machine and then you will be able to start using it.

```python

import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('Hello World',
                          font_size=24,
                          font_name="Times New Roman",
                          color=(255,255,255,255),
                          x=window.width//2-70,
                          y=window.width//2)
                          
def on_draw():
    window.clear()
    label.draw()

window.on_draw = on_draw

pyglet.app.run()

```

### Assignment 8 (started in class, can finish at home)

Whether you realize it or not, you have already been using Object Oriented concepts because Python is an object-based language. We have discussed in class over the past two weeks the different between a class and an object -- a class provides the definition (code) so that many objects can be created from that class. Similar to functions, you define the class once to be used again and again every time you need an object of that class. We started with a class to define a multi-sided die and worked up to a simple dice rolling exercise where each die keeps track of its own history.

See the following gist -- should be similar to the code you wrote in class:
<script src="https://gist.github.com/wray/3f56149db45d954beed20764ad1b7c1e.js"></script>

To keep going with this assignment, think about how you could add code to the MultiSidedDie class to keep track of how often each side is rolled. The solution requires creating a dictionary variable in the class. The dictionary should have a key for each side of the dice where the value is updated each time that side is rolled. Using this stats dictionary and history list, you can then calculate the roll percentage for each side.

Remember the syntax for a dictionary:

```python

# creating and populating a dictionary
d = {}
d[key] = value
d[key2] = value2

# getting values from a dictionary
d[key]

```

### Assignment 9 (also mostly done in class)
One of the many benefits of Object Oriented design and programming is to organize your code the same way humans organize their world -- classifications and class hiearchies. Defining a general class allows you to define more specific sub-classes without having to re-define the parent class methods. For example, we started to create some code to "model" a book. When using a book in the real world, you need to be able to read the book, turn pages, and place a bookmark to pick up where you left off before.

Review the following code which should look similar to the code you wrote in class:
<script src="https://gist.github.com/wray/707297e73e401d01329b87060b48ddbf.js"></script>

For fun, think about what you would need to do to create another sub-class of Book that is a pop up book.


### Python 3 and Graphics
We are going to change direction a little bit and use Python 3 now and the graphics that come with Python 3 (along with a simple graphics library to make things a bit easier).

 * Download [Python 3](http://python.org) (if you haven't already).
 * Download [graphics.py](http://mcsp.wartburg.edu/zelle/python/graphics.py) and put the file in the same folder as your python code.
 * Create a simple file using the Python3 IDLE with simply:

```python
 from graphics import *
```

 * Run the program and in the window that opens, type in this:

```python
 win = GraphWin('Hello')
```

 * You should see another window has popped up.
 * So, then you can:

```python
 win.close()
```


Don't forget, you can "use the source, Luke" and open the graphics.py file to see what other options you have -- we'll be using this graphics package for the final projects.

### Assignment 10 (mostly covered in class)
Once you have graphics setup as above, we played around with the graphics file and talked about how it is Object-Oriented (as is most graphics modern graphics packages). Not only can we draw shapes in our graphics window, but we can also create entry boxes and wait for mouse clicks.

However, we quickly found that the graphics.py library doesn't include a button. So, we used our new Object-Oriented skills to extend the library to include a button. Make sure your code for the button is working for this assignment. Don't worry if some of the syntax seems odd -- class initializers can be confusing because the method must be named __init__ . And when we extend classes, we will want to call the parent class' initializer (the first line of code in our Button initializer). We then did something even more advanced -- we overrode the draw method in Rectangle to make sure our button class draws not just the rectangle, but also the text label.

<script src="https://gist.github.com/wray/b4744c0bdea2ccd7e3cc0e5b8150f8f2.js"></script>

### Assignment 11
For the final two weeks of class I'd like for everyone to go back to their choose your own adventure game and have it run with a graphics window. I'll start posting a few hints for that here.

I hope you all have been able to carry on with what we started in class. My graphics choose your own adventures follows below. Please come to class with questions on my use of the keywords break and pass.

<script src="https://gist.github.com/wray/11b9c498651c14ef81e7d33a028438cf.js"></script>

### Final Assignment
We have also been talking about the Dice Poker game so the final final project will be to also make that game use a graphics interface. You'll need to show the dice, the player's score and their current roll score. You'll need to have buttons to roll again as well as some way to choose which dice to re-roll.
