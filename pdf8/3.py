import turtle
import keyboard

def new_turtle(x,y):
    newTurtle = turtle.Turtle()
    newTurtle.speed("fastest")
    newTurtle.penup()
    newTurtle.goto(x,y)
    newTurtle.pendown()

    return newTurtle

def sierpinski_triangle(t, a, depth_limit=6, depth=0,dir=False):
    if depth == depth_limit:
        t.hideturtle()
        return
    
    sierpinski_triangle(new_turtle(t.pos()[0], t.pos()[1]), a/2, depth_limit, depth+1)
    t.forward(a/2)
    sierpinski_triangle(new_turtle(t.pos()[0], t.pos()[1]), a/2, depth_limit, depth+1)
    t.forward(a/2)
    t.left(120)
    t.forward(a)
    t.left(120)
    t.forward(a/2)
    sierpinski_triangle(new_turtle(t.pos()[0], t.pos()[1]), a/2, depth_limit, depth+1)
    t.forward(a/2)
    t.hideturtle()

sierpinski_triangle(new_turtle(-200,-200), 400)

keyboard.wait("e")