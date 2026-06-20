# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextFlags_test_float_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    FloatOperation = self.decimal.FloatOperation
    localcontext = self.decimal.localcontext

    def assert_attr(a, b, attr, context, signal=None):
        context.clear_flags()
        f = getattr(a, attr)
        if signal == FloatOperation:
            self.assertRaises(signal, f, b)
        else:
            self.assertIs(f(b), True)
        self.assertTrue(context.flags[FloatOperation])
    small_d = Decimal('0.25')
    big_d = Decimal('3.0')
    small_f = 0.25
    big_f = 3.0
    zero_d = Decimal('0.0')
    neg_zero_d = Decimal('-0.0')
    zero_f = 0.0
    neg_zero_f = -0.0
    inf_d = Decimal('Infinity')
    neg_inf_d = Decimal('-Infinity')
    inf_f = float('inf')
    neg_inf_f = float('-inf')

    def doit(c, signal=None):
        for attr in ('__lt__', '__le__'):
            assert_attr(small_d, big_f, attr, c, signal)
        for attr in ('__gt__', '__ge__'):
            assert_attr(big_d, small_f, attr, c, signal)
        assert_attr(small_d, small_f, '__eq__', c, None)
        assert_attr(neg_zero_d, neg_zero_f, '__eq__', c, None)
        assert_attr(neg_zero_d, zero_f, '__eq__', c, None)
        assert_attr(zero_d, neg_zero_f, '__eq__', c, None)
        assert_attr(zero_d, zero_f, '__eq__', c, None)
        assert_attr(neg_inf_d, neg_inf_f, '__eq__', c, None)
        assert_attr(inf_d, inf_f, '__eq__', c, None)
        assert_attr(small_d, big_f, '__ne__', c, None)
        assert_attr(Decimal('0.1'), 0.1, '__ne__', c, None)
        assert_attr(neg_inf_d, inf_f, '__ne__', c, None)
        assert_attr(inf_d, neg_inf_f, '__ne__', c, None)
        assert_attr(Decimal('NaN'), float('nan'), '__ne__', c, None)

    def test_containers(c, signal=None):
        c.clear_flags()
        s = set([100.0, Decimal('100.0')])
        self.assertEqual(len(s), 1)
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        if signal:
            self.assertRaises(signal, sorted, [1.0, Decimal('10.0')])
        else:
            s = sorted([10.0, Decimal('10.0')])
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        b = 10.0 in [Decimal('10.0'), 1.0]
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        b = 10.0 in {Decimal('10.0'): 'a', 1.0: 'b'}
        self.assertTrue(c.flags[FloatOperation])
    nc = Context()
    with localcontext(nc) as c:
        self.assertFalse(c.traps[FloatOperation])
        doit(c, signal=None)
        test_containers(c, signal=None)
        c.traps[FloatOperation] = True
        doit(c, signal=FloatOperation)
        test_containers(c, signal=FloatOperation)
