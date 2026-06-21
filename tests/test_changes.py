import unittest
from math_utils import calculate_factorial

class TestCalculateFactorialEdgeCases(unittest.TestCase):
    def test_large_inputs(self):
        self.assertEqual(calculate_factorial(10), 3628800)
        self.assertEqual(calculate_factorial(15), 1307674368000)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            calculate_factorial(float("inf"))
        with self.assertRaises(ValueError):
            calculate_factorial(float("-inf"))
        with self.assertRaises(ValueError):
            calculate_factorial(None)

if __name__ == '__main__':
    unittest.main()