from list_adt import Node
class Queue():

    def __init__(self):
        self.queue = []

    # the end of list is the rear of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # # the begin of list is the rear of the queue
    # def enqueue(self. item):
    #     self.queue.insert(0, item)

    # def dequeue(self):
    #     self.queue.pop()

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return str(self.queue)

# use the circularly linked list to implement the queue with operations that can be performed in constant time
# use fixed size list and two loop variable to implement
class ConstantQueue():

    def __init__(self):
        # use one variable to store the second last item with the circularly linked list
        self.head = None
        self.rear = None
        self.queue_size = 0

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        return self.queue_size

    def enqueue(self, item):
        temp = Node(item)
        if not self.is_empty():
            self.rear.set_reference( temp )
        else:
            self.head = temp
        temp.set_reference(None)
        self.rear = temp
        self.queue_size += 1
    
    def dequeue(self):
        if self.size() == 1:
            self.rear = None
        result = self.head.get_data()
        self.head = self.head.get_reference()
        self.queue_size -= 1
        return result