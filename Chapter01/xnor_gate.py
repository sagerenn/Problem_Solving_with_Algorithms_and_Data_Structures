from xor_gate import XorGate

class XnorGate(XorGate):
    
    def perform_gate_logic(self):
        if super().perform_gate_logic():
            return 0
        else:
            return 1
