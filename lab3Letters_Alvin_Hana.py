#1) It is the first turtle that Python creates
#2) turtle is the name of the package and Turtle() is a special function that creates a new turtle function
#3) myTurtle.sety(100)
import turtle
def drawA(theTurtle, size):
    '''draws the letter A'''
    
    theTurtle.left(90)
    theTurtle.forward(size)
    theTurtle.right(90)
    theTurtle.forward(size)
    theTurtle.backward(size)
    theTurtle.left(90)
    theTurtle.backward(size * 2)
    theTurtle.forward(size)
    theTurtle.right(90)
    theTurtle.forward(size)
    theTurtle.left(90)
    theTurtle.forward(size)
    theTurtle.backward(size * 2)

bob = turtle.Turtle()
drawA(bob,50)
turtle.done()
