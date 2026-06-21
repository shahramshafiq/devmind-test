import unittest
from math_utils import calculate_factorial

class TestCalculateFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(calculate_factorial(0), 1)

    def test_factorial_of_positive_integers(self):
        self.assertEqual(calculate_factorial(5), 120)

    def test_input_validation_negative_integer(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

    def test_input_validation_non_integer(self):
        with self.assertRaises(TypeError):
            calculate_factorial(3.5)

if __name__ == '__main__':
    unittest.main()