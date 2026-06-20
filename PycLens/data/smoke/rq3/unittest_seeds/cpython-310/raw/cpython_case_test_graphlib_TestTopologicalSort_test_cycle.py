# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._assert_cycle({1: {1}}, [1, 1])
    self._assert_cycle({1: {2}, 2: {1}}, [1, 2, 1])
    self._assert_cycle({1: {2}, 2: {3}, 3: {1}}, [1, 3, 2, 1])
    self._assert_cycle({1: {2}, 2: {3}, 3: {1}, 5: {4}, 4: {6}}, [1, 3, 2, 1])
    self._assert_cycle({1: {2}, 2: {1}, 3: {4}, 4: {5}, 6: {7}, 7: {6}}, [1, 2, 1])
    self._assert_cycle({1: {2}, 2: {3}, 3: {2, 4}, 4: {5}}, [3, 2])
