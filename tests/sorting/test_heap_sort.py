from popular_algorithms.sorting.heap_sort import heap_sort
from tests.sorting.test_sort import TestSort


class TestHeapSort(TestSort):
    __test__ = True

    def _sort(self, input_list):
        return heap_sort(input_list)
