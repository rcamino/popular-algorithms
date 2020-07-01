import unittest

from popular_algorithms.graphs.edmonds_karp import maximum_flow


class TestEdmondsKarp(unittest.TestCase):

    def _test(self, source, target, capacities, expected_flow):
        self.assertEqual(expected_flow, maximum_flow(source, target, capacities))

    def test_small(self):
        self._test(
            "A",
            "D",
            {
                "A": {"B": 1000, "C": 1000},
                "B": {"C": 1, "D": 1000},
                "C": {"D": 1000},
            },
            1000
        )

    def test_big(self):
        self._test(
            "A",
            "G",
            {
                "A": {"B": 3, "D": 3},
                "B": {"C": 4},
                "C": {"A": 3, "D": 1, "E": 2},
                "D": {"E": 2, "F": 6},
                "E": {"G": 1},
                "F": {"G": 9},
            },
            5
        )
