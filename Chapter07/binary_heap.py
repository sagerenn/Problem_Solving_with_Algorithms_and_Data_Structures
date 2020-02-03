import random
import math

class BinHeap():

    def __init__(self):
        # the item in the heap will start from 1 to fulfill the position relationship with parent and child.
        self.heap = [0]
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0 and self.heap[i//2][0] > self.heap[i][0]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        temp = self.size

        # compare with parent node, exchange when the parent is larger
        while temp // 2 > 0 and self.heap[temp//2][0] > self.heap[temp][0]:
            self.heap[temp], self.heap[temp//2] = self.heap[temp//2], self.heap[temp]
            temp = temp//2

    def min_index(self, i, j):
        if self.heap[i][0] <= self.heap[j][0]:
            return i
        elif self.heap[j][0] <= self.heap[i][0]:
            return j

    def get_left(self, i):
        if 2*i <= self.size:
            return 2*i

    def get_right(self, i):
        if 2*i + 1 <= self.size:
            return 2*i + 1

    def get_size(self):
        return self.size

    def get_list(self):
        return self.heap

    # compare the left and the right child
    def min_child(self, i):
        if 2*i > self.size:
            return None
        elif 2*i + 1 > self.size:
            return 2*i
        else:
            if self.heap[2*i][0] > self.heap[2*i + 1][0]:
                return 2*i + 1
            else:
                return 2*i

    def percolate_down(self, i):
        while i*2 <= self.size:
            t = self.min_child(i)
            if self.heap[i][0] > self.heap[t][0]:
                self.heap[i], self.heap[t] = self.heap[t], self.heap[i]
            else:
                break
                
            i = t

    # O(n), the percolating operation will cover all the interior nodes that has leaf nodes to compare the root, the left subtree and the right subtree to find the min nodes
    def build_heap(self, item_list):
        parent_node = len(item_list) // 2
        self.size = len(item_list)
        self.heap = [0] + item_list
        while parent_node > 0:
            self.percolate_down(parent_node)
            parent_node -= 1


    def del_min(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            temp = self.heap.pop()
            self.size -= 1
        else:
            self.size -= 1
            temp = self.heap[1]
            self.heap[1] = self.heap.pop()
            i = 1
            min_i = None
            while ( self.get_left(i) or self.get_right(i) ):
                if self.get_left(i):
                    min_i = self.min_index(i, self.get_left(i))
                if self.get_right(i):
                    min_i = self.min_index(min_i, self.get_right(i))
                if i != min_i:
                    self.heap[i], self.heap[min_i] = self.heap[min_i], self.heap[i]
                    i = min_i
                else:
                    break

        return temp

    def decrease_element(self, old, new):
        for i in range(1, self.size+1):
            if self.heap[i] == old:
                self.heap[i] = new
                self.percolate_up(i)
                break

    def __contains__(self, item):
        for i in self.heap:
            if i == item:
                return True

        return False

class BinMaxHeap():

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, index):
        if index // 2 > 0:
            if self.heap[index] > self.heap[index//2]:
                temp = self.heap[index//2]
                self.heap[index//2] = self.heap[index]
                self.heap[index] = temp
                self.percolate_up(index//2)

    def max_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap[index * 2 + 1] > self.heap[index * 2]:
                return index * 2 + 1
            else:
                return index * 2

    def percolate_down(self, index):
        if index * 2 <= self.size:
            max_child = self.max_child(index)
            if self.heap[index] < self.heap[max_child]:
                temp = self.heap[index]
                self.heap[index] = self.heap[max_child]
                self.heap[max_child] = temp
                self.percolate_down(max_child)

    def del_max(self):
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.percolate_down(1)
        return result

    def build_heap(self, item_list):
        self.heap = [0] + item_list
        self.size = len(item_list)
        parent_index = len(item_list) // 2
        while parent_index > 0:
            self.percolate_down(parent_index)
            parent_index -= 1

    def get_size(self):
        return self.size

    def get_list(self):
        return self.heap

class FixBinMaxHeap(BinMaxHeap):

    def __init__(self, fix_value):
        super().__init__()
        self.fix_size = fix_value

    # O(n)
    # maybe we can maintain another max heap list to find the max heap to retrieve O(log N)
    def find_min(self):
        loop = self.size // 2
        min = loop
        while loop <= self.size:
            if self.heap[loop] < self.heap[min]:
                min = loop
            loop += 1
        return min

    def insert(self, item):
        if self.size == self.fix_size:
            min_index = self.find_min()
            if item > self.heap[min_index]:
                self.heap[min_index] = item
                self.percolate_up(min_index)
        else:
            super().insert(item)


class PriorityQueue():

    def __init__(self):
        self.heap = BinHeap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.del_min()

    def __len__(self):
        return self.heap.get_size()


def heap_sort(num_list):
    num_heap = BinHeap()
    num_heap.build_heap(num_list)
    i = 0
    while num_heap.get_size() > 0:
        num_list[i] = num_heap.del_min()
        i += 1
    return num_list

def level_print(width, num, item_list):
    if num == 0:
        print(" " * (width//2), end="")
        print(item_list.pop(0), end="")
        print(" " * ((width-1)//2) )
    else:
        pairs = 2**(num-1)
        print(" " * ((width - pairs*3 - (pairs-1)*3 )//2), end="")
        while item_list:
            print(str(item_list.pop(0))+ " ", end="")
            if item_list:
                print(item_list.pop(0), end="")
            print(" " * 3, end="")
        print()
            

def print_heap(heap_list):
    width = 3 * (len(heap_list) - 1) - 3
    current_level = 0
    temp = []
    for i in range(1, len(heap_list)):
        if int(math.log(i, 2)) != current_level:
            level_print(width, current_level, temp)
            temp = [heap_list[i]]
            current_level += 1
        elif i == len(heap_list) - 1:
            temp.append(heap_list[i])
            level_print(width, current_level, temp)
        else:
            temp.append(heap_list[i])


if __name__ == "__main__":
    bh = BinHeap()
    bhm = BinMaxHeap()
    pq = PriorityQueue()
    fb = FixBinMaxHeap(10)
    # bh.build_heap([9,5,6,2,3])

    # print(bh.del_min())
    # print(bh.del_min())
    # print(bh.del_min())
    # print(bh.del_min())
    # print(bh.del_min())

    temp = []
    temp2 = []
    for i in range(10):
        m = random.randint(0, 1000)
        # m = i
        temp.append(m)
        bh.insert(m)
        pq.enqueue(m)
        temp2.append(m)
    print(temp)
    
    print(bh.get_list())
    print()
    print()
    print()
    print_heap(bh.get_list())
    print()
    print()

    bh.build_heap(temp)
    print(bh.get_list())
    print()
    print()
    print()

    print_heap(bh.get_list())

    print()
    print()
    while len(pq) > 0:
        print(pq.dequeue())


    print(heap_sort(temp))

    bhm.build_heap(temp2)
    print(bhm.get_list())
    print_heap(bhm.get_list())
    fb.build_heap(temp2)
    print(fb.get_list())
    fb.insert(0)
    fb.insert(10001)
    print(fb.get_list())

