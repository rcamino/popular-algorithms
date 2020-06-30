from popular_algorithms.trees.in_order import in_order
from tests.trees.test_traversal import TestTraversal


class TestInOrder(TestTraversal):

    def _traversal(self, tree, callback):
        return in_order(tree, callback)

    def _expected_small_traversal(self):
        return [4, 2, 5, 1, 3]

    def _expected_big_traversal(self):
        return [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]
