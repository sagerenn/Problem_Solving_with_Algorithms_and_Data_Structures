import turtle
import os
import random
import time

# export DISPLAY=localhost:0.0

os.environ['Display'] = 'localhost:0.0'


# how to convert to iteration?
def tree(branch_length, width, turtle_i):
    if branch_length > 5 and width > 0:
        if branch_length - 15 <= 5 or width - 3 <= 0:
            turtle_i.color("green")
        else:
            turtle_i.color("brown")
        turtle_i.width(width)
        turtle_i.forward(branch_length)

        rand_right = random.randint(15,45)
        rand_left = random.randint(15,45)
        rand_llen = random.randint(12,18)
        rand_rlen = random.randint(12,18)

        turtle_i.right(rand_right)
        # turtle_i.forward(branch_length-10)
        tree(branch_length-rand_rlen, width-3, turtle_i)
        # turtle_i.backward(branch_length-10)

        turtle_i.left(rand_left + rand_right)
        # turtle_i.forward(branch_length-10)
        tree(branch_length-rand_llen, width-3, turtle_i)
        # turtle_i.backward(branch_length-10)

        turtle_i.right(rand_left)
        if branch_length - 15 <= 5 or width - 3 <= 0:
            turtle_i.color("green")
        else:
            turtle_i.color("brown")
        turtle_i.backward(branch_length)

def main():
    time.sleep(5)
    turtle_i = turtle.Turtle()
    turtle_w = turtle.Screen()
    turtle_i.left(90)
    turtle_i.up()
    turtle_i.backward(150)
    turtle_i.down()
    tree(100, 20, turtle_i)
    turtle_w.exitonclick()

main()