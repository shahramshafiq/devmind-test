import unittest
from pagination import paginate

class TestPaginateFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(paginate([], 10), [])

    def test_list_length_divisible_by_page_size(self):
        self.assertEqual(paginate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

    def test_list_length_not_divisible_by_page_size(self):
        self.assertEqual(paginate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 10), [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11]])

    def test_page_size_greater_than_list_length(self):
        self.assertEqual(paginate([1, 2, 3], 10), [[1, 2, 3]])

    def test_page_size_of_1(self):
        self.assertEqual(paginate([1, 2, 3], 1), [[1], [2], [3]])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            paginate("not a list", 10)
        with self.assertRaises(ValueError):
            paginate([1, 2, 3], "not an integer")
        with self.assertRaises(ValueError):
            paginate([1, 2, 3], -10)

if __name__ == "__main__":
    unittest.main()