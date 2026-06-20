import unittest
from pagination import paginate

class TestPagination(unittest.TestCase):
    def test_paginate_exact_divisible(self):
        data = [1, 2, 3, 4, 5, 6]
        page_size = 2
        expected_result = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(paginate(data, page_size), expected_result)

    def test_paginate_not_exact_divisible(self):
        data = [1, 2, 3, 4, 5]
        page_size = 2
        expected_result = [[1, 2], [3, 4], [5]]
        self.assertEqual(paginate(data, page_size), expected_result)

    def test_paginate_empty_list(self):
        data = []
        page_size = 2
        expected_result = []
        self.assertEqual(paginate(data, page_size), expected_result)

    def test_paginate_single_element_list(self):
        data = [1]
        page_size = 2
        expected_result = [[1]]
        self.assertEqual(paginate(data, page_size), expected_result)