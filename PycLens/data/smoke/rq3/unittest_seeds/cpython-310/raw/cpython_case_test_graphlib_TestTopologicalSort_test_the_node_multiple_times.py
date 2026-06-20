# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_the_node_multiple_times

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_graph({1: {2}, 3: {4}, 0: [2, 4, 4, 4, 4, 4]}, [(2, 4), (0, 1, 3)])
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2)
    ts.add(1, 2)
    ts.add(1, 2)
    self.assertEqual([*ts.static_order()], [2, 1])
