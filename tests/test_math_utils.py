import unittest
from math_utils import calculate_factorial

class TestCalculateFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(calculate_factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(calculate_factorial(1), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(calculate_factorial(5), 120)

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

    def test_factorial_of_non_integer(self):
        with self.assertRaises(TypeError):
            calculate_factorial(2.5)

if __name__ == '__main__':
    unittest.main()