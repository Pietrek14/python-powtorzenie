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

def frac(a, min_squares, depth_limit=4, depth=0):
    if depth_limit-depth+1 < min_squares:
        return
    t.left(90)
    if depth < depth_limit:
        frac(a/3,min_squares,depth_limit,depth=depth+1)
    t.forward(a)
    t.right(90)
    if depth < depth_limit - 1:
        frac(a/3,min_squares,depth_limit,depth=depth+1)
    t.forward(a)
    t.right(90)
    if depth < depth_limit - 2:
        frac(a/3,min_squares,depth_limit,depth=depth+1)
    t.forward(a)
    t.right(90)
    if depth < depth_limit - 3:
        frac(a/3,min_squares,depth_limit,depth=depth+1)
    t.forward(a)
    t.left(180)

frac(100,2)

keyboard.wait("e")