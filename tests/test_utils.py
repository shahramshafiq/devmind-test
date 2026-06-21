import unittest
from math_utils import calculate_factorial

class TestCalculateFactorial(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)

    def test_positive_integers(self):
        self.assertEqual(calculate_factorial(2), 2)
        self.assertEqual(calculate_factorial(3), 6)
        self.assertEqual(calculate_factorial(5), 120)

    def test_negative_integers(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
        with self.assertRaises(ValueError):
            calculate_factorial(-5)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            calculate_factorial(2.5)
        with self.assertRaises(TypeError):
            calculate_factorial("5")

if __name__ == '__main__':
    unittest.main()