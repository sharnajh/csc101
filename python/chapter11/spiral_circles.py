# CSC 101
# Sharna Hossain
# Chapter 11 | Program 22
# spiral_circles.py

# In lieue of submitting flower.py which I could not find
# anywhere in Chapter 11 or anywhere else in the textbook,
# I am providing the altered code for spiral_circles.py
# (which was maybe mistaken for flower.py, because it looks
# like a flower?)

# In my alteration of spiral_circles.py, I am going to have
# the loop function change the color of each "petal" on
# each iteration by changing the pencolor.
# I will be selecting a random color for each petal by
# generating a random integer between 0 and 255 for each
# RBG (Red, Blue, and Green) value and setting the pencolor()
# with it.

# This program draws a design using repeated circles.
# Importing random module to help select random integer.
# Importing keyboard to detect correct keypress.
import random
import turtle

# Set the turtle screen colormode to [0,255] scale, this
# was necessary because by default the colormode is at
# a [0,1] scale of floats. I wanted to set it as 255
# because of what we learned in class during the Multimedia
# chapter.
turtle.colormode(255)

# Setting background color to black to make colors stand out.
turtle.bgcolor("black")
turtle.hideturtle()

# Creating helper functions to generate 3 random integer
# between 0 and 255 using the random module, which together
# make an RGB color code.


def random_rgb():
    # Generate random RGB code by returning 3 random floats
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


# Named constants
NUM_CIRCLES = 36        # Number of circles to draw
RADIUS = 100            # Radius of each circle
ANGLE = 10              # Angle to turn
ANIMATION_SPEED = 0     # Animation speed

# Set the animation speed
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted
# by 10 degrees after each circle is drawn.


def draw_flower():
    for x in range(NUM_CIRCLES):
        # Generate random RGB code for pencolor
        petal_outline = random_rgb()
        # Change the pencolor
        turtle.pencolor(petal_outline)
        turtle.circle(RADIUS)
        turtle.left(ANGLE)

draw_flower()

# Stops turtle window from closing
turtle.done()
