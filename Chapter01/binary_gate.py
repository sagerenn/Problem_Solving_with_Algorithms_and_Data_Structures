"""the log gate has two input lines"""
from log_gate import LogGate

class BinaryGate(LogGate):
    """simulate the binary log gate"""
    def __init__(self,n):
        """initialize the binary gate"""
        LogGate.__init__(self, n)
        self.pina = None
        self.pinb = None

    def get_pina(self):
        """ask and get the value of pin A"""
        if self.pina == None:
            return int(input("Enter Pin A input for gate " + self.get_label() + "-->"))
        else:
            return self.pina.get_from().get_output()

    # import from the external or the connector which provide a gate
    def get_pinb(self):
        """ask and get the value of pin B"""
        if self.pinb == None:
            return int(input("Enter Pin B input for gate " + self.get_label() + "-->"))
        else:
            return self.pina.get_from().get_output()

    def set_next_pin(self, source):
        """get the input from the connector"""
        if self.pina == None:
            self.pina = source
        elif self.pinb == None:
            self.pinb = source
        else:
            raise RuntimeError("Error: No Empty Pins")

