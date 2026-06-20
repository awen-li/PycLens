# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_graph_with_iterables

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dependson = (2 * x + 1 for x in range(5))
    ts = graphlib.TopologicalSorter({0: dependson})
    self.assertEqual(list(ts.static_order()), [1, 3, 5, 7, 9, 0])
