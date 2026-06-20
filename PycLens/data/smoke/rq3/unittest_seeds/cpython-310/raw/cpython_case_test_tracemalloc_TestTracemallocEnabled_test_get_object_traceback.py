# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_get_object_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracemalloc.clear_traces()
    obj_size = 12345
    (obj, obj_traceback) = allocate_bytes(obj_size)
    traceback = tracemalloc.get_object_traceback(obj)
    self.assertEqual(traceback, obj_traceback)
