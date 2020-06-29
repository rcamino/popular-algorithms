from popular_algorithms.sorting.quick_sort import quick_sort
from tests.sorting.sort_test import TestSort


class TestQuickSort(TestSort):
    __test__ = True

    def _sort(self, input_list):
        return quick_sort(input_list)
