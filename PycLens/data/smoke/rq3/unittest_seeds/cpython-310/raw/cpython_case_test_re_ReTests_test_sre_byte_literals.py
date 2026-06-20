# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_sre_byte_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in [0, 8, 16, 32, 64, 127, 128, 255]:
        self.assertTrue(re.match(('\\%03o' % i).encode(), bytes([i])))
        self.assertTrue(re.match(('\\%03o0' % i).encode(), bytes([i]) + b'0'))
        self.assertTrue(re.match(('\\%03o8' % i).encode(), bytes([i]) + b'8'))
        self.assertTrue(re.match(('\\x%02x' % i).encode(), bytes([i])))
        self.assertTrue(re.match(('\\x%02x0' % i).encode(), bytes([i]) + b'0'))
        self.assertTrue(re.match(('\\x%02xz' % i).encode(), bytes([i]) + b'z'))
    self.assertRaises(re.error, re.compile, b'\\u1234')
    self.assertRaises(re.error, re.compile, b'\\U00012345')
    self.assertTrue(re.match(b'\\0', b'\x00'))
    self.assertTrue(re.match(b'\\08', b'\x008'))
    self.assertTrue(re.match(b'\\01', b'\x01'))
    self.assertTrue(re.match(b'\\018', b'\x018'))
    self.checkPatternError(b'\\567', 'octal escape value \\567 outside of range 0-0o377', 0)
    self.checkPatternError(b'\\911', 'invalid group reference 91', 1)
    self.checkPatternError(b'\\x1', 'incomplete escape \\x1', 0)
    self.checkPatternError(b'\\x1z', 'incomplete escape \\x1', 0)
