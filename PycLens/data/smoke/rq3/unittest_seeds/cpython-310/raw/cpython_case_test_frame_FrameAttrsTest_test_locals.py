# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: FrameAttrsTest_test_locals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (f, outer, inner) = self.make_frames()
    outer_locals = outer.f_locals
    self.assertIsInstance(outer_locals.pop('inner'), types.FunctionType)
    self.assertEqual(outer_locals, {'x': 5, 'y': 6})
    inner_locals = inner.f_locals
    self.assertEqual(inner_locals, {'x': 5, 'z': 7})
