"""the log gate has one input lines"""
from log_gate import LogGate

class UnaryGate(LogGate):
    """simulate the binary log gate"""
    def __init__(self,n):
        """initialize the binary gate"""
        # LogGate.__init__(self, n)

        # This is a more general mechanism, and is widely used, especially when a class has more than one parent. 
        # loose coupling to remember the name of superclass
        super(UnaryGate,self).__init__(n)
        self.pina = None

    def get_pina(self):
        """ask and get the value of pin A"""
        if self.pina == None:
            return int(input("Enter Pin A input for gate " + self.get_label() + "-->"))
        else:
            return self.pina.get_from().get_output()

    def set_next_pin(self, source):
        """get the input from the connector"""
        if self.pina == None:
            self.pina = source
        else:
            raise RuntimeError("Error: No Empty Pins")


