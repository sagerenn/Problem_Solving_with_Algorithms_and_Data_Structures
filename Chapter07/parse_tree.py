import sys
import os
sys.path.append(os.path.abspath('./Chapter04'))
from stack import Stack
from class_tree import BinaryTree, inorder_trav
import re
import operator


# the operands and the right parentheses will be back to the parent
# the left parentheses and the operators will go down
# n(l+operators) + 1 = n(r+operands), it means the number of turning back will be greater than the number of pushing down
def parse_math(expr):
    expr = re.sub("([0-9]+)", r" \1 ", expr)
    expr = re.sub("([()])", r" \1 ", expr)#.replace("* *", "**")
    expr = re.sub("\s+", " ", expr).strip().split(" ")
    node_stack = Stack()
    my_tree = BinaryTree(None)
    node_stack.push(my_tree)
    current_node = node_stack.peek()
    for token in expr:
        if token == '(':
            current_node.insert_left(None)
            current_node = current_node.get_left()
            node_stack.push(current_node)
        elif token in ['-', '+', '/', '*', '%', '**', 'and', 'or', 'not']:
            current_node.set_root(token)
            current_node.insert_right(None)
            current_node = current_node.get_right()
            node_stack.push(current_node)
        elif token == ')':
            node_stack.pop()

            # if using stack to store and keep track of the nodes, the final step will try to index from empty list that will raise a indexError

            if node_stack.size() == 0:
                current_node = None
            else:
                current_node = node_stack.peek()

        else:
            try:
                current_node.set_root(int(token))
                node_stack.pop()
                current_node = node_stack.peek()
                if current_node.get_root() == 'not':
                    node_stack.pop()
                    current_node = node_stack.peek()
            except ValueError:
                raise ValueError(f"token '{token}' is not a valid integer.")

    return my_tree

def evaluate(parse_tree):
    # the base case is to reach to the leaf node
    if type(parse_tree.get_root()) is int:
        return parse_tree.get_root()
    elif parse_tree.get_root() == 'not':
        return not parse_tree.get_right()
    else:
        if parse_tree.get_root() == '+':
            return evaluate(parse_tree.get_left()) + evaluate(parse_tree.get_right())
        elif parse_tree.get_root() == '-':
            return evaluate(parse_tree.get_left()) - evaluate(parse_tree.get_right())
        elif parse_tree.get_root() == '*':
            return evaluate(parse_tree.get_left()) * evaluate(parse_tree.get_right())
        elif parse_tree.get_root() == '/':
            return evaluate(parse_tree.get_left()) / evaluate(parse_tree.get_right())
        elif parse_tree.get_root() == '**':
            return evaluate(parse_tree.get_left()) ** evaluate(parse_tree.get_right())
        elif parse_tree.get_root() == 'and':
            return evaluate(parse_tree.get_left()) and evaluate(parse_tree.get_right())
        elif parse_tree.get_root() == 'or':
            return evaluate(parse_tree.get_left()) or evaluate(parse_tree.get_right())

def postorder_evaluate(parse_tree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    # the base case is the tree is exist
    if parse_tree:

        # the result of subtrees
        left = postorder_evaluate(parse_tree.get_left())
        right = postorder_evaluate(parse_tree.get_right())

        if left and right:
            return opers[ parse_tree.get_root() ](left, right)
        else:
            return parse_tree.get_root()

def cal_express(parse_tree):
    return postorder_evaluate(parse_tree)

if __name__ == "__main__":
    # print(evaluate(parse_math("(5+(6*(7-6)))")))
    # print(postorder_evaluate(parse_math("(5+(6*(7-6)))")))
    # print(postorder_evaluate(parse_math("(5+(12/(7-5)))")))
    # print(inorder_trav(parse_math("(5+(12/(7-5)))")))
    print(parse_math("(((4*8)/6)-3)"))
