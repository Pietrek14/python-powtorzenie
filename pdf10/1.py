import turtle
import keyboard

def new_turtle(x,y):
    newTurtle = turtle.Turtle()
    newTurtle.speed("fastest")
    newTurtle.penup()
    newTurtle.goto(x,y)
    newTurtle.pendown()

    return newTurtle

t = new_turtle(-200, 0)

def frac(a, r=7, depth_limit=3,depth=0):
    if depth == depth_limit:
        t.right(90)
        t.circle(r)
        t.left(90)
        return
    
    t.left(45)
    t.forward(a)
    frac(a/2,r,depth_limit,depth+1)
    t.backward(a)
    t.right(45)
    t.forward(a)
    frac(a/2,r,depth_limit,depth+1)
    t.backward(a)
    t.right(45)
    t.forward(a)
    frac(a/2,r,depth_limit,depth+1)
    t.backward(a)
    t.left(45)

t.forward(150)
frac(150)

keyboard.wait("e")