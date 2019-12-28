from turtle import Screen, Turtle
import os

os.environ['DISPLAY'] = ':0'


def hilbert_curve(turtle, A, parity, n):

    if n < 1:
        return

    turtle.left(parity * 90)
    hilbert_curve(turtle, A, - parity, n - 1)
    turtle.forward(A)
    turtle.right(parity * 90)
    hilbert_curve(turtle, A, parity, n - 1)
    turtle.forward(A)
    hilbert_curve(turtle, A, parity, n - 1)
    turtle.right(parity * 90)
    turtle.forward(A)
    hilbert_curve(turtle, A, - parity, n - 1)
    turtle.left(parity * 90)

screen = Screen()

yertle = Turtle()
yertle.speed('fastest')  # because I have no patience

hilbert_curve(yertle, 10, 1, 3)

screen.exitonclick()