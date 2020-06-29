from popular_algorithms.sorting.selection_sort import selection_sort
from tests.sorting.sort_test import TestSort


class TestSelectionSort(TestSort):
    __test__ = True

    def _sort(self, input_list):
        return selection_sort(input_list)
