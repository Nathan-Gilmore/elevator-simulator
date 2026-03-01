from argparse import ArgumentTypeError
import unittest

from elevator import main, list_floors

class TestElevator(unittest.TestCase):
    def test_expected_outputs(self):
        start = 12
        floor = [2,9,1,32]
        [time, allFloorsStr] = main(start, floor)
        
        assert time == 560
        assert allFloorsStr == "12,2,9,1,32"


    def test_expected_outputs_negatives(self):
        start = -12
        floor = [2,9,-1,32]
        [time, allFloorsStr] = main(start, floor)
        
        assert time == 640
        assert allFloorsStr == "-12,2,9,-1,32"

    
    def test_invalid_input(self):
        input = "2,9,e,32"
        try:
            list_floors(input)
            raise Exception("Unexpected Error")
        except ArgumentTypeError as e:
            assert str(e) == f"Invalid --floor value '{input}'. Expected comma-separated integers like 2,9,1,32"

    
    def test_invalid_empty_input(self):
        input = ""
        try:
            list_floors(input)
            raise Exception("Unexpected Error")
        except ArgumentTypeError as e:
            assert str(e) == f"Invalid --floor value '{input}'. Expected comma-separated integers like 2,9,1,32"


    def test_invalid_decimal_input(self):
        input = "2,9.5,1,32"
        try:
            list_floors(input)
            raise Exception("Unexpected Error")
        except ArgumentTypeError as e:
            assert str(e) == f"Invalid --floor value '{input}'. Expected comma-separated integers like 2,9,1,32"


if __name__ == '__main__':
    unittest.main()