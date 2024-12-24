import unittest
from main import sum_nested_numbers

class TestCalculations(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(sum_nested_numbers([0]), 0)

    def test_flat_list(self):
        self.assertEqual(sum_nested_numbers([1, 2, 3, 4, 5]), 15)

    def test_nested_list(self):
        self.assertEqual(sum_nested_numbers([1, [2], 3, [4, [5]]]), 149)

    def test_deeply_nested_list(self):
        self.assertEqual(sum_nested_numbers([6, [5], [[4]], [[[3]]], [[[[2]]]], [[[[[1]]]]]]), 209)

    def test_mixed_signs(self):
        self.assertEqual(sum_nested_numbers([1, [-1], [[1]], [[[-1]]], [[[[1]]]]]), 5)

if __name__ == '__main__':
    # run test in verbose mode
    unittest.main()

