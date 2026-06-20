import unittest
from math_utils import factorial

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)
        
    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)
        
    def test_factorial_of_positive_numbers(self):
        self.assertEqual(factorial(5), 120)
        
    def test_factorial_of_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial(-5)
            
    def test_factorial_of_non_integer_input(self):
        with self.assertRaises(TypeError):
            factorial(3.5)
            
if __name__ == '__main__':
    unittest.main()