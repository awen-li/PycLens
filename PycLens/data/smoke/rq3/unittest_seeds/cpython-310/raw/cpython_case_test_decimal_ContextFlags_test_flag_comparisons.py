# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextFlags_test_flag_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = self.decimal.Context
    Inexact = self.decimal.Inexact
    Rounded = self.decimal.Rounded
    c = Context()
    self.assertNotEqual(c.flags, c.traps)
    self.assertNotEqual(c.traps, c.flags)
    c.flags = c.traps
    self.assertEqual(c.flags, c.traps)
    self.assertEqual(c.traps, c.flags)
    c.flags[Rounded] = True
    c.traps = c.flags
    self.assertEqual(c.flags, c.traps)
    self.assertEqual(c.traps, c.flags)
    d = {}
    d.update(c.flags)
    self.assertEqual(d, c.flags)
    self.assertEqual(c.flags, d)
    d[Inexact] = True
    self.assertNotEqual(d, c.flags)
    self.assertNotEqual(c.flags, d)
    d = {Inexact: False}
    self.assertNotEqual(d, c.flags)
    self.assertNotEqual(c.flags, d)
    d = ['xyz']
    self.assertNotEqual(d, c.flags)
    self.assertNotEqual(c.flags, d)
