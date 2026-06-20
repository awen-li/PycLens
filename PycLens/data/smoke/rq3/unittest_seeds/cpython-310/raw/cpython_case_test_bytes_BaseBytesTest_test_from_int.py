# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_from_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(0)
    self.assertEqual(b, self.type2test())
    b = self.type2test(10)
    self.assertEqual(b, self.type2test([0] * 10))
    b = self.type2test(10000)
    self.assertEqual(b, self.type2test([0] * 10000))
