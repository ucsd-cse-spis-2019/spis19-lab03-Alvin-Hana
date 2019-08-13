import turtle
import time
import random
# Create a turtle
player1 = turtle.Turtle()

# Set the simulation speed to maximum. This is not the speed of the turtle, but specifies
# how fast the animations are updated. A value of "0" is best for smooth animations
player1.speed(2)
player1.write(random.randrange(0,10))


# Function that will be executed on a specific key stroke (see below)
# It causes player1 to turn left
def turnleft():
    player1.left(30)

def turnright():
    player1.right(30)

def stop():
    player1.speed(0)
    global go
    go = False
    turtle.done()

# Function that will be executed on a specific key stroke (see below)
# It causes the speed of player 1 to double
def speedup():
    global speed1
    speed1 = speed1 * 2

# This code makes the turtle library listen to key strokes
# Then for the keys listed, e.g., the left arrow or the "d" key,
# it specifies which function will be executed when that key is pressed. 
# You can list additional keys and tie them to your own functions
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(stop,"d")
turtle.onkey(speedup,"s")
# The initial speed of player 1
speed1 = 0.25

# Print the current time
# This is Unix time, i.e., the time in seconds since 1/1/1970
print(time.time())
go = True
if(time.time()%5==0):
    turtle.speedup()

# This is the main game loop
# It is an infinite loop; this code is executed forever
while go:
    player1.forward(speed1)


