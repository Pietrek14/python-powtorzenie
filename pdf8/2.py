import turtle
import keyboard

t = turtle.Turtle()
t.speed("fastest")

def frac(a, depth_limit=50, depth=0):
    if depth == depth_limit:
        return

    for i in range(4):
        t.forward(a)
        t.left(90)
    
    frac(0.9 * a, depth_limit, depth+1)

frac(200)

keyboard.wait("e")