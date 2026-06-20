# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_is_tracing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracemalloc.stop()
    self.assertFalse(tracemalloc.is_tracing())
    tracemalloc.start()
    self.assertTrue(tracemalloc.is_tracing())
