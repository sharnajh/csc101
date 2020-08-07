# CSC 101
# Sharna Hossain
# Chapter 12 | Program 33
# graphics_mod_demo.py

# For my modification of graphics_mod_demo.py,
# I will be using the random module to generate
# random RGB color codes for the turtle graphics
# as well as randomzing some of the variables.
# The result looks like very abstract art.

import turtle
import my_graphics
import random

# Set the turtle screen colormode to [0,255] scale, this
# was necessary because by default the colormode is at
# a [0,1] scale of floats. I wanted to set it as 255
# because of what we learned in class during the Multimedia
# chapter.
turtle.colormode(255)
# Setting window size of turtle to better randomize plot points
turtle.setup(700, 700)

# Creating helper functions to generate 3 random integer
# between 0 and 255 using the random module, which together
# make an RGB color code.


def random_rgb():
    # Generate random RGB code by returning 3 random floats
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


# Set background to random color using random_rgb()
turtle.bgcolor(random_rgb())


# Functions to randomize plot points and shapes
def random_coords():
    return random.randint(-350, 350)


def radius():
    return random.randint(50, 120)


def random_square():
    my_graphics.square(random_coords(),
                       random_coords(),
                       (random_coords() - random_coords()),
                       random_rgb())


def random_circle():
    my_graphics.circle(random_coords(), random_coords(),
                       radius(), random_rgb())


def random_line():
    my_graphics.line(random_coords(), random_coords(),
                     random_coords(), random_coords(), random_rgb())


def main():
    turtle.hideturtle()

    # Draw some squares
    for x in range(random.randint(1,7)):
        random_square()

    # Draw some circles.
    for x in range(random.randint(3,6)):
        random_circle()

    # Draw some lines
    for x in range(random.randint(3,7)):
        random_line()

    # Stops turtle graphics from closing
    turtle.done()


main()
