# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_simple_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_graph({2: {11}, 9: {11, 8}, 10: {11, 3}, 11: {7, 5}, 8: {7, 3}}, [(3, 5, 7), (8, 11), (2, 9, 10)])
    self._test_graph({1: {}}, [(1,)])
    self._test_graph({x: {x + 1} for x in range(10)}, [(x,) for x in range(10, -1, -1)])
    self._test_graph({2: {3}, 3: {4}, 4: {5}, 5: {1}, 11: {12}, 12: {13}, 13: {14}, 14: {15}}, [(1, 15), (5, 14), (4, 13), (3, 12), (2, 11)])
    self._test_graph({0: [1, 2], 1: [3], 2: [5, 6], 3: [4], 4: [9], 5: [3], 6: [7], 7: [8], 8: [4], 9: []}, [(9,), (4,), (3, 8), (1, 5, 7), (6,), (2,), (0,)])
    self._test_graph({0: [1, 2], 1: [], 2: [3], 3: []}, [(1, 3), (2,), (0,)])
    self._test_graph({0: [1, 2], 1: [], 2: [3], 3: [], 4: [5], 5: [6], 6: []}, [(1, 3, 6), (2, 5), (0, 4)])
