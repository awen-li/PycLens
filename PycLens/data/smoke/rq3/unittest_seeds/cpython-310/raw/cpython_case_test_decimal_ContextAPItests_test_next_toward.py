# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_next_toward

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.next_toward(Decimal(1), Decimal(2))
    self.assertEqual(c.next_toward(1, 2), d)
    self.assertEqual(c.next_toward(Decimal(1), 2), d)
    self.assertEqual(c.next_toward(1, Decimal(2)), d)
    self.assertRaises(TypeError, c.next_toward, '1', 2)
    self.assertRaises(TypeError, c.next_toward, 1, '2')
