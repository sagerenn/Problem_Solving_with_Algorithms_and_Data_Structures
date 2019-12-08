"""simulate and logic"""
from binary_gate import BinaryGate

class AndGate(BinaryGate):

    def __init__(self, n):
        """initialize a and digit circuit"""
        super(AndGate, self).__init__(n)

    def perform_gate_logic(self):
        """implement and logic"""
        if self.get_pina() == 1 and self.get_pinb() == 1:
            return 1
        else:
            return 0
