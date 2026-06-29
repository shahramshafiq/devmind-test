import unittest
from math_utils import is_prime

class TestIsPrimeFunction(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_edge_cases(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        with self.assertRaises(TypeError):
            is_prime(3.5)

if __name__ == '__main__':
    unittest.main()