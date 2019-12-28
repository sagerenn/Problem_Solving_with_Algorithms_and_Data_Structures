import turtle
import os
os.environ['DISPLAY'] = '127.0.0.1:0.0'
os.chdir( os.path.dirname( __file__ ) )
my_turtle = turtle.Turtle()
my_window = turtle.Screen()

def draw_triangle(points, color, t):
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def get_mid(p1, p2):
    return [ (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 ]

def sierpinski(points, degree, my_turtle):
    colormap = ['red', 'green', 'blue', 'yellow', 'black', 'white']
    draw_triangle(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski( [
                points[0],
                get_mid(points[0], points[2]), 
                get_mid(points[1], points[0]),
                ], degree - 1, my_turtle )
        sierpinski( [
                points[1],
                get_mid(points[0], points[1]), 
                get_mid(points[1], points[2]),
                ], degree - 1, my_turtle )
        sierpinski( [
                points[2],
                get_mid(points[0], points[2]), 
                get_mid(points[1], points[2]),
                ], degree - 1, my_turtle )

def main():
    points = [
        [-300, -150],
        [0,300],
        [300, -150],
    ]
    sierpinski(points, 4, my_turtle)
    my_window.exitonclick()

main()

