"""the superclass of log gate"""

class LogGate:
    """simulate a digit log gate"""

    def __init__(self, n):
        """get the initial value of instance"""
        self.label = n
        self.output = None

    def get_label(self):
        """return the label"""
        return self.label

    def get_output(self):
        """retrieve the output from the input"""
        self.output = self.perform_gate_logic()
        return self.output