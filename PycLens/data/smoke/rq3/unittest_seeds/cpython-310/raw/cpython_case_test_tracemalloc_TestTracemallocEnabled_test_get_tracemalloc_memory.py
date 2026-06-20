# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_get_tracemalloc_memory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [allocate_bytes(123) for count in range(1000)]
    size = tracemalloc.get_tracemalloc_memory()
    self.assertGreaterEqual(size, 0)
    tracemalloc.clear_traces()
    size2 = tracemalloc.get_tracemalloc_memory()
    self.assertGreaterEqual(size2, 0)
    self.assertLessEqual(size2, size)
