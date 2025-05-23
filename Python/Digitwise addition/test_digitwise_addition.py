import unittest
from digitwise_addition import digitwise_addition

class TestCalculations(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(digitwise_addition(9812, 2), 6)
    
    def test_example_2(self):
        self.assertEqual(digitwise_addition(9899, 3), 8)

if __name__ == '__main__':
    # run test in verbose mode
    unittest.main()

