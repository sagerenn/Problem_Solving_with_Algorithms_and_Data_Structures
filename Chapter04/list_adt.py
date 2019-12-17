
class Node():

    def __init__(self, data):
        self.data = data
        self.reference = None

    def get_data(self):
        return self.data

    def get_reference(self):
        return self.reference

    def set_data(self, data):
        self.data = data

    def set_reference(self, reference):
        self.reference = reference

    def __str__(self):
        return str(self.data)


class UnorderedList():

    def __init__(self):
        self.head = None

        # keep track the first item added to list
        # use some specific position to optimize the time complexity
        self.last_index = -1
        self.last = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def slice(self, start=0, end=-1):
        if end == -1:
            end = self.last_index + 1
        if end <= start:
            return False
        loop_index = self.head
        count = 0
        new = UnorderedList()
        while loop_index != None and count != end:
            if count >= start and count < end:
                new.append(loop_index.get_data())
            loop_index = loop_index.get_reference()
            count += 1
        return new

    def add(self, item):
        temp = Node(item)
        if self.is_empty():
            self.last = temp
        temp.set_reference(self.head) # link the old link from the head, and make the head to link itself
        self.head = temp
        self.last_index += 1

    def size(self):
        # <class Node 1> --> A,None 
        # temp == <class Node 1> 
        # temp.get_reference() == None

        return self.last_index + 1

        # temp = self.head
        # count = 0
        # while temp != None:
        #     count += 1
        #     temp = temp.get_reference()
        # return count

    def search(self, item):
        temp = self.head
        found = False
        while temp != None and not found: # the empty list and found condition
            if temp.get_data() == item:
                found = True
            else:
                temp = temp.get_reference() # reference has only two possible result: None and object Node
        return found

    def remove(self, item):
        temp = self.head
        old = None
        if self.is_empty():
            return False
        while temp.get_data() != item:
            old = temp # it's not the list, so the temp change in the future doesn't influence the old
            temp = temp.get_reference()

        # When the first item is matched, the old will be the initial value
        # if initial with the head, the head doesn't have the set_reference method.
        if old == None:
            self.head = temp.get_reference()
        else:
            if temp == self.last:
                self.last = old
            # If the item is not in the list, the temp will be NoneType
            old.set_reference( temp.get_reference() )
        self.last_index -= 1        

    def append(self, item):
        temp = Node(item)
        # i = self.head
        # while i.get_reference() != None:
        #     i = i.get_reference()
        # temp.set_reference(i.get_reference())
        # i.set_reference(temp)

        if self.is_empty():
            self.head = temp
            self.last = temp
        else:
            self.last.set_reference( temp )
            temp.set_reference( None )
            self.last = temp
        self.last_index += 1

    def index(self, item):
        temp = self.head
        count = 0
        while temp.get_data() != item:
            count += 1
            temp = temp.get_reference()
        return count

    def insert(self, position, item):
        temp = Node(item)
        i = self.head
        count = 0
        if position == 0:
            temp.set_reference( self.head )
            self.head = temp
        elif position > 0:
            # assume the position is greater than or equal to 0
            while count != position - 1:
                count += 1
                i = i.get_reference()
                
            temp.set_reference( i.get_reference() )
            i.set_reference( temp )
        if position == self.last_index + 1:
            self.last = temp
        self.last_index += 1


    def pop(self, position=0):
        temp = self.head
        count = 0
        item = None
        if position == 0:
            item = temp.get_data()
            self.head = temp.get_reference()
        elif position > 0:
            while count != position - 1:
                count += 1
                temp = temp.get_reference()
            if position == self.last_index:
                self.last = temp
            item = temp.get_reference().get_data()
            temp.set_reference( temp.get_reference().get_reference() )

        self.last_index -= 1
        return item

    def __str__(self):
        temp = self.head
        result = '[ '
        while temp != None:
            result += str(temp.get_data()) + " "
            temp = temp.get_reference()
        result += ']'
        return result

    def get_head(self):
        return self.head.get_data()

# It seems the time complexity of many method are O(n) with the linked list.
# We can change the basic data structure to continous list to reduce the time complexity 
class OrderedList():

    def __init__(self):
        self.head = None
        self.last_index = -1

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def add(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.set_reference( self.head )
            self.head = temp
        else:
            loop_index = self.head
            count = 0
            # keep track the position at the front of the new item
            while loop_index.get_data() < item:
                count += 1
                if loop_index.get_reference() == None:
                    break
                if loop_index.get_reference().get_data() >= item:
                    break
                loop_index = loop_index.get_reference()

            # less than the first item
            if loop_index == self.head and count == 0:
                temp.set_reference(self.head)
                self.head = temp
            # greater than the last item
            elif loop_index.get_reference() == None:
                temp.set_reference(None)
                loop_index.set_reference(temp)
            else:
                temp.set_reference(loop_index.get_reference())
                loop_index.set_reference(temp)

        self.last_index += 1

    def size(self):
        return self.last_index + 1

    def pop(self, position=-1):
        if position == -1:
            position = self.last_index
        count = 0
        loop_index = self.head
        while count != position:
            count += 1
            previous = loop_index
            loop_index = loop_index.get_reference()
        previous.set_reference( loop_index.get_reference() )
        self.last_index -= 1
        return loop_index

    # use the flag variable to control the loop would be meaningful and simple, the condition and the variable should cover only one situation to avoid the ambiguity.
    def search(self, item):
        if self.is_empty():
            return False
        else:
            loop_index = self.head
            while loop_index.get_data() != item:
                if loop_index.get_data() > item:
                    return False
                elif loop_index.get_reference() == None:
                    return False
                loop_index = loop_index.get_reference()
            return True

    def index(self, item):
        if self.is_empty():
            return False
        else:
            count = 0
            loop_index = self.head
            while loop_index.get_data() != item:
                count += 1
                if loop_index.get_reference() == None:
                    return False
                loop_index = loop_index.get_reference()
            return count

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            loop_index = self.head
            result = '[ '
            while loop_index != None:
                result += str(loop_index.get_data()) + " "
                loop_index = loop_index.get_reference()
            return result + "]"


class TriNode():
    def __init__(self, data):
        self.next = None
        self.back = None
        self.data = data

    def set_next(self, Node):
        self.next = Node

    def set_back(self, Node):
        self.back = Node

    def get_next(self):
        return self.next

    def get_back(self):
        return self.back

    def get_data(self):
        return self.data

class TriUnorderedList():

    def __init__(self):
        self.head = Node(None)
        self.last_index = -1

    def is_empty(self):
        if self.head.get_data() == None:
            return True
        else:
            return False

    def add(self, item):
        temp = TriNode(item)
        self.last_index += 1
        if self.is_empty():
            self.head.set_data(temp)
            self.head.set_reference(temp)
        else:
            temp.set_next(self.head.get_data())
            self.head.get_data().set_back(temp)
            self.head.set_data(temp)

    def append(self, item):
        if self.is_empty():
            self.add(item)
        else:
            temp = TriNode(item)
            self.head.get_reference().set_next(temp)
            temp.set_back( self.head.get_reference() )
            self.head.set_reference(temp)
        self.last_index += 1
        
    def insert(self, position, item):
        if position == 0:
            self.add(item)
        elif position == self.last_index + 1:
            self.append(item)
        elif position > self.last_index + 1:
            return False
        else:
            temp = TriNode(item)
            count = 0
            self.last_index += 1
            loop_index = self.head.get_data()
            while position != count:
                loop_index = loop_index.get_next()
                count += 1

            temp.set_next( loop_index )
            temp.set_back( loop_index.get_back() )
            loop_index.get_back().set_next( temp )
            loop_index.set_back( temp )

    def size(self):
        return self.last_index + 1

    def index(self, item):
        if self.is_empty():
            return False
        else:
            loop_index = self.head.get_data()
            count = 0
            while count != self.last_index:
                if loop_index.get_data() == item:
                    return count
                loop_index = loop_index.get_next()
                count += 1

            return False

    def pop(self, position=-1):
        if position > self.last_index:
            return False
        elif self.size() == 1:
            result = self.head.get_data().get_data()
            self.head.set_data(None)
            self.head.set_reference(None)
        elif position == -1:
            result = self.head.get_reference().get_data()
            self.head.set_reference( self.head.get_reference().get_back() )
            self.head.get_reference().set_next(None)
        elif position == 0:
            result = self.head.get_data().get_data()
            self.head.set_data( self.head.get_data().get_next() )
            self.head.get_data().set_back(None)
        else:
            loop_index = self.head.get_data()
            count = 0
            while count != position:
                loop_index = loop_index.get_next()
                count += 1
            loop_index.get_back().set_next( loop_index.get_next() )
            loop_index.get_next().set_back( loop_index.get_back() )
            result = loop_index.get_data()

        self.last_index -= 1

        return result

    def remove(self, item):

        if self.is_empty():
            return False
        elif self.size() == 1:
            if self.head.get_data().get_data() == item:
                self.head.set_data(None)
                self.head.set_reference(None)
                self.last_index -= 1

            else:
                return False
        else:
            loop_index = self.head.get_data()
            count = 0
            while count != self.last_index:
                if loop_index.get_data() == item:
                    loop_index.get_back().set_next( loop_index.get_next() )
                    loop_index.get_next().set_back( loop_index.get_back() )
                    self.last_index -= 1

                    return True
                loop_index = loop_index.get_next()
                count += 1

            return False

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            result = "[ "
            loop_index = self.head.get_data()
            while loop_index != None:
                result += str(loop_index.get_data()) + " "
                loop_index = loop_index.get_next()
            result += "]"
            return result