# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: FPTest_test_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, [float('nan')])
    b = array.array(self.typecode, [float('nan')])
    self.assertIs(a != b, True)
    self.assertIs(a == b, False)
    self.assertIs(a > b, False)
    self.assertIs(a >= b, False)
    self.assertIs(a < b, False)
    self.assertIs(a <= b, False)
