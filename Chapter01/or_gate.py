"""simulate or logic"""
from binary_gate import BinaryGate

class OrGate(BinaryGate):

    def __init__(self, n):
        """initialize a or digit circuit"""
        super(OrGate, self).__init__(n)

    def perform_gate_logic(self):
        """implement or logic"""
        a = self.get_pina()
        b = self.get_pinb()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
