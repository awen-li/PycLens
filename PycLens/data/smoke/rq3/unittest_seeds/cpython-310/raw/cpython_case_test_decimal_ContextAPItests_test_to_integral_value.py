# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_to_integral_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.to_integral_value(Decimal(10))
    self.assertEqual(c.to_integral_value(10), d)
    self.assertRaises(TypeError, c.to_integral_value, '10')
    self.assertRaises(TypeError, c.to_integral_value, 10, 'x')
