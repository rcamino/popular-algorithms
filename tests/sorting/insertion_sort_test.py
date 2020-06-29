from popular_algorithms.sorting.insertion_sort import insertion_sort
from tests.sorting.sort_test import TestSort


class TestInsertionSort(TestSort):
    __test__ = True

    def _sort(self, input_list):
        return insertion_sort(input_list)
