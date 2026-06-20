# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: FrameAttrsTest_test_locals_clear_locals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (f, outer, inner) = self.make_frames()
    outer.f_locals
    inner.f_locals
    outer.clear()
    inner.clear()
    self.assertEqual(outer.f_locals, {})
    self.assertEqual(inner.f_locals, {})
