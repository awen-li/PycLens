# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_not_hashable_nodes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = graphlib.TopologicalSorter()
    self.assertRaises(TypeError, ts.add, dict(), 1)
    self.assertRaises(TypeError, ts.add, 1, dict())
    self.assertRaises(TypeError, ts.add, dict(), dict())
