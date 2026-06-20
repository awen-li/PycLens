# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = defaultdict()
    self.assertEqual(d1.default_factory, None)
    self.assertEqual(repr(d1), 'defaultdict(None, {})')
    self.assertEqual(eval(repr(d1)), d1)
    d1[11] = 41
    self.assertEqual(repr(d1), 'defaultdict(None, {11: 41})')
    d2 = defaultdict(int)
    self.assertEqual(d2.default_factory, int)
    d2[12] = 42
    self.assertEqual(repr(d2), "defaultdict(<class 'int'>, {12: 42})")

    def foo():
        return 43
    d3 = defaultdict(foo)
    self.assertTrue(d3.default_factory is foo)
    d3[13]
    self.assertEqual(repr(d3), 'defaultdict(%s, {13: 43})' % repr(foo))
