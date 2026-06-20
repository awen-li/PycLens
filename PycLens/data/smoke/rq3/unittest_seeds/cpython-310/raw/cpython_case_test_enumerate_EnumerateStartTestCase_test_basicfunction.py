# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: EnumerateStartTestCase_test_basicfunction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self.enum(self.seq)
    self.assertEqual(iter(e), e)
    self.assertEqual(list(self.enum(self.seq)), self.res)
