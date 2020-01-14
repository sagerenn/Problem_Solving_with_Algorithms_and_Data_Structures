import json

def test_list_tree():
    my_tree = [
        'a',
        [
            'b',
            [
                'd', [], []
            ],
            [
                'e', [], []
            ]
        ],
        [
            'c',
            [
                'f', [], []
            ],
            []
        ]
    ]

    print("root: " + my_tree[0])
    print("left_subtree: ", my_tree[1])
    print("right_subtree: ", my_tree[2])

def binary_tree(root):
    return [root, [], []]

def insert_left_node(tree_list, new_node):
    temp = tree_list[1]
    tree_list[1] = [new_node, temp, []]
    return tree_list

def insert_right_node(tree_list, new_node):
    temp = tree_list[2]
    tree_list[2] = [new_node, [], temp]
    return tree_list

def get_root(tree_list):
    return tree_list[0]

def set_root(tree_list, new_node):
    tree_list[0] = new_node

def get_left_child(tree_list):
    return tree_list[1]

def get_right_child(tree_list):
    return tree_list[2]

if __name__ == "__main__":
    # test_list_tree()
    # my_tree = binary_tree(3)
    # insert_left_node(my_tree, 4)
    # insert_left_node(my_tree, 5)
    # insert_right_node(my_tree, 6)
    # insert_right_node(my_tree, 7)
    # print(json.dumps(get_left_child(my_tree), indent=4))
    # print(json.dumps(my_tree, indent=4))
    # set_root(my_tree, 9)
    # print(json.dumps(my_tree, indent=4))
    # insert_left_node(my_tree, 11)
    # print(json.dumps(my_tree, indent=4))

    # print(json.dumps(get_right_child(get_right_child(my_tree)), indent=4))

    x = binary_tree('a')
    insert_left_node(x, 'b')
    insert_right_node(x, 'c')
    insert_right_node(get_left_child(x), 'd')
    insert_right_node(get_right_child(x), 'f')
    insert_left_node(get_right_child(x), 'e')

    print(json.dumps(x, indent=4))
