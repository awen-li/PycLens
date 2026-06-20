# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_set_traceback_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj_size = 10
    tracemalloc.stop()
    self.assertRaises(ValueError, tracemalloc.start, -1)
    tracemalloc.stop()
    tracemalloc.start(10)
    (obj2, obj2_traceback) = allocate_bytes(obj_size)
    traceback = tracemalloc.get_object_traceback(obj2)
    self.assertEqual(len(traceback), 10)
    self.assertEqual(traceback, obj2_traceback)
    tracemalloc.stop()
    tracemalloc.start(1)
    (obj, obj_traceback) = allocate_bytes(obj_size)
    traceback = tracemalloc.get_object_traceback(obj)
    self.assertEqual(len(traceback), 1)
    self.assertEqual(traceback, obj_traceback)
