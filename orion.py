import turtle

# Set the window size
turtle.setup(500,600)

# Setup the turtle
turtle.penup()
turtle.hideturtle()

# Create named constants for star coordinates
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELSTAR_X = -40
LEFT_BELSTAR_Y = -20

MIDDLE_BELSTAR_X = 0
MIDDLE_BELSTAR_Y = 0

RIGHT_BELSTAR_X = 40
RIGHT_BELSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Draw the stars
turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELSTAR_X,LEFT_BELSTAR_Y)
turtle.dot()
turtle.goto(MIDDLE_BELSTAR_X,MIDDLE_BELSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELSTAR_X,RIGHT_BELSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.dot()

# Draw the star names
turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.write("Betegeuse")
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.write("Meissa")
turtle.goto(LEFT_BELSTAR_X,LEFT_BELSTAR_Y)
turtle.write("Alnitak")
turtle.goto(MIDDLE_BELSTAR_X,MIDDLE_BELSTAR_Y)
turtle.write("Alnilam")
turtle.goto(RIGHT_BELSTAR_X,RIGHT_BELSTAR_Y)
turtle.write("Mintaka")
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.write("Saiph")
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.write("Rigel")

# Draw lines connecting the stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELSTAR_X, LEFT_BELSTAR_Y)
turtle.penup()

turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X,RIGHT_BELSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELSTAR_X,LEFT_BELSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELSTAR_X,MIDDLE_BELSTAR_Y)
turtle.penup()

turtle.goto(MIDDLE_BELSTAR_X,MIDDLE_BELSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X,RIGHT_BELSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELSTAR_X,LEFT_BELSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.penup()

turtle.goto(RIGHT_BELSTAR_X,RIGHT_BELSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)

# Stops turtle window from closing after running
turtle.done()