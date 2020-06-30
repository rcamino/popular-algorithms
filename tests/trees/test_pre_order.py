from popular_algorithms.trees.pre_order import pre_order
from tests.trees.test_traversal import TraversalTest


class PreOrderTest(TraversalTest):

    def _traversal(self, tree, callback):
        return pre_order(tree, callback)

    def _expected_small_traversal(self):
        return [1, 2, 4, 5, 3]

    def _expected_big_traversal(self):
        return [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]
