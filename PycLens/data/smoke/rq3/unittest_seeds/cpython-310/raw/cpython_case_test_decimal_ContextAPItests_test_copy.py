# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.copy()
    self.assertNotEqual(id(c), id(d))
    self.assertNotEqual(id(c.flags), id(d.flags))
    self.assertNotEqual(id(c.traps), id(d.traps))
    k1 = set(c.flags.keys())
    k2 = set(d.flags.keys())
    self.assertEqual(k1, k2)
    self.assertEqual(c.flags, d.flags)
