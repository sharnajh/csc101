# CSC 101
# Sharna Hossain
# Chapter 10 | Program 9
# hit_the_target.py

# Hit the Target Game
import turtle

# Importing random module to generate random target position for
# each game
import random

# Allow user to choose color of turtle
color = input("What color should the turtle be?\t")

# Using if-elif-else statements to make program more interactive
if (color == "blue" or color == "pink"):
    print(f"{color} is my favorite color! Nice choice!")
elif (color == "brown" or color == "yellow"):
    print(f"{color} is my not favorite color, but to each their own...")
else:
    print(f'{color} has been selected')

# Changing the turtle color and fill color
turtle.pencolor(color)
turtle.fillcolor(color)

# Named constants
SCREEN_WIDTH = 600                  
SCREEN_HEIGHT = 600                
TARGET_WIDTH = 25                           
FORCE_FACTOR = 30                   
PROJECTILE_SPEED = 1                
NORTH = 90                          
SOUTH = 270                         
EAST = 0                            
WEST = 180 

# I am using range() to place target in random coordinate
# on the screen
TARGET_LLEFT_X = random.randint(1,SCREEN_WIDTH/2)       
TARGET_LLEFT_Y = random.randint(1,SCREEN_HEIGHT/2)                             

# Setup the window
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

# Draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle:\t"))
force = float(input("Enter the launce force (1-10):\t"))

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
else:
        print('You missed the target.')