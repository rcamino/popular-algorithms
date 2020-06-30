import unittest


class TestTraversal(unittest.TestCase):

    def _traversal(self, tree, callback):
        raise NotImplementedError

    def _expected_small_traversal(self):
        raise NotImplementedError

    def _expected_big_traversal(self):
        raise NotImplementedError

    def _test_traversal(self, tree, expected_traversal):
        traversal = []

        def callback(value):
            traversal.append(value)

        self._traversal(tree, callback)

        self.assertEqual(expected_traversal, traversal)

    def test_small(self):
        tree = {
            "value": 1,
            "left": {
                "value": 2,
                "left": {"value": 4},
                "right": {"value": 5}
            },
            "right": {"value": 3}
        }

        self._test_traversal(tree, self._expected_small_traversal())

    def test_big(self):
        tree = {
            "value": 25,
            "left": {
                "value": 15,
                "left": {
                    "value": 10,
                    "left": {"value": 4},
                    "right": {"value": 12}
                },
                "right": {
                    "value": 22,
                    "left": {"value": 18},
                    "right": {"value": 24}
                }
            },
            "right": {
                "value": 50,
                "left": {
                    "value": 35,
                    "left": {"value": 31},
                    "right": {"value": 44}
                },
                "right": {
                    "value": 70,
                    "left": {"value": 66},
                    "right": {"value": 90}
                }
            }
        }

        self._test_traversal(tree, self._expected_big_traversal())
