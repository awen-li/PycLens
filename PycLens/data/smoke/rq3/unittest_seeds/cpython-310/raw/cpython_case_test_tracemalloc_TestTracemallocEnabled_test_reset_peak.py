# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_reset_peak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracemalloc.clear_traces()
    large_sum = sum(list(range(100000)))
    (size1, peak1) = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()
    (size2, peak2) = tracemalloc.get_traced_memory()
    self.assertGreaterEqual(peak2, size2)
    self.assertLess(peak2, peak1)
    obj_size = 1024 * 1024
    (obj, obj_traceback) = allocate_bytes(obj_size)
    (size3, peak3) = tracemalloc.get_traced_memory()
    self.assertGreaterEqual(peak3, size3)
    self.assertGreater(peak3, peak2)
    self.assertGreaterEqual(peak3 - peak2, obj_size)
