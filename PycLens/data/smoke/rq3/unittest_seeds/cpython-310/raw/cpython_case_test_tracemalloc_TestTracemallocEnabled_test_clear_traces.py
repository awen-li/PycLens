# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_clear_traces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (obj, obj_traceback) = allocate_bytes(123)
    traceback = tracemalloc.get_object_traceback(obj)
    self.assertIsNotNone(traceback)
    tracemalloc.clear_traces()
    traceback2 = tracemalloc.get_object_traceback(obj)
    self.assertIsNone(traceback2)
