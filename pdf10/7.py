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
t.speed("fastest")

def frac(a, depth_limit=3, depth=0):
    if depth == depth_limit:
        t.left(90)
        t.forward(a)
        t.right(90)
        t.forward(a)
        t.right(90)
        t.forward(a)
        t.right(90)
        t.forward(a)
        t.left(180)
        return

    t.left(90)
    frac(a/3,depth_limit,depth=depth+1)
    t.forward(a)
    t.right(90)
    frac(a/3,depth_limit,depth=depth+1)
    t.forward(a)
    t.right(90)
    frac(a/3,depth_limit,depth=depth+1)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.left(180)

t.left(90)
for i in range(4):
    frac(200/3)
    t.forward(200)
    t.right(90)

keyboard.wait("e")