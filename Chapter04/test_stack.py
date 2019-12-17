import unittest
from stack import Stack, LinkedStack

class TestStack(unittest.TestCase):

    def setUp(self):
        # self.stack = Stack()
        self.stack = LinkedStack()

    def test_stack_method(self):
        print(self.stack.is_empty())
        self.stack.push(4)
        self.stack.push('dog')
        print(self.stack.peek())
        self.stack.push(True)
        print(self.stack.size())
        print(self.stack.is_empty())
        self.stack.push(8.4)
        print(self.stack.pop())
        print(self.stack.pop())
        print(self.stack.size())
        print(repr(self.stack))

    def test_reverse(self):
        for i in 'LEARNPYTHON':
            self.stack.push(i)
        result_str = ''
        while not self.stack.is_empty():
            result_str += self.stack.pop()
        print(result_str)
        self.assertEqual(result_str, "NOHTYPNRAEL")

    def test_balanced_parentheses(self):

        test_expression = '(5+6)∗(7+8}/(4+3)'
        open_symbols = "[{("
        close_symbols = "]})"
        for ch in test_expression:
            if ch in open_symbols:
                self.stack.push(ch)
            elif ch in close_symbols and self.stack.is_empty():
                print('False')
                return
            elif ch in close_symbols:

                # simulate dictionary using by two list
                if open_symbols.index(self.stack.peek()) == close_symbols.index(ch):
                    self.stack.pop()
                else:
                    print('False')
                    return
        if self.stack.is_empty():
            print('True')
        else:
            print('False')

    def test_convert_base_number(self):
        print("--------------")

        test_num = 96
        base = 2
        hex_char = '0123456789ABCDEF'
        bin_num = bin(test_num).replace('0b','')

        while test_num > 0:
            self.stack.push(hex_char[test_num % base])
            test_num = test_num // base
            # if test_num < 2:
            #     self.stack.push(test_num)

        result_num = ''
        while not self.stack.is_empty():
            result_num += str(self.stack.pop())
        print(result_num)
        print("--------------")

        # self.assertEqual(result_num, bin_num)

    def test_postfix(self):
        test_expression = "A + ( ( B + C ) * ( D + E ) )"
        test_expression = test_expression.split()
        result_string = ""
        operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '**': 3,
            '(': 0,
            ')': 0,
        }
        # operators = '+-/*()'
        # priority = '112200'

        for ch in test_expression:
            if ch not in operators:
                result_string += ch + " "
            elif ch == ')':
                tmp_ch = self.stack.pop()
                while tmp_ch != '(' and not self.stack.is_empty():
                    result_string += tmp_ch + " "
                    tmp_ch = self.stack.pop()
            elif ch == '(':
                self.stack.push(ch)
            else:
                while not self.stack.is_empty() and operators[self.stack.peek()] >= operators[ch]:
                    tmp_ch = self.stack.pop()
                    result_string += tmp_ch + " "
                
                self.stack.push(ch)

        while not self.stack.is_empty():
            tmp_ch = self.stack.pop()
            result_string += tmp_ch + " "
        print("~~~~~~~~~~~")
        print(result_string)
        print("~~~~~~~~~~~")

    def test_postfix_infix(self):
        postfix = '12345*+*+'
        operators = ['+', '-', '/', '*', '(', ')', '**']
        for ch in postfix:
            if ch not in operators:
                self.stack.push(ch)
            elif ch in operators:
                a_string = self.stack.pop()
                b_string = self.stack.pop()
                self.stack.push( " ( " + b_string + ch + a_string + " ) " )
        print("~~~~~~~~~~~")
        print(self.stack.pop())
        print("~~~~~~~~~~~")



if __name__ == '__main__':
    unittest.main()

