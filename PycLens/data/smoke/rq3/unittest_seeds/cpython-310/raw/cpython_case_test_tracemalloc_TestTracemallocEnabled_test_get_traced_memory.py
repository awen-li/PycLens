# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_get_traced_memory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    max_error = 2048
    obj_size = 1024 * 1024
    tracemalloc.clear_traces()
    (obj, obj_traceback) = allocate_bytes(obj_size)
    (size, peak_size) = tracemalloc.get_traced_memory()
    self.assertGreaterEqual(size, obj_size)
    self.assertGreaterEqual(peak_size, size)
    self.assertLessEqual(size - obj_size, max_error)
    self.assertLessEqual(peak_size - size, max_error)
    obj = None
    (size2, peak_size2) = tracemalloc.get_traced_memory()
    self.assertLess(size2, size)
    self.assertGreaterEqual(size - size2, obj_size - max_error)
    self.assertGreaterEqual(peak_size2, peak_size)
    tracemalloc.clear_traces()
    self.assertEqual(tracemalloc.get_traced_memory(), (0, 0))
    (obj, obj_traceback) = allocate_bytes(obj_size)
    (size, peak_size) = tracemalloc.get_traced_memory()
    self.assertGreaterEqual(size, obj_size)
    tracemalloc.stop()
    self.assertEqual(tracemalloc.get_traced_memory(), (0, 0))
