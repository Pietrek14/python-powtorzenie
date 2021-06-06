import turtle
import keyboard

def new_turtle(x,y):
    newTurtle = turtle.Turtle()
    newTurtle.speed("fastest")
    newTurtle.penup()
    newTurtle.goto(x,y)
    newTurtle.pendown()

    return newTurtle

t = new_turtle(0, 0)

def frac(a, depth_limit=35, depth=0):
    if depth == depth_limit:
        return
    
    t.forward(a/2)

    for i in range(3):
        t.left(90)
        t.forward(a)
    
    t.left(90)
    t.forward(a/2)
    
    frac(a*0.6,depth=depth+1)

frac(200)

keyboard.wait("e")