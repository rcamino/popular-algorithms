import unittest

from collections import defaultdict

from popular_algorithms.graphs.dfs import dfs
from popular_algorithms.graphs.kruskal import minimum_spanning_tree


class TestKruskal(unittest.TestCase):

    def _test(self, nodes, edges, expected_tree_cost):
        tree_edges = minimum_spanning_tree(nodes, edges)

        # collect the tree nodes
        tree_nodes = self._nodes_from_edges(tree_edges)

        # check that the amount of nodes in the input match
        self.assertEqual(len(nodes), len(tree_nodes))

        # check that the amount of edges is correct for a tree: |E| = |V| - 1
        self.assertEqual(len(tree_edges), len(tree_nodes) - 1)

        # check if the tree is connected
        self._graph_is_connected(tree_nodes, tree_edges)

        # check if the costs match
        self.assertEqual(expected_tree_cost, self._graph_cost(tree_edges))

    @staticmethod
    def _nodes_from_edges(edges):
        nodes = set()
        for source, target, _ in edges:
            nodes.add(source)
            nodes.add(target)
        return nodes

    @staticmethod
    def _graph_cost(edges):
        graph_cost = 0
        for _, _, cost in edges:
            graph_cost += cost
        return graph_cost

    def _graph_is_connected(self, nodes, edges):
        # transform tree edge list into an adjacency list
        adjacency_list = defaultdict(list)
        root = None
        for source, target, _ in edges:
            # need to pick any node as the root
            if root is None:
                root = source

            # add the edge in both directions
            adjacency_list[source].append(target)
            adjacency_list[target].append(source)

        # run a dfs and collect all traversed tree nodes
        visited_nodes = set()

        def dfs_callback(node, parent_by_node):
            visited_nodes.add(node)

        dfs(root, adjacency_list, dfs_callback)

        self.assertEqual(len(nodes), len(visited_nodes))

    def test_small(self):
        self._test(
            # nodes
            {"S", "A", "B", "C", "D", "T"},
            # edges
            {
                ("S", "A", 7),
                ("S", "C", 8),
                ("A", "B", 6),
                ("A", "B", 9),
                ("A", "C", 3),
                ("B", "C", 4),
                ("B", "D", 2),
                ("B", "T", 5),
                ("C", "C", 1),
                ("C", "D", 3),
                ("D", "T", 2),
            },
            # expected tree cost
            17
        )

    def test_big(self):
        self._test(
            # nodes
            {0, 1, 2, 3, 4, 5, 6, 7, 8},
            # edges
            {
                (0, 1, 4),
                (0, 7, 8),
                (1, 2, 8),
                (1, 7, 11),
                (2, 3, 7),
                (2, 5, 4),
                (2, 8, 2),
                (3, 4, 9),
                (3, 5, 14),
                (4, 5, 10),
                (5, 6, 2),
                (6, 7, 1),
                (6, 8, 6),
                (7, 8, 7),
            },
            # expected tree cost
            37
        )
