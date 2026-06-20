# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_valid_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DefaultContext = C.DefaultContext
    Clamped = C.Clamped
    Underflow = C.Underflow
    Inexact = C.Inexact
    Rounded = C.Rounded
    Subnormal = C.Subnormal
    c = DefaultContext.copy()
    c.prec = 34
    c.rounding = ROUND_HALF_UP
    c.Emax = 3000
    c.Emin = -3000
    c.capitals = 1
    c.clamp = 0
    self.assertEqual(c.prec, 34)
    self.assertEqual(c.rounding, ROUND_HALF_UP)
    self.assertEqual(c.Emin, -3000)
    self.assertEqual(c.Emax, 3000)
    self.assertEqual(c.capitals, 1)
    self.assertEqual(c.clamp, 0)
    self.assertEqual(c.Etiny(), -3033)
    self.assertEqual(c.Etop(), 2967)
    if C.MAX_PREC == 425000000:
        c._unsafe_setprec(999999999)
        c._unsafe_setemax(999999999)
        c._unsafe_setemin(-999999999)
        self.assertEqual(c.prec, 999999999)
        self.assertEqual(c.Emax, 999999999)
        self.assertEqual(c.Emin, -999999999)
