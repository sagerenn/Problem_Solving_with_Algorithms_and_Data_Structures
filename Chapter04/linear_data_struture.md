
The position of item added stays between the other elements that came before and came after it. They are distinguished by the way in which items add added and removed, in particular the location where these additions and removals occur.
1. Stacks
2. Queues
3. Deques
4. Lists

# Stack
an ordered collection of items and the addition and removal occur in the same end. First in, Last out. Stacks can be used to reverse the order of items. The order of insertion is the reverse of the order of removal.

- a stack of books on the desktop
- the thing in the cans which open only one side
- undo
- match balanced parentheses, extract function begin with '{' and end with '}'. Because the most recent opening parentheses must match the next closing symbol. The closing symbols match the opening symbols in the reverse order of their appearance.
- convert decimal number to 2/8/16 base number. f(10) = f(2/8/16) + remainder * f(-1)(2/8/16), and the order of remainder generated is reverse with the order of the 2/16/8 read. Encryption.

abstraction pros:
1. the physics implementation of an abstract data type changed will not affect the logic characteristics 

## expression, infix, prefix, postfix

The parentheses is only need on the infix to avoid the ambiguous due to the precedence. Fully parenthesize the infix and move the operators to either left or right enclosed parenthesis to get the prefix or postfix notation.

Infix     | Prefix     | POSTFIX
A + B * C | + A * B C  | A B C * +

1. the order of operands doesn't change
2. the order of operators shows the precedence of operation
3. the position of operator:

postfix --> stack, put the operator on the right and recovered by move it to the left, this is similar to the LIFO


# Queue
First In, First Out

1. task, download, print
2. movie, cafeteria
3. move like front to end, hot potato

# Deque
A list collection can be added or removed the items on both sides.

1. palindrome check('madam')

# unordered linked List
A collection of items where earch items holds a relative position with respect to the others. unordered list. The new items can be added into anywhere. The address of object will be as the reference of the before item. When we need to modify the list, we need to traverse the list. It doesn't require the large physics storage.

Optimize the abstract data type:
1. know the condiction of each method requires
2. extract one specific variable for many method to use
3. calcute the varible in each method or operation, and use in conclusion to save time to loop over every time, just like the system format the data as soon as possible in the early stage to reduce the cost of transfering and complexity in the center


# ordered linked list
The items of the list have the relative position of each other. and it sorts by some characteristic of the items that have a meaningful comparison operation.

