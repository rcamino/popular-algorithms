import unittest


class TestSort(unittest.TestCase):
    __test__ = False

    def _sort(self, input_list):
        raise NotImplementedError

    def _test_sort(self, input_list, expected_list):
        self.assertEqual(expected_list, self._sort(input_list))

    def test_bubble_sort_with_positive_numbers(self):
        self._test_sort([5, 5, 7, 8, 2, 4, 1], [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_negative_numbers_only(self):
        self._test_sort([-1, -3, -5, -7, -9, -5], [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_with_negative_and_positive_numbers(self):
        self._test_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1], [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_same_numbers(self):
        self._test_sort([1, 1, 1, 1], [1, 1, 1, 1])

    def test_bubble_sort_empty_list(self):
        self._test_sort([], [])
