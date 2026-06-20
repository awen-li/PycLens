# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_get_traces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracemalloc.clear_traces()
    obj_size = 12345
    (obj, obj_traceback) = allocate_bytes(obj_size)
    traces = tracemalloc._get_traces()
    trace = self.find_trace(traces, obj_traceback)
    self.assertIsInstance(trace, tuple)
    (domain, size, traceback, length) = trace
    self.assertEqual(size, obj_size)
    self.assertEqual(traceback, obj_traceback._frames)
    tracemalloc.stop()
    self.assertEqual(tracemalloc._get_traces(), [])
