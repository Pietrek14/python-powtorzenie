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
    
    for i in range(4):
        t.forward(a)
        t.left(90)
    
    frac(a*0.85,depth=depth+1)

frac(200)

keyboard.wait("e")