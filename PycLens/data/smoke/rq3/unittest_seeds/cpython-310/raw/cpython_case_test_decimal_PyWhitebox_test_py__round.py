# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PyWhitebox_test_py__round

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = P.Decimal
    self.assertRaises(ValueError, Decimal('3.1234')._round, 0, ROUND_UP)
