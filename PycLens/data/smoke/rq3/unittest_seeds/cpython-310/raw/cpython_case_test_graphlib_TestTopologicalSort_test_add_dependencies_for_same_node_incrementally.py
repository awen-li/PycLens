# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_add_dependencies_for_same_node_incrementally

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2)
    ts.add(1, 3)
    ts.add(1, 4)
    ts.add(1, 5)
    ts2 = graphlib.TopologicalSorter({1: {2, 3, 4, 5}})
    self.assertEqual([*ts.static_order()], [*ts2.static_order()])
