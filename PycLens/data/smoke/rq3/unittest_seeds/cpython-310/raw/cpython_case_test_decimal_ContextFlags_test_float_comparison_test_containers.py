# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextFlags_test_float_comparison_test_containers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
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
