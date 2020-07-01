from collections import defaultdict

from popular_algorithms.graphs.prim import minimum_spanning_tree
from tests.graphs.test_minimum_spanning_tree import TestMinimumSpanningTree


class TestPrim(TestMinimumSpanningTree):

    def _minimum_spanning_tree(self, nodes, edges):
        nodes = set()
        transition_cost = defaultdict(dict)
        for source, target, cost in edges:
            nodes.add(source)
            nodes.add(target)
            transition_cost[source][target] = cost
            transition_cost[target][source] = cost

        return minimum_spanning_tree(nodes, transition_cost)
