# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_invalid_nodes_in_done

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = graphlib.TopologicalSorter()
    ts.add(1, 2, 3, 4)
    ts.add(2, 3, 4)
    ts.prepare()
    ts.get_ready()
    with self.assertRaisesRegex(ValueError, 'node 2 was not passed out'):
        ts.done(2)
    with self.assertRaisesRegex(ValueError, 'node 24 was not added using add\\(\\)'):
        ts.done(24)
