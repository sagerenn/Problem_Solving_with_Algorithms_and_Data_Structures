from list_adt import UnorderedList

class Deque():

    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0)

    def remove_rear(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def __repr__(self):
        return str(self.deque)


class LinkedDeque():

    def __init__(self):
        self.deque = UnorderedList()

    def add_front(self, item):
        self.deque.add(item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop()

    # O(n)
    def remove_rear(self):
        return self.deque.pop( self.deque.last_index )

    def size(self):
        return self.deque.size()

    def is_empty(self):
        return self.deque.is_empty()

    def __repr__(self):
        return str(self.deque)