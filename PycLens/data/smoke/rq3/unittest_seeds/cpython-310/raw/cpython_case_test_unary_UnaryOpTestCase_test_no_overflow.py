# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unary.py
# case: UnaryOpTestCase_test_no_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nines = '9' * 32
    self.assertTrue(eval('+' + nines) == 10 ** 32 - 1)
    self.assertTrue(eval('-' + nines) == -(10 ** 32 - 1))
    self.assertTrue(eval('~' + nines) == ~(10 ** 32 - 1))
