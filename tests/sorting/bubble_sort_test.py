from popular_algorithms.sorting.bubble_sort import bubble_sort
from tests.sorting.sort_test import TestSort


class TestBubbleSort(TestSort):
    __test__ = True

    def _sort(self, input_list):
        return bubble_sort(input_list)
