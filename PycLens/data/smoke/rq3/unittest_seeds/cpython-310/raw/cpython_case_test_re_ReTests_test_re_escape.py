# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = ''.join((chr(i) for i in range(256)))
    for c in p:
        self.assertMatch(re.escape(c), c)
        self.assertMatch('[' + re.escape(c) + ']', c)
        self.assertMatch('(?x)' + re.escape(c), c)
    self.assertMatch(re.escape(p), p)
    for c in '-.]{}':
        self.assertEqual(re.escape(c)[:1], '\\')
    literal_chars = self.LITERAL_CHARS
    self.assertEqual(re.escape(literal_chars), literal_chars)
