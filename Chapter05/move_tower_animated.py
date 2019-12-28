import os
import turtle

os.environ['DISPLAY'] = ':0'

my_turtle1 = turtle.Turtle()
my_turtle2 = turtle.Turtle()
my_turtle3 = turtle.Turtle()
my_turtle4 = turtle.Turtle()
my_turtle5 = turtle.Turtle()
my_screen = turtle.Screen()

my_turtle1.up()
my_turtle2.up()
my_turtle3.up()
my_turtle4.up()


my_turtle5.up()
my_turtle5.goto(200, -10)
my_turtle5.down()
my_turtle5.goto(200, 120)
my_turtle5.up()
my_turtle5.goto(0, -10)
my_turtle5.down()
my_turtle5.goto(0, 120)
my_turtle5.up()
my_turtle5.goto(-200, -10)
my_turtle5.down()
my_turtle5.goto(-200, 120)
my_turtle5.up()
my_turtle5.hideturtle()

my_turtle1.shape("square")
my_turtle1.shapesize(1, 2)
my_turtle1.goto(-200, 60)
my_turtle2.shape("square")
my_turtle2.shapesize(1, 4)
my_turtle2.goto(-200, 40)
my_turtle3.shape("square")
my_turtle3.shapesize(1, 6)
my_turtle3.goto(-200, 20)
my_turtle4.shape("square")
my_turtle4.shapesize(1, 8)
my_turtle4.goto(-200, 0)

a, b, c = [1, my_turtle1, my_turtle2, my_turtle3, my_turtle4], [2], [3]

def move_one_tower(one_turtle, temp):
    one_turtle.goto((temp[0]-2)*200, (len(temp)-1)*20 )

def move_tower_turtle(turtle_list, one, two, three):
    if len(three) == 5:
        return True
    elif len(turtle_list) == 0:
        return False
    else:
        move_tower_turtle(turtle_list[:-1], one, three, two)
        move_one_tower(turtle_list[-1], three)
        three.append(one.pop())
        move_tower_turtle(turtle_list[:-1], two, one, three)

my_turtle1.speed(3)
my_turtle2.speed(3)
my_turtle3.speed(3)
my_turtle4.speed(3)
move_tower_turtle([my_turtle1, my_turtle2, my_turtle3, my_turtle4], a, b, c)

my_screen.exitonclick()
# turtle.shapesize(5, 5, 12)