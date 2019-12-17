from list_adt import UnorderedList
class Stack():
    """Stack Abstract Data Type"""

    def __init__(self):
        """initialize a stack"""
        self.stack = []

    def push(self, item):
        """push item to stack"""
        self.stack.append(item)

    def pop(self):
        """get the item from the top, and modified the stack"""
        return self.stack.pop()

    def peek(self):
        """get the item from the top, and don't modified the stack"""
        return self.stack[-1]

    def is_empty(self):
        """check whether the stack is empty"""
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def size(self):
        """check the length of stack"""
        return len(self.stack)

    def __repr__(self):
        """return the stack"""
        return str(self.stack)


class LinkedStack():
    def __init__(self):
        self.stack = UnorderedList()

    def push(self, item):
        self.stack.add(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.get_head()

    def is_empty(self):
        return self.stack.is_empty()

    def size(self):
        return self.stack.size()

    # Why must explicitly use the str to convert the object to string?
    def __str__(self):
        return str(self.stack)

    __repr__ = __str__