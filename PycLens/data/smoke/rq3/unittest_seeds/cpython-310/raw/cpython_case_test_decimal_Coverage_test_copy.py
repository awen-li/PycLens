# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = self.decimal.Context
    c = Context()
    c.prec = 10000
    x = -1172 ** 1712
    y = c.copy_abs(x)
    self.assertEqual(y, -x)
    y = c.copy_negate(x)
    self.assertEqual(y, -x)
    y = c.copy_sign(x, 1)
    self.assertEqual(y, -x)
