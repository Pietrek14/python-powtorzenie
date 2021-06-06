import turtle
import keyboard

def new_turtle(x,y):
    newTurtle = turtle.Turtle()
    newTurtle.speed("fastest")
    newTurtle.penup()
    newTurtle.goto(x,y)
    newTurtle.pendown()

    return newTurtle

t = new_turtle(-100, -100)
t.speed("fastest")

def frac(a, depth=5):
    if depth < 3:
        return
    
    angle = ((depth-2)*180)/depth
    t.left(angle)
    frac(a/3,depth-1)
    t.forward(a)
    for i in range(depth-2):
        t.right(180-angle)
        frac(a/3,depth-1)
        t.forward(a)
    t.right(180-angle)
    t.forward(a)
    t.left(180)

frac(200)

keyboard.wait("e")