import unittest
from random import randint

from accesscheck.accesscheck import AccessChecker


class TestInputArgs(unittest.TestCase):

    graph = {1: [2, 3, 5],
             2: [],
             3: [1, 4],
             4: [2, 5, 6],
             5: [4],
             6: []}

    online_status = {1: True, 4: True, 5: True, 6: True}

    def _test(self, graph, online, start, end, connected=True):
        ac = AccessChecker(graph, online)
        self.assertEqual(ac.is_connected(start, end), connected)

    def test_simple_ok(self):
        self._test({1: [2]},
                   [1, 2],
                   1, 2, True)

    def test_ok(self):
        self._test(self.graph, self.online_status, 1, 6)

    def test_empty(self):
        self._test({}, [], 1, 5, False)

    def test_offline(self):
        self._test({1: [2]}, [], 1, 2, False)

    def test_big_graph(self):
        n = 1024
        g = {i: [i+1] for i in range(n)}
        on = {i: True for i in range(n+1)}
        self._test(g, on, 0, n)

    def test_dense(self):
        n = 1024
        g = {i: [i+1] for i in range(n)}
        for i in g:
            g[i].append(randint(0, n))
        on = {i: True for i in range(n+1)}
        self._test(g, on, 0, n)

    def test_cycle(self):
        self._test({1: [2], 2: [1, 3]}, [1, 2, 3], 1, 3, True)

    def test_cycle_offline(self):
        self._test({1: [2], 2: [1, 3]}, [1, 3], 1, 3, False)


if __name__ == '__main__':
    unittest.main()
