import sys
import os
sys.path.append(os.path.abspath('./Chapter04'))
from stack import Stack


def move_disk(from_pole, to_pole, steps):
    print("moving disk from ",from_pole," to ",to_pole)
    to_pole.push(from_pole.pop())
    steps.append("moving disk from " + str(from_pole) + " to " + str(to_pole) )


def move_tower(height, from_pole, to_pole, with_pole, steps):
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole, steps)
        move_disk(from_pole, to_pole, steps)
        move_tower(height-1, with_pole, to_pole, from_pole, steps)

def main():
    from_pole = Stack()
    with_pole = Stack()
    to_pole = Stack()
    steps = []
    height = 5
    for i in range(height):
        from_pole.push((height + 1 - i) * 20)
    print(from_pole, with_pole, to_pole)
    move_tower(height, from_pole, to_pole, with_pole, steps)
    print(from_pole, with_pole, to_pole, len(steps))

main()