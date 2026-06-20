# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_bug_27936

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [1234, 1234.56, decimal.Decimal('1234.56'), fractions.Fraction(123456, 100)]:
        self.assertEqual(round(x, None), round(x))
        self.assertEqual(type(round(x, None)), type(round(x)))
