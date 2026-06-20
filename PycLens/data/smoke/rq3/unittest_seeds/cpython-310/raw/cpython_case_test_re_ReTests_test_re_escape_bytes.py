# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_escape_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = bytes(range(256))
    for i in p:
        b = bytes([i])
        self.assertMatch(re.escape(b), b)
        self.assertMatch(b'[' + re.escape(b) + b']', b)
        self.assertMatch(b'(?x)' + re.escape(b), b)
    self.assertMatch(re.escape(p), p)
    for i in b'-.]{}':
        b = bytes([i])
        self.assertEqual(re.escape(b)[:1], b'\\')
    literal_chars = self.LITERAL_CHARS.encode('ascii')
    self.assertEqual(re.escape(literal_chars), literal_chars)
