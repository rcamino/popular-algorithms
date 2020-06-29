from popular_algorithms.sorting.merge_sort import merge_sort
from tests.sorting.sort_test import TestSort


class TestMergeSort(TestSort):
    __test__ = True

    def _sort(self, input_list):
        return merge_sort(input_list)
