from stack import Stack
import re

class InfixEvaluator():

    def __init__(self):
        self.last_exprs = None
        self.last_result = None

    def last_express(self):
        return " ".join(map(str, self.last_exprs)) + " = " + str(self.last_result)

    # how to hide the middle function outside the class
    def str_operator(self, operator, operand_a, operand_b):
        if operator == "+":
            return operand_a + operand_b
        elif operator == "-":
            return operand_a - operand_b
        elif operator == "*":
            return operand_a * operand_b
        elif operator == "/":
            return operand_a / operand_b
        elif operator == "**":
            return operand_a ** operand_b
        elif operator == "^":
            return operand_a ** operand_b

    # calculate by converting to postfix
    def cal_postfix(self, expression):
        self.last_exprs = re.sub("([0-9]+)", r" \1 ", expression)
        self.last_exprs = re.sub("([()])", r" \1 ", self.last_exprs)#.replace("* *", "**")
        self.last_exprs = re.sub("\s+", " ", self.last_exprs).strip().split(" ")
        operand_stack = Stack()
        operator_stack = Stack()
        # how to support the operator whose length is greater than one
        operator_precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3,
            "**": 3,
            "(": 4,
            ")": 4,
        }

        # two operand or operator appear closely will be error
        for ch in self.last_exprs:
            if re.search("[0-9]", ch):
                operand_stack.push( float(ch) )
            else:
                if not operator_stack.is_empty() and operator_stack.peek() == '(':
                    operator_stack.push( ch )
                elif ch == ')':
                    while operator_stack.peek() != '(':
                        a = operand_stack.pop()
                        b = operand_stack.pop()
                        operand_stack.push( self.str_operator( operator_stack.pop(), b, a ) )
                    operator_stack.pop()
                elif not operator_stack.is_empty() and operator_precedence[ch] <= operator_precedence[ operator_stack.peek() ]:
                    while not operator_stack.is_empty() and operator_precedence[ch] <= operator_precedence[ operator_stack.peek() ] and operator_stack.peek() != '(':
                        a = operand_stack.pop()
                        b = operand_stack.pop()
                        operand_stack.push( self.str_operator( operator_stack.pop(), b, a ) )
                    operator_stack.push( ch )
                else:
                    operator_stack.push( ch )

        while not operator_stack.is_empty():
            a = operand_stack.pop()
            b = operand_stack.pop()
            operand_stack.push( self.str_operator( operator_stack.pop(), b, a ) )

        self.last_result = operand_stack.pop()
        return self.last_result

if __name__ == "__main__":
    calculator = InfixEvaluator()
    print( calculator.cal_postfix("5*(4-4*5+5)") )
    print( calculator.cal_postfix("4-4**((2+1)/3+1)*4") )
    print( calculator.last_express() )