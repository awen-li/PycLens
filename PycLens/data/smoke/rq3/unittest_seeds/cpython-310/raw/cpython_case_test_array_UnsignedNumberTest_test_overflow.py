# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: UnsignedNumberTest_test_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode)
    lower = 0
    upper = int(pow(2, a.itemsize * 8)) - 1
    self.check_overflow(lower, upper)
    self.check_overflow(Intable(lower), Intable(upper))
