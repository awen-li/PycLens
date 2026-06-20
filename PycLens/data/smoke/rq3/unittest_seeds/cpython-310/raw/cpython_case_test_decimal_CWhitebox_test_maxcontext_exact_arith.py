# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_maxcontext_exact_arith

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    MaxContextSkip = ['logical_invert', 'next_minus', 'next_plus', 'logical_and', 'logical_or', 'logical_xor', 'next_toward', 'rotate', 'shift']
    Decimal = C.Decimal
    Context = C.Context
    localcontext = C.localcontext
    maxcontext = Context(prec=C.MAX_PREC, Emin=C.MIN_EMIN, Emax=C.MAX_EMAX)
    with localcontext(maxcontext):
        self.assertEqual(Decimal(0).exp(), 1)
        self.assertEqual(Decimal(1).ln(), 0)
        self.assertEqual(Decimal(1).log10(), 0)
        self.assertEqual(Decimal(10 ** 2).log10(), 2)
        self.assertEqual(Decimal(10 ** 223).log10(), 223)
        self.assertEqual(Decimal(10 ** 19).logb(), 19)
        self.assertEqual(Decimal(4).sqrt(), 2)
        self.assertEqual(Decimal('40E9').sqrt(), Decimal('2.0E+5'))
        self.assertEqual(divmod(Decimal(10), 3), (3, 1))
        self.assertEqual(Decimal(10) // 3, 3)
        self.assertEqual(Decimal(4) / 2, 2)
        self.assertEqual(Decimal(400) ** (-1), Decimal('0.0025'))
