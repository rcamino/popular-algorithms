from popular_algorithms.sorting.heap_sort import heap_sort
from tests.sorting.sort_test import TestSort


class TestHeapSort(TestSort):
    __test__ = True

    def _sort(self, input_list):
        return heap_sort(input_list)
