import unittest
from math_utils import calculate_factorial

class TestCalculateFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(calculate_factorial(0), 1)

    def test_factorial_of_positive_numbers(self):
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(2), 2)
        self.assertEqual(calculate_factorial(3), 6)
        self.assertEqual(calculate_factorial(4), 24)

    def test_factorial_of_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
        with self.assertRaises(ValueError):
            calculate_factorial(-5)

    def test_factorial_of_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            calculate_factorial(2.5)
        with self.assertRaises(TypeError):
            calculate_factorial("5")