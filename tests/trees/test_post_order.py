from popular_algorithms.trees.post_order import post_order
from tests.trees.test_traversal import TraversalTest


class PostOrderTest(TraversalTest):

    def _traversal(self, tree, callback):
        return post_order(tree, callback)

    def _expected_small_traversal(self):
        return [4, 5, 2, 3, 1]

    def _expected_big_traversal(self):
        return [4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25]
