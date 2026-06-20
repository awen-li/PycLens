# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_prepare_multiple_times

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = graphlib.TopologicalSorter()
    ts.prepare()
    with self.assertRaisesRegex(ValueError, 'cannot prepare\\(\\) more than once'):
        ts.prepare()
