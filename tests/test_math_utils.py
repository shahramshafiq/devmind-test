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
            
    def test_factorial_of_list_input(self):
        with self.assertRaises(TypeError):
            factorial([1, 2, 3])
            
    def test_factorial_of_dict_input(self):
        with self.assertRaises(TypeError):
            factorial({"a": 1, "b": 2})
            
    def test_factorial_of_set_input(self):
        with self.assertRaises(TypeError):
            factorial({1, 2, 3})
            
    def test_factorial_of_tuple_input(self):
        with self.assertRaises(TypeError):
            factorial((1, 2, 3))
            
    def test_factorial_of_large_input(self):
        with self.assertRaises(OverflowError):
            factorial(1000)
            
if __name__ == '__main__':
    unittest.main()