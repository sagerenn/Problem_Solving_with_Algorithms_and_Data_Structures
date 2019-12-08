from or_gate import OrGate

class NorGate(OrGate):

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1