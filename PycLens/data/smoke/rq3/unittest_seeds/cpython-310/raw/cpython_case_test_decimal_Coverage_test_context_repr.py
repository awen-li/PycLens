# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_context_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = self.decimal.DefaultContext.copy()
    c.prec = 425000000
    c.Emax = 425000000
    c.Emin = -425000000
    c.rounding = ROUND_HALF_DOWN
    c.capitals = 0
    c.clamp = 1
    for sig in OrderedSignals[self.decimal]:
        c.flags[sig] = False
        c.traps[sig] = False
    s = c.__repr__()
    t = 'Context(prec=425000000, rounding=ROUND_HALF_DOWN, Emin=-425000000, Emax=425000000, capitals=0, clamp=1, flags=[], traps=[])'
    self.assertEqual(s, t)
