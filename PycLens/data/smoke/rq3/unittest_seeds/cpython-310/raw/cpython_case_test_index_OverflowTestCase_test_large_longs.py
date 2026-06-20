# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: OverflowTestCase_test_large_longs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.pos.__index__(), self.pos)
    self.assertEqual(self.neg.__index__(), self.neg)
