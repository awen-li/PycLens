# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CFunctionality_test_c_ieee_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    IEEEContext = C.IEEEContext
    DECIMAL32 = C.DECIMAL32
    DECIMAL64 = C.DECIMAL64
    DECIMAL128 = C.DECIMAL128

    def assert_rest(self, context):
        self.assertEqual(context.clamp, 1)
        assert_signals(self, context, 'traps', [])
        assert_signals(self, context, 'flags', [])
    c = IEEEContext(DECIMAL32)
    self.assertEqual(c.prec, 7)
    self.assertEqual(c.Emax, 96)
    self.assertEqual(c.Emin, -95)
    assert_rest(self, c)
    c = IEEEContext(DECIMAL64)
    self.assertEqual(c.prec, 16)
    self.assertEqual(c.Emax, 384)
    self.assertEqual(c.Emin, -383)
    assert_rest(self, c)
    c = IEEEContext(DECIMAL128)
    self.assertEqual(c.prec, 34)
    self.assertEqual(c.Emax, 6144)
    self.assertEqual(c.Emin, -6143)
    assert_rest(self, c)
    self.assertRaises(OverflowError, IEEEContext, 2 ** 63)
    self.assertRaises(ValueError, IEEEContext, -1)
    self.assertRaises(ValueError, IEEEContext, 1024)
