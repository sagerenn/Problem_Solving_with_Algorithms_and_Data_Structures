from class_tree import BinaryTree

class BinarySearchTree():

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.length()

    def __iter__(self):
        return self.root.__iter__()

    def _put(self, subtree, node):
        if subtree.get_root()[0] == node.get_root()[0]:
            subtree.root = node.get_root()
            return 0
        elif subtree.get_root()[0] > node.get_root()[0]:
            if subtree.get_left():
                return self._put(subtree.get_left(), node)
            else:
                subtree.left_child = node
                node.parent = subtree
                return 1
        else:
            if subtree.get_right():
                return self._put(subtree.get_right(), node)
            else:
                subtree.right_child = node
                node.parent = subtree
                return 1

    def put(self, key, value):
        new_node = BinaryTree([key, value])
        if self.root:
            self.size += self._put(self.root, new_node)
        else:
            self.root = new_node
            self.size += 1

    def _get(self, subtree, key):
        if subtree.root[0] == key:
            # return the node to support flexible usage
            return subtree
        elif subtree.is_leaf():
            return None
        elif subtree.root[0] > key:
            return self._get(subtree.get_left(), key)
        else:
            return self._get(subtree.get_right(), key)

    def get(self, key):
        if self.root:
            res = self._get(self.root, key)
            if res:
                return res.root[1]
            else:
                return None
        else:
            return None

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    # missing the order, cannot use to achieve the threaded search tree
    def find_successor(self, node):
        if node.left_child:
            successor = node.left_child
            while successor.get_right():
                successor = successor.get_right()
        elif node.right_child:
            successor = node.right_child
            while successor.get_left():
                successor = successor.get_left()
        return successor

    def iter_inorder_trav(self):
        least_node = self.root.find_min()
        while least_node:
            print(least_node.root)
            least_node = least_node.find_successor()

    def del_leaf(self, node):
        if node.is_left_child():
            node.parent.left_child = None
        elif node.is_right_child():
            node.parent.right_child = None

    def del_one_child(self, node):
        if node.is_left_child():
            if node.get_left():
                node.get_left().parent = node.parent
                node.parent.left_child = node.get_left()
            else:
                node.get_right().parent = node.parent
                node.parent.left_child = node.get_right()
        elif node.is_right_child():
            if node.get_left():
                node.get_left().parent = node.parent
                node.parent.right_child = node.get_left()
            else:
                node.get_right().parent = node.parent
                node.parent.right_child = node.get_right()

    def remove(self, node):
        if node.is_leaf():
            self.del_leaf(node)
        else:
            successor = self.find_successor(node)

            if successor.is_leaf():
                self.del_leaf(successor)
            else:
                self.del_one_child(successor)
            node.root = successor.root

    def delete(self, key):
        if self.size == 0:
            raise KeyError("Key Not Found")
        elif self.size == 1:
            if self.root[0] != key:
                raise KeyError("Key Not Found")
            else:
                self.root = None
                self.size -= 1
        else:
            node_remove = self._get(self.root, key)
            if node_remove:
                self.remove(node_remove)
                self.size -= 1
            else:
                raise KeyError("Key Not Found")              

    def __str__(self):
        if self.size == 0:
            return "[]"
        else:
            self.root.inorder_trav()
            return ""

    __delitem__ = delete
    __getitem__ = get
    __setitem__ = put


class AVLTree(BinarySearchTree):

    def __init__(self):
        self.root = None
        self.size = 0

    # O(log(N))
    def _put(self, tree, node):

        if tree.get_root()[0] == node.get_root()[0]:
            tree.root[1] = node.root[1]
        elif tree.get_root()[0] > node.get_root()[0]:
            if tree.left_child:
                # O(log(N))
                self._put(tree.left_child, node)
            else:
                node.parent = tree
                tree.left_child = node

                # after put the node into the tree, the balance factor can be updated based on the left or right
                # O(log(N))
                self.update_balance(tree.left_child)
        else:
            if tree.right_child:
                self._put(tree.right_child, node)
            else:
                node.parent = tree
                tree.right_child = node
                self.update_balance(tree.right_child)

    def remove(self, node):
        if node.is_leaf():

            self.del_leaf(node)

            # after deletion, the node can point to the origin parent, but the origin parent point to None
            self.update_balance_del(node)

        else:
            successor = self.find_successor(node)

            if successor.is_leaf():
                self.del_leaf(successor)
            else:
                self.del_one_child(successor)
            node.root = successor.root

            self.update_balance_del(successor)


    def update_balance_del(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:

            if node.is_left_child():
                node.parent.balance_factor -= 1
            else:
                node.parent.balance_factor += 1

            if node.parent.balance_factor == 0:
                self.update_balance(node.parent)


    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            # heavy on one side, we will need to rebalance, which occurs from bottom to top, the subtree more balance to full, and then update the heavy to parent node 
            # O(1)
            self.rebalance(node)
            return
        if node.parent:
            # update the balanced factor based on the current node's position

            if node.is_left_child():
                node.parent.balance_factor += 1
            else:
                node.parent.balance_factor -= 1

            # after changing the parent node, we can check the balanced state to continue to go up
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.left_rotation(node.left_child)

            self.right_rotation(node)
        elif node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.right_rotation(node.right_child)

            self.left_rotation(node)

    def right_rotation(self, node):

        new_root = node.left_child
        # the pair of subtree of old or new root
        node.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = node

        # the pair of parent of old or new root
        if not node.parent:
            self.root = new_root
        else:
            if node.is_left_child():
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root

        # the pair of old and new root
        new_root.parent = node.parent
        new_root.right_child = node
        node.parent = new_root
        # node.left_child = temp

        node.balance_factor = node.balance_factor - 1 - max( new_root.balance_factor, 0 )
        new_root.balance_factor = new_root.balance_factor - 1 + min( node.balance_factor, 0 )


    def left_rotation(self, node):
        new_root = node.right_child
        temp = new_root.left_child
        if not node.parent:
            self.root = new_root
        else:
            if node.is_left_child():
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root

        new_root.parent = node.parent
        new_root.left_child = node
        node.parent = new_root
        node.right_child = temp
        if temp:
            temp.parent = node
            
        node.balance_factor = node.balance_factor + 1 - min( new_root.balance_factor, 0 )
        new_root.balance_factor = new_root.balance_factor + 1 + max( node.balance_factor, 0 )


if __name__ == "__main__":
    mytree = BinarySearchTree()
    print(mytree)

    mytree[3]="red"
    print(mytree)

    mytree[4]="blue"
    mytree[6]="yellow"

    mytree[2]="at"
    mytree[5]="rr"

    mytree[4]="rhrth"

    print(mytree[6])
    print(mytree[2])
    print(mytree)
    print('-------')
    print('-------')
    print('-------')
    mytree.iter_inorder_trav()
    print('-------')
    print('-------')
    print('-------')


    del mytree[4]
    # del mytree[9]
    print(mytree)
    for i in mytree:
        print(i)