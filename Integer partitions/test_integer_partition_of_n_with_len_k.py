import unittest
from integer_partition_of_n_with_len_k import integer_partition_of_n_with_len_k

class TestCalculations(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(integer_partition_of_n_with_len_k(10,3,3), 5)
    

if __name__ == '__main__':
    # run test in verbose mode
    unittest.main()

