#jaz heres my comment
import turtle
def drawH(ttl):
    '''draws the letter H'''
    ttl.left(90)
    ttl.forward(200)
    ttl.backward(100)
    ttl.right(90)
    ttl.forward(100)
    ttl.left(90)
    ttl.forward(100)
    ttl.backward(200)

theTurtle = turtle.Turtle()
secondTurtle = turtle.Turtle()
drawH(theTurtle)
secondTurtle.penup()
secondTurtle.forward(100)
secondTurtle.pendown()
drawH(secondTurtle)
turtle.done()
