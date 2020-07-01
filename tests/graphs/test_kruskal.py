from popular_algorithms.graphs.kruskal import minimum_spanning_tree
from tests.graphs.test_minimum_spanning_tree import TestMinimumSpanningTree


class TestKruskal(TestMinimumSpanningTree):

    def _minimum_spanning_tree(self, nodes, edges):
        return minimum_spanning_tree(nodes, edges)
