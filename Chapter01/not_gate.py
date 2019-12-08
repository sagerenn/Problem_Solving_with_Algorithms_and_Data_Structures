"""simulate not logic"""
from unary_gate import UnaryGate

class NotGate(UnaryGate):

    def __init__(self, n):
        """initialize a not digit circuit"""
        super(NotGate, self).__init__(n)

    def perform_gate_logic(self):
        """implement not logic"""
        if self.get_pina() == 1:
            return 0
        else:
            return 1
