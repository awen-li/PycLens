# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: FrameAttrsTest_test_f_lineno_del_segfault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (f, _, _) = self.make_frames()
    with self.assertRaises(AttributeError):
        del f.f_lineno
