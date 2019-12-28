
# https://repl.it/languages/python_turtle 
# sudo apt-get install python3-tk tk-dev x11-apps
# https://sourceforge.net/projects/xming/ install on Windows
# sudo apt install imagemagick ghostscript

import turtle
import os
os.environ['DISPLAY'] = '127.0.0.1:1.0'
os.chdir( os.path.dirname( __file__ ) )

my_turtle = turtle.Turtle()
my_window = turtle.Screen()

def draw_spiral(my_turtle, line_length):
    if line_length > 0:
        my_turtle.forward(line_length)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_length-5)

draw_spiral(my_turtle, 100)


# my_window.getcanvas().postscript(file="test.eps")

# sudo sed -i_bak \
# 's/rights="none" pattern="PDF"/rights="read | write" pattern="PDF"/' \
# /etc/ImageMagick-6/policy.xml

# os.system("convert test.eps test.gif")
my_window.exitonclick()
