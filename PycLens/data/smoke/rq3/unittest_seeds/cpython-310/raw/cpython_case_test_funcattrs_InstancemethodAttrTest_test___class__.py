# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: InstancemethodAttrTest_test___class__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.fi.a.__self__.__class__, self.F)
    self.cannot_set_attr(self.fi.a, '__class__', self.F, TypeError)
