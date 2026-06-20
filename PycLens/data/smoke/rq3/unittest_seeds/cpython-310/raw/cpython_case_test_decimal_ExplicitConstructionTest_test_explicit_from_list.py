# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_from_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal([0, [0], 0])
    self.assertEqual(str(d), '0')
    d = Decimal([1, [4, 3, 4, 9, 1, 3, 5, 3, 4], -25])
    self.assertEqual(str(d), '-4.34913534E-17')
    d = Decimal([1, (4, 3, 4, 9, 1, 3, 5, 3, 4), -25])
    self.assertEqual(str(d), '-4.34913534E-17')
    d = Decimal((1, [4, 3, 4, 9, 1, 3, 5, 3, 4], -25))
    self.assertEqual(str(d), '-4.34913534E-17')
