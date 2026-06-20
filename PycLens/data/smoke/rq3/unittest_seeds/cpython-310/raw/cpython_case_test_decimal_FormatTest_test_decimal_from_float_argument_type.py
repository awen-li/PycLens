# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: FormatTest_test_decimal_from_float_argument_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(self.decimal.Decimal):

        def __init__(self, a):
            self.a_type = type(a)
    a = A.from_float(42.5)
    self.assertEqual(self.decimal.Decimal, a.a_type)
    a = A.from_float(42)
    self.assertEqual(self.decimal.Decimal, a.a_type)
