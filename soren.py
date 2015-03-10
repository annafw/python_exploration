# To a python interpreter The symbol '#' indicates
# that the following text is not python code but
# instead a comment, not to be interpreted.
# In the following all comments
# are descriptions, explanatations or instructions.

# We need to use the turtle package which
# provides all the functionality for us to do
# turtle graphics.
# import loads the implementation of the specified package
import turtle;

# everything following the '#' is a comment
bob=5  # bob is now the number 5
print(bob)

bob=turtle.Turtle();  # bob is now a turtle object
print(bob)

# A turtle object can be given commands to move around on a
# "canvas" which is like a sheet of paper

# You can give bob commands to do many things
bob.reset()  # delete bob's paths and center on canvas

# 'fd' is an abreviation for 'forward'
bob.fd(100)  # move bob forward 100 units

# 'rt' is an abreviation for 'right turn'
bob.rt(100) # rotate bob 100 degree to the right
bob.fd(100)  # move bob forward 50 units

# 'lt' is for left turn and 'bk' is for backward
bob.lt(105)
bob.bk(75)

bob.clear() # clears screen but leave the turtle where he was
bob.reset() # clears screen and centers bob on the canvas

# The 'penup' tells bob to keep the pen off the canvas when
# he moves
bob.penup()
bob.fd(200) # no line was drawn

# The 'pendown' command tells bob to put the pen back down
# so it draws on the canvas when he moves.
bob.pendown()
bob.bk(200)

# You can also change the pens color
bob.color("blue")
bob.lt(90)
bob.fd(90)

# you can have more than one turtle on the same canvas
sally = turtle.Turtle()
sally.fd(100)
sally.rt(90)
sally.fd(90)

bob.reset()
sally.reset()

bob.rt(90)
bob.fd(90)
sally.fd(90)

# Now start over with your own turtle, named
# whatever you want, move your turtle around a little
# maybe change the color of your turtle.

# After you have moved you turtle around give your turtle the
# 'reset' command so the canvas is cleared and the turtle
# is centered.
bob.reset()
# Now lets draw a square
bob.fd(150)
bob.rt(90)
bob.fd(150)
bob.rt(90)
bob.fd(150)
bob.rt(90)
bob.fd(150)
bob.rt(90)

# Notice we did the same thing 4 times in a row, maybe you even copied
# the text so you didn't have to type it four times.
# There must be an easier way to repeat things in python, and there
# is.  Repeating is also called iterating or iteration.

# Python has special objects called 'iterators' that can be used in
# what is called a 'for loop'

# An iterator is an object from which you can asked for the next
# element repeatedly, until you get to the end.

# range() returns an interator object or integers of the
# specified size

iteratorObj = range(4)
print(iteratorObj)
# notice that the interator object has 4 integers but they are
# the numbers 0,1,2,3 and not 4.  Remember this, it is what
# range does

# You can select individual components of an iterable object
print(iteratorObj[1])  # this is the second object
# this is called indexing and notice that the first item is indexed
# with 0.
print(iteratorObj[0])

# The following is a "for loop".
# for each item in iteratorObj assign it to
# the variable i
# the body of the for loop is everything that is indented
# underneat the for statement
for i in iteratorObj:
    print(i)
    # if I had more statements here the would also
    # be executed as part of the loop

# Use a for loop to make a square
bob.reset()
for i in iteratorObj:
    bob.fd(150)
    bob.rt(90)

# Now write a for loop that will make a triangle
# It help to imagine you are the turtle to know
# what you want it to do.  Even walking around on the
# floor can help you.

# Can you write a for loop to make a pentagon?

# next we are going to make a house but first
# we are going to learn how to define a function
# that will execute a block of code.

# The following is a function that
# tells bob to make a square
# Recall, range(4) returns an iterator object.
def squareBob():
    for i in range(4):
        bob.fd(200)
        bob.rt(90)

bob.reset()
squareBob()

# We can also pass parameters to the square
# here we can specify how big we want the side to be
def squareBob(side):
    for i in range(4):
        bob.fd(side)
        bob.rt(90)

bob.reset()
squareBob(90)
squareBob(50)
# notice that if we don't provide the
# argument, '90' or '50' above,
# it doesn't work
squareBob()

# we can change the function definition
# to have a default value which it will use
# if a side value is not specified.
def squareBob(side=100):
    for i in range(4):
        bob.fd(side)
        bob.rt(90)

bob.reset()
squareBob()
squareBob(50)

# What happens if you put your squareBob()
# function in a loop?
bob.reset()
for i in range(10):
    squareBob(i*15)

# The following you the values that are passed to squareBob()
# for each iteration of the loop.
for i in range(10):
    print(i*15)

# Now make a function to draw a triangle
# Try do do this before you look at how
# it is done below.

# Then use your triangle function to
# draw a house.

def triangleBob(size=100):
    for i in range(3):
        bob.fd(size)
        bob.rt(120)

bob.reset()
squareBob()
triangleBob()

# That's not so good, What is wrong?
# Can you fix things to make a proper house?
# There are a lot of ways you could fix
# it, here is one.
def triangleBob(size=100):
    for i in range(3):
        bob.fd(size)
        bob.lt(120)


bob.reset()
squareBob()
triangleBob()

# We can also define a function to make a house
def house(size=100):
    squareBob(size)
    triangleBob(size)

# and make a nieghborhood
bob.reset()
bob.penup()
bob.bk(300)
bob.pendown()
house(150)
bob.penup()
bob.fd(175)
bob.pendown()
house(100)
bob.penup()
bob.fd(150)
bob.pendown()
house(75)
bob.penup()
bob.fd(100)
bob.pendown()
house(200)

# You could add doors and windows to your house too.

#===================================================

# Following is a bunch of code that you can use,
# modify and explore.  Some is more complicated than
# others.  Each block has suggestions for what you might
# do next.  You can jump around or try things in the
# order they are presented.  Have Fun.
#

#---------------------------------------------
#    Shapes
#---------------------------------------------

# You know how to make a square and a triangle.
# Now make a function to make a hexagon

def hexagon(size=100):
    for i in range(6):
        bob.fd(size)
        bob.rt(60)

bob.reset()
hexagon()

# Can you define a function to make a polygon of
# any number of sides?  The definition would start
# like the following, which would make a square
# be default.
# def polygon(sides=4):
#     for i in range()

# If you got that to work try making a polygon
# function that you can specify the
# number of sides and the size of the sides.
# The function call would look like this
# polygon(sides=4,size=100)
#
#
# # If you think your polygon function is working
# # but for some number of sides it isn't being
# # closed properly, look at the following to see
# # if it helps you figure out the problem.
# print(10/3)
# print(float(10)/3)
# print(10.0/3)
#
# # Why are we getting different values?  The first one
# # does arithmetic only with integers.  When there
# # is only integers in an arithmetic expression
# # the result will be an integer.
# # float() turns the number into a decimal value so
# # the expression will evaluate to a decimal
# # If you include the decimal the you will get
# # a decimal result.
#
# # Does this give you an idea of how to fix your
# # polygon function?
#
# # Can you use your polygon function to make function
# # that makes a circle?
#
# #---------------------------------------------
# #        Patterns
# #---------------------------------------------
#
# # Define an interesting (or random) path
# def path():
#     bob.fd(100)
#     bob.rt(90)
#     bob.fd(100)
#     bob.rt(90)
#     bob.fd(50)
#     bob.rt(90)
#     bob.fd(50)
#     bob.rt(90)
#     bob.fd(100)
#     bob.rt(90)
#     bob.fd(25)
#     bob.rt(90)
#     bob.fd(25)
#     bob.rt(90)
#     bob.fd(50)
#
# bob.reset()
# path()
#
# # repeat your path
# def thing1():
#     for i in range(4):
#         path()
#
# bob.reset()
# thing1()
#
# # repeat the path again but with a rotaion and shift
# # added
# def thing2():
#     for i in range(10):
#         path()
#         bob.rt(10)
#         bob.fd(50)
#
# bob.reset()
# thing2()
#
# # You can do a similar thing with other
# # shapes you have defined.  What other
# # patterns can you create?
# def squarePattern():
#     for i in range(8):
#         squareBob()
#         bob.rt(360.0/8)
#
# bob.reset()
# squarePattern()
#
# # following makes an arc to the right
# def arcRight(step=3, degrees=60):
#     for i in range(degrees):
#         bob.fd(step)
#         bob.rt(1)
#
# bob.reset()
# arcRight()
#
# # following makes an arc to the left
# def arcLeft(step=3, degrees=60):
#     for i in range(degrees):
#         bob.fd(step)
#         bob.lt(1)
#
# bob.reset()
# arcLeft()
#
# # Use the arcRight function to make a petal
# def petal(size=2):
#     arcRight(size,60)
#     bob.rt(120)
#     arcRight(size,60)
#     bob.rt(120)
#
# bob.reset()
# petal()
#
# # Use the petal function to make a flower
# def flower(size=3):
#     for i in range(6):
#         petal(size)
#         bob.rt(60)
#
# bob.reset()
# flower()
#
# # You can also fill with color the
# # shapes you create
# bob.reset()
# bob.fillcolor("red")
# flower()
# bob.fill(True)
#
# bob.reset()
# bob.begin_fill()
# flower()
# bob.end_fill()
#
# # This creates someting polygon like
# def somePoly(side,angle,steps):
#     for i in range(steps):
#         bob.fd(side)
#         bob.rt(angle)
#
# bob.reset()
# somePoly(50,72,5) # pentagon
# somePoly(100,144,5) # a star
# somePoly(50,135,8) # different star
#
# #---------------------------------------------
# #            Random Motion
# #---------------------------------------------
# # The random package will allow you go generate
# # random numbers.
# import random;
# for i in range(30):
#     print(random.random()) # random numbers between 0 and 1.
#
# # Here is code to make the turtle move in a randomly
# # selected direction.
# # This is an example of how bacteria move and is also known
# # as Brownian Motion.
# bob.reset()
# for i in range(20):
#     r = random.random()
#     ang = ((r -.5) * 180)
#     bob.fd(5)
#     bob.rt(ang)
#
# def randomWalk(length=50):
#     for i in range(length):
#         r = random.random()
#         ang = ((r -.5) * 180)
#         bob.fd(5)
#         bob.rt(ang)
#
# bob.reset()
# randomWalk()
#
# # You can add more parameter to the random walk
# # function give more control to how the walk is
# # done.
#
# #--------------------------------------------
# #       Controlling the Animation
# #--------------------------------------------
# # You can control the animation and screen.
# # Get a canvas/screen object
# canvas = turtle.Screen()
# # Get the delay between turtle motions
# print(canvas.delay())
#
# # Set the delay value
# # to change how fast the animation happens
# canvas.delay(40)
# house()
# canvas.delay(5)
# house()
#
# # Create a user interface that allows the user
# # to control the turtle.  Can you read the code
# # and figure out how to control the turtle?
# # Run the code and see if you are right?
# # This is code like what you may have see
# # from "The Dark Tunnel" tutorial.
# keepDriving = True
# while keepDriving:
#     print("D-one, F-orward, R-ight, L-eft")
#     command = raw_input("enter choice ")
#     if command == "D":
#         keepDriving = False
#     elif command == "F":
#         bob.fd(50)
#     elif command == "R":
#         bob.rt(45)
#     elif command == "L":
#         bob.lt(45)
#
# #-------------------------------------------
# #     Recursion
# #-------------------------------------------
#
# # Recursion can be a dificult concept to understand
# # A recursice function calls itselt like the
# # following two functions.
# # A recursive function always has a parameter
# # that control when the recursion stops
# def spiral(side, angle,steps):
#     if(steps > 0):  # when steps = 0 (or less than) stop
#         bob.fd(side)
#         bob.rt(angle)
#         spiral(side+5,angle,steps-1) # recursive call
# # notice steps is reduced each time a recursive call is
# # made so eventually it will be set to 0.
#
# bob.reset()
# spiral(5,120,50) # triangl spiral
#
# bob.reset()
# spiral(5,75,50) # almost pentagon spiral
#
# bob.reset()
# spiral(5,157,50) #
#
# # You can also change the "line" to be a different path
# def zigZag(length=50):
#     for i in range(3):
#         bob.rt(30)
#         bob.fd(length/6.0)
#         bob.lt(60)
#         bob.fd(length/6.0)
#         bob.rt(30)
#
# # Now you are replace lines, "bob.fd()" calls,
# # with zigZag's, we is done for the making
# # a square below
# def ziggySquare(size=200):
#     for i in range(4):
#         zigZag(size)
#         bob.rt(90)
#
# bob.reset()
# ziggySquare()
#
#
# # Lots of things in nature have a recursive structure to them.
# # Trees are a good example.  A tree is a big branch that has
# # branches sticking out of it, and those branches
# # have branches stick out if them, and so on ...
#
# # Following creates a Y-tree.  Can you figure out what
# # each line does?
# def yTree(length=100,level=1):
#     if(level > 0):
#         bob.fd(length)
#         bob.lt(45)
#         yTree(length/2.0,level-1)
#         bob.rt(90)
#         yTree(length/2.0,level-1)
#         bob.lt(45)  # what does this do?
#         bob.bk(length) # and what does this do?
#
# bob.reset()
# bob.lt(90)
# yTree(100,4)
#
# # You can experiment with this yTree code by changing
# # the angles, or making the angle a parameter
# # You can also change the thickness of the lines.
#
# # If you get this far there a lot of things you can do now:
# # Create a neighborhood with trees and bees (randomWalking).
# # Modify the functions that are interesting to you so
# # you have more control over what they do.
# # Make a maze.
# # Ask a mentor for a challenge.
# # Combine things you have learned if your own creative
# # way.
