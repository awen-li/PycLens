# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: EnumerateTestCase_test_basicfunction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(type(self.enum(self.seq)), self.enum)
    e = self.enum(self.seq)
    self.assertEqual(iter(e), e)
    self.assertEqual(list(self.enum(self.seq)), self.res)
    self.enum.__doc__
