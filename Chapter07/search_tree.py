from class_tree import BinaryTree

class SearchTree(BinaryTree):

    def __init__(self, key=None, value=None):
        if key:
            
            self.root = [key, value]
            self.size = 1
        else:
            self.root = None
            self.size = 0
        self.left_child = None
        self.right_child = None

        # for use of deletion
        self.parent = None

    def get_root(self):
        return self.root

    def insert_left(self, left_child):
        raise Exception("Not method")

    def insert_right(self, right_child):
        raise Exception("Not method")

    def tree_size(self):
        return self.size

    def get(self, key):
        if self.size == 0:
            return None
        elif self.root[0] == key:
            return self
        elif self.root[0] < key:
            if self.right_child:
                return self.right_child.get(key)
            else:
                return None
        else:
            if self.left_child:
                return self.left_child.get(key)
            else:
                return None

    def put(self, key, value):
        if self.size == 0:
            self.root = [key, value]
        elif self.root[0] == key:
            self.root[1] = value
        elif self.root[0] < key:
            if self.right_child:
                self.right_child.put(key, value)
            else:
                temp = SearchTree(key, value)
                self.right_child = temp
                temp.parent = self
        else:
            if self.left_child:
                self.left_child.put(key, value)
            else:
                temp = SearchTree(key, value)
                self.left_child = temp
                temp.parent = self

        self.size += 1


    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        else:
            return True

    def is_left_child(self):
        if self.parent.left_child == self:
            return True
        else:
            return False

    def is_right_child(self):
        if self.parent.right_child == self:
            return True
        else:
            return False

    def del_leaf(self, is_root=False):
        if is_root:
            self.root = None
        elif self.is_left_child():
            self.parent.left_child = None
        else:
            self.parent.right_child = None

    def del_one_child(self, is_root=False):
        if is_root:
            if self.left_child:
                self.left_child = self.left_child.left_child
                self.right_child = self.left_child.right_child
                self.root = self.left_child.root
                self.size = self.left_child.size

            elif self.right_child:
                self.left_child = self.right_child.left_child
                self.right_child = self.right_child.right_child
                self.root = self.right_child.root
                self.size = self.right_child.size

        elif self.is_left_child():
            if self.left_child:
                self.parent.left_child = self.left_child
            elif self.right_child:
                self.parent.left_child = self.right_child
        elif self.is_right_child():
            if self.left_child:
                self.parent.right_child = self.left_child
            elif self.right_child:
                self.parent.right_child = self.right_child


    def del_two_child(self):
        # if self.left_child:
        successor = self.left_child
        if successor.is_leaf():
            successor.del_leaf()
        
        elif not successor.right_child:
            self.del_one_child()
        else:
            while successor.get_right():
                successor = successor.get_right()

            if successor.is_leaf():
                successor.del_leaf()
            else:
                successor.del_one_child()

        self.root = successor.root


    def __delitem__(self, key):
        temp = self.get(key)
        if temp:
            if temp.parent == None:
                is_root = True
            else:
                is_root = False

            if temp.is_leaf():
                temp.del_leaf(is_root=is_root)
            elif temp.left_child and temp.right_child:
                temp.del_two_child()
            else:
                temp.del_one_child(is_root=is_root)

            self.size -= 1
        else:
            raise Exception("Not found")

    def __getitem__(self, key):
        if self.size == 0:
            return None
        elif self.root[0] == key:
            return self.root[1]
        elif self.root[0] < key:
            if self.right_child:
                return self.right_child[key]
            else:
                return None
        else:
            if self.left_child:
                return self.left_child[key]
            else:
                return None

    def __str__(self):
        if self.size == 0:
            return "[]"
        else:
            super().inorder_trav()
            return ""

    __setitem__ = put

if __name__ == "__main__":
    mytree = SearchTree()
    print(mytree)

    mytree[3]="red"
    print(mytree.get_root())

    mytree[4]="blue"
    mytree[6]="yellow"
    print(mytree.get_root(), mytree.get_left(), mytree.get_right())

    mytree[2]="at"
    mytree[5]="rr"

    mytree[4]="rhrth"

    print(mytree[6])
    print(mytree[2])
    print(mytree)

    del mytree[4]
    # del mytree[9]
    print(mytree, mytree.get_root())
