# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: FailNegTest_test_pass_through

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = [1, 2.0, Fraction(3), Decimal(4)]
    new = list(statistics._fail_neg(values))
    self.assertEqual(values, new)
