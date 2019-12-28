import turtle

class Maze:
    def __init__(self, maze_input):
        self.mazelist = []
        self.obstacle = '+'
        self.path = 'O'
        self.tried = '.'
        self.dead_end = '-'
        row_num = 0
        for row in maze_input:
            row_list = []
            col_num = 0
            for ch in row:
                row_list.append(ch)
                if ch == 'S':
                    self.start_point = [row_num, col_num]
                col_num += 1
            row_num += 1
            self.mazelist.append(row_list)
        self.maze_size = [len(maze_input), len(maze_input[0])]
        self.maze_turtle = turtle.Turtle()
        self.maze_turtle.shape("turtle")
        self.maze_window = turtle.Screen()
        self.maze_window.setworldcoordinates(-self.maze_size[1]/2-1, \
            -self.maze_size[0]/2-1, self.maze_size[1]/2+1, self.maze_size[0]/2+1)

    def draw_maze(self):
        self.maze_turtle.speed(10)
        self.maze_window.tracer(0)
        for y in range(self.maze_size[0]):
            for x in range(self.maze_size[1]):
                if self.mazelist[y][x] == self.obstacle:
                    self.draw_box( x-self.maze_size[1]/2, -y+self.maze_size[0]/2, 'brown' )

        self.maze_turtle.color('black')
        self.maze_turtle.fillcolor('blue')
        self.maze_window.update()
        self.maze_window.tracer(1)

    def draw_box(self,x,y,color):
        self.maze_turtle.up()
        self.maze_turtle.goto(x-0.5, y-0.5)
        self.maze_turtle.color(color)
        self.maze_turtle.fillcolor(color)
        self.maze_turtle.setheading(90)
        self.maze_turtle.down()
        self.maze_turtle.begin_fill()
        for i in range(4):
            self.maze_turtle.forward(1)
            self.maze_turtle.right(90)
        self.maze_turtle.end_fill()

    def is_exit(self, row, col):
        return (row == 0 or col == 0 or \
            row == self.maze_size[0] - 1 or col == self.maze_size[1] - 1) and \
                self.mazelist[row][col] == " "

    def move_turtle(self, x, y):
        self.maze_turtle.up()
        self.maze_turtle.setheading(self.maze_turtle.towards(x, y))
        self.maze_turtle.goto(x, y)

    def update_position(self, row, col, signal=None):

        # set the signal of path walked
        if signal:
            self.mazelist[row][col] = signal
        self.move_turtle(col-self.maze_size[1]/2, -row+self.maze_size[0]/2)

        if signal == self.obstacle:
            color = 'red'
        elif signal == self.tried:
            color = 'yellow'
        elif signal == self.dead_end:
            color = 'red'
        elif signal == self.path:
            color = 'green'
        else:
            color = None

        if color:
            self.maze_turtle.dot(10, color)

    def __getitem__(self, id):
        return self.mazelist[id]

    def __str__(self):
        result = ''
        for line in self.mazelist:
            result += str(line) + '\n'
        return str(result)

def search_maze(maze, row, col):
    maze.update_position(row, col)

    # reach some obstacle to return to try other directions
    if maze[row][col] == maze.obstacle:
        return False
    if maze[row][col] == maze.tried or maze[row][col] == maze.dead_end:
        return False
    if maze.is_exit(row, col):
        maze.update_position(row, col, maze.path)
        return True
    maze.update_position(row, col, maze.tried)

    found = ( search_maze(maze, row-1, col) or search_maze(maze, row+1, col) \
        or search_maze(maze, row, col-1) or search_maze(maze, row, col+1) )
    # found = ( search_maze(maze, row, col+1) or search_maze(maze, row, col-1) \
    #     or search_maze(maze, row+1, col) or search_maze(maze, row-1, col) )
    if found:
        maze.update_position(row, col, maze.path)
    else:
        maze.update_position(row, col, maze.dead_end)

    return found

maze_input = """
++++++++++++++++++++++
+   +   ++ ++        +
      +     ++++++++++
+ +    ++  ++++ +++ ++
+ +   + + ++    +++  +
+          ++  ++  + +
+++++ + +      ++  + +
+++++ +++  + +  ++   +
+          + + S+ +  +
+++++ +  + + +     + +
++++++++++++++++++++++
"""

maze_input = maze_input.strip().splitlines()
my_maze = Maze(maze_input)
my_maze.draw_maze()
my_maze.update_position(my_maze.start_point[0], my_maze.start_point[1])
search_maze(my_maze, my_maze.start_point[0], my_maze.start_point[1])
my_maze.maze_window.exitonclick()