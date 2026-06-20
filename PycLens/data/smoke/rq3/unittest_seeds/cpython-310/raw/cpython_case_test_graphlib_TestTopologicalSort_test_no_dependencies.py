# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_no_dependencies

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_graph({1: {2}, 3: {4}, 5: {6}}, [(2, 4, 6), (1, 3, 5)])
    self._test_graph({1: set(), 3: set(), 5: set()}, [(1, 3, 5)])
