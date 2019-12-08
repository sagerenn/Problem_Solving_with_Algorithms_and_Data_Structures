
from binary_gate import BinaryGate

class NandGate(BinaryGate):

    def __init__(self, n):

        super(NandGate, self).__init__(n)

    def perform_gate_logic(self):
        """implement and logic"""
        if self.get_pina() == 1 and self.get_pinb() == 1:
            return 0
        else:
            return 1
