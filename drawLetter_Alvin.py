#hey cowgirl *cowgirl emoji*
import turtle
def drawA(theTurtle):
    '''draws the letter A'''
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.right(90)
    theTurtle.forward(100)
    theTurtle.backward(100)
    theTurtle.left(90)
    theTurtle.backward(200)
    theTurtle.forward(100)
    theTurtle.right(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.backward(200)

bob = turtle.Turtle()
drawA(bob)
turtle.done()
