# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestCAPI_test_stop_untrack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracemalloc.start()
    self.track()
    tracemalloc.stop()
    with self.assertRaises(RuntimeError):
        self.untrack()
