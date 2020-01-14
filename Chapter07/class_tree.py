
class BinaryTree():

    def __init__(self, root_obj, left=None, right=None, parent=None):
        self.root = root_obj
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

    def has_left_child(self):
        if self.left_child:
            return True
        else:
            return False

    def has_right_child(self):
        if self.right_child:
            return True
        else:
            return False

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_child(self):
        return self.left_child or self.right_child

    def has_both_child(self):
        return self.left_child and self.right_child

    def replace_node_data(self, root_obj, lc, rc):
        self.root = root_obj
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def __iter__(self):
        if self:
            if self.left_child:

                # for x in call the __iter__ to make the recursive call
                for elem in self.left_child:
                    yield elem
            yield self.root
            if self.right_child:
                for elem in self.right_child:
                    yield elem

    def get_left(self):
        return self.left_child

    def insert_left(self, left_child):
        old_left = self.get_left()
        self.left_child = BinaryTree(left_child)
        self.left_child.left_child = old_left

    def get_right(self):
        return self.right_child

    def insert_right(self, right_child):
        t = BinaryTree(right_child)
        t.right_child = self.right_child
        self.right_child = t

    def get_root(self):
        return self.root

    def set_root(self, root_obj):
        self.root = root_obj

    def find_min(self):
        current_node = self
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node

    def find_successor(self):
        succ = None
        if self.right_child:
            succ = self.right_child.find_min()
        else:
            if self.parent:
                # make a threaded binary tree
                if self.is_left_child():
                    succ = self.parent
                else:
                    
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        
        return succ

    # just return all nodes
    def preorder_trav(self):
        # if self.root:
        # the instance must be exist to call the method
        print(self.root)

        # check the base case whether the children is exist
        if self.left_child:
            self.left_child.preorder_trav()
        else:
            print(" ", end=" ")
        if self.right_child:
            self.right_child.preorder_trav()
        else:
            print(" ", end=" ")

        print()

    def postorder_trav(self):

        if self.left_child:
            self.left_child.postorder_trav()

        if self.right_child:
            self.right_child.postorder_trav()

        print(self.root)

    def inorder_trav(self):
 
        if self.left_child:
            self.left_child.inorder_trav()

        print(self.root)

        if self.right_child:
            self.right_child.inorder_trav()


# do something to all nodes
def preorder_trav(tree):
    if tree:
        print(tree.get_root())
        left_subtree = tree.get_left()
        right_subtree = tree.get_right()
        print(preorder_trav(left_subtree), end=" ")
        print(preorder_trav(right_subtree), end=" ")
        print()

    return "  "

def postorder_trav(tree):
    if tree:
        left_subtree = tree.get_left()
        right_subtree = tree.get_right()
        postorder_trav(left_subtree)
        postorder_trav(right_subtree)
        print(tree.get_root())

def inorder_trav(tree):
    result = ''
    if tree:
        # left_subtree = tree.get_left()
        # right_subtree = tree.get_right()
        # if left_subtree and right_subtree:
        #     return "( " + inorder_trav(left_subtree) + " " + str(tree.get_root()) + " " + inorder_trav(right_subtree) + " )"
        # else:
        #     return str(tree.get_root())
        # for each node have children will be operators, it needs a pair of parentheses
        if tree.get_left():
            result += '( ' + inorder_trav(tree.get_left())
        result += " " + str(tree.get_root()) + " "
        if tree.get_right():
            result += inorder_trav(tree.get_right()) + " )"
    return result

# how to print all node with order?


if __name__ == "__main__":
    my_tree = BinaryTree('a')

    my_tree.insert_left('b')

    my_tree.get_left().insert_right('d')

    my_tree.insert_right('c')

    my_tree.get_right().insert_right('f')
    
    my_tree.get_right().insert_left('e')

    print(my_tree.get_root(), my_tree.get_left().get_root(), my_tree.get_right().get_root())
    print(my_tree.get_left().get_right().get_root(), my_tree.get_right().get_left().get_root(), my_tree.get_right().get_right().get_root())
    print()
    print()
    print()
    # preorder_trav(my_tree)
    my_tree.preorder_trav()
    # my_tree.postorder_trav()
    # postorder_trav(my_tree)
