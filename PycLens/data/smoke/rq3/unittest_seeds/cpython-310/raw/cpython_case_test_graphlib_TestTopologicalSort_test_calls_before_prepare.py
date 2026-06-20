# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_calls_before_prepare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ts = graphlib.TopologicalSorter()
    with self.assertRaisesRegex(ValueError, 'prepare\\(\\) must be called first'):
        ts.get_ready()
    with self.assertRaisesRegex(ValueError, 'prepare\\(\\) must be called first'):
        ts.done(3)
    with self.assertRaisesRegex(ValueError, 'prepare\\(\\) must be called first'):
        ts.is_active()
