import unittest
from pagination import paginate

class TestPaginateFunction(unittest.TestCase):
    def test_list_length_exactly_divisible_by_page_size(self):
        list_to_paginate = [1, 2, 3, 4, 5, 6]
        page_size = 3
        pages = paginate(list_to_paginate, page_size)
        self.assertEqual(pages, [[1, 2, 3], [4, 5, 6]])

    def test_list_length_not_exactly_divisible_by_page_size(self):
        list_to_paginate = [1, 2, 3, 4, 5, 6, 7]
        page_size = 3
        pages = paginate(list_to_paginate, page_size)
        self.assertEqual(pages, [[1, 2, 3], [4, 5, 6], [7]])

    def test_empty_list(self):
        list_to_paginate = []
        page_size = 3
        pages = paginate(list_to_paginate, page_size)
        self.assertEqual(pages, [])

    def test_page_size_larger_than_list_length(self):
        list_to_paginate = [1, 2, 3]
        page_size = 5
        pages = paginate(list_to_paginate, page_size)
        self.assertEqual(pages, [[1, 2, 3]])

if __name__ == '__main__':
    unittest.main()