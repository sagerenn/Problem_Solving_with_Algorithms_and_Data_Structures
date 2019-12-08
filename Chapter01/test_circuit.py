
from and_gate import AndGate
from or_gate import OrGate
from not_gate import NotGate
from nand_gate import NandGate
from nor_gate import NorGate
from xor_gate import XorGate
from connector import Connector
from unittest import mock
from io import StringIO
import unittest

class TestCircuit(unittest.TestCase):

    # def setUp(self):


    @mock.patch("sys.stdin", StringIO("0\n1\n1\n1\n"))
    def test_taooon_circuit(self):
        g1 = AndGate("G1")
        g2 = AndGate("G2")
        g3 = OrGate("G3")
        g4 = NotGate("G4")
        c1 = Connector(g1, g3)
        c2 = Connector(g2, g3)
        c3 = Connector(g3, g4)
        # g4.get_output() # unittest will not accept input
        self.assertEqual(g4.get_output(), 0)

    @mock.patch("builtins.input", side_effect=[0,1,1,1])
    def test_compare_not_or(self, input):
        g1 = AndGate("G1")
        g2 = AndGate("G2")
        g6 = NorGate("G6")
        c1 = Connector(g1, g6)
        c2 = Connector(g2, g6)
        self.assertEqual(g6.get_output(), 0)

    @mock.patch("builtins.input", side_effect=[0,1,1,1]) # use auto input in python code testing
    def test_compare_not_and(self, input): # set the preset input value to the function named input, each call will get all the result
        g1 = NandGate("G1")
        g2 = NandGate("G2")
        g3 = AndGate("G3")
        c1 = Connector(g1, g3)
        c2 = Connector(g2, g3)
        self.assertEqual(g3.get_output(), 0)

    @mock.patch("builtins.input", side_effect=[1,1,1,1])
    def test_half_adder(self, input):
        g1 = AndGate('G1')
        g2 = XorGate("G2")
        self.assertEqual(int(str(g1.get_output()) + str(g2.get_output()), 2), 2)

if __name__ == "__main__":
    unittest.main()