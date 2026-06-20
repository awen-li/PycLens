# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test()
    self.assertEqual(type(b), self.type2test)
    self.assertEqual(b.__class__, self.type2test)
