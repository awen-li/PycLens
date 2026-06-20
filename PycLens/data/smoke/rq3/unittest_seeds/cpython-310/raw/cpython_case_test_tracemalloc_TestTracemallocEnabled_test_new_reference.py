# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_new_reference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracemalloc.clear_traces()
    support.gc_collect()
    obj = []
    obj = None
    obj = []
    nframe = tracemalloc.get_traceback_limit()
    frames = get_frames(nframe, -3)
    obj_traceback = tracemalloc.Traceback(frames, min(len(frames), nframe))
    traceback = tracemalloc.get_object_traceback(obj)
    self.assertIsNotNone(traceback)
    self.assertEqual(traceback, obj_traceback)
