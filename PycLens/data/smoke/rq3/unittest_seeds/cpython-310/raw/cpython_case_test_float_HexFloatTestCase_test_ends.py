# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: HexFloatTestCase_test_ends

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.identical(self.MIN, ldexp(1.0, -1022))
    self.identical(self.TINY, ldexp(1.0, -1074))
    self.identical(self.EPS, ldexp(1.0, -52))
    self.identical(self.MAX, 2.0 * (ldexp(1.0, 1023) - ldexp(1.0, 970)))
