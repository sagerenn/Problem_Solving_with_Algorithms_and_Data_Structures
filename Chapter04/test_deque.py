from deque_adt import Deque, LinkedDeque

def test_operations():
    # d = Deque()
    d = LinkedDeque()
    print(d.is_empty())
    d.add_front(4)
    d.add_rear('dog')
    print(d)
    d.add_front('cat')
    d.add_rear(True)
    print(d)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_front())
    print(d.remove_rear())
    print(d)


def test_palindrome_checking(test_string):
    # test_string = 'madam'
    # d = Deque()
    d = LinkedDeque()
    for ch in test_string:
        if ch != " ":
            d.add_rear(ch)

    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False

    return True

test_operations()
print( test_palindrome_checking('I madamI') )
print( test_palindrome_checking('madm') )

