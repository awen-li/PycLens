# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_compare_signal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.compare_signal(Decimal(1), Decimal(1))
    self.assertEqual(c.compare_signal(1, 1), d)
    self.assertEqual(c.compare_signal(Decimal(1), 1), d)
    self.assertEqual(c.compare_signal(1, Decimal(1)), d)
    self.assertRaises(TypeError, c.compare_signal, '1', 1)
    self.assertRaises(TypeError, c.compare_signal, 1, '1')
