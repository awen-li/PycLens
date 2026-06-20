# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_number_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    self.assertEqual(c.number_class(123), c.number_class(Decimal(123)))
    self.assertEqual(c.number_class(0), c.number_class(Decimal(0)))
    self.assertEqual(c.number_class(-45), c.number_class(Decimal(-45)))
