import unittest
from main import square_digits_sequence

sample_test_cases = [
    ( 16,  9),
    (103,  4),
    (  1,  2),
    ( 86,  4),
    (  6, 18),
]

class TestCalculations(unittest.TestCase):

    for n, expected in sample_test_cases:
        def test(self, n=n, expected=expected):
            self.assertEqual(square_digits_sequence(n), expected)

if __name__ == '__main__':
    # run test in verbose mode
    unittest.main()

