from binary_gate import BinaryGate

class XorGate(BinaryGate):

    def __init__(self, n):
        """initialize a or digit circuit"""
        super(XorGate, self).__init__(n)

    def perform_gate_logic(self):
        """implement or logic"""
        a = self.get_pina()
        b = self.get_pinb()
        if a == b:
            return 0
        else:
            return 1