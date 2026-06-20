# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_exp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.exp(Decimal(10))
    self.assertEqual(c.exp(10), d)
    self.assertRaises(TypeError, c.exp, '10')
