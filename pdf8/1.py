import turtle
import keyboard

t = turtle.Turtle()
t.speed("fastest")

def equilateral_triangle(a):
    for i in range(3):
        t.forward(a)
        t.left(120)

equilateral_triangle(50)

keyboard.wait("e")