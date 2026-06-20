# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_float_containment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    floats = (INF, -INF, 0.0, 1.0, NAN)
    for f in floats:
        self.assertIn(f, [f])
        self.assertIn(f, (f,))
        self.assertIn(f, {f})
        self.assertIn(f, {f: None})
        self.assertEqual([f].count(f), 1, "[].count('%r') != 1" % f)
        self.assertIn(f, floats)
    for f in floats:
        self.assertTrue([f] == [f], '[%r] != [%r]' % (f, f))
        self.assertTrue((f,) == (f,), '(%r,) != (%r,)' % (f, f))
        self.assertTrue({f} == {f}, '{%r} != {%r}' % (f, f))
        self.assertTrue({f: None} == {f: None}, '{%r : None} != {%r : None}' % (f, f))
        (l, t, s, d) = ([f], (f,), {f}, {f: None})
        self.assertTrue(l == l, '[%r] not equal to itself' % f)
        self.assertTrue(t == t, '(%r,) not equal to itself' % f)
        self.assertTrue(s == s, '{%r} not equal to itself' % f)
        self.assertTrue(d == d, '{%r : None} not equal to itself' % f)
