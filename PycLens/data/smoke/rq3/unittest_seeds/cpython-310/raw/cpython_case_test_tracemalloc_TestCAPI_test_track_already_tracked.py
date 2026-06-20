# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestCAPI_test_track_already_tracked

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nframe = 5
    tracemalloc.start(nframe)
    self.track()
    frames = self.track(nframe=nframe)
    self.assertEqual(self.get_traceback(), tracemalloc.Traceback(frames))
