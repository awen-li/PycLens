# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_sre_character_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in [0, 8, 16, 32, 64, 127, 128, 255, 256, 65535, 65536, 1114111]:
        if i < 256:
            self.assertTrue(re.match('\\%03o' % i, chr(i)))
            self.assertTrue(re.match('\\%03o0' % i, chr(i) + '0'))
            self.assertTrue(re.match('\\%03o8' % i, chr(i) + '8'))
            self.assertTrue(re.match('\\x%02x' % i, chr(i)))
            self.assertTrue(re.match('\\x%02x0' % i, chr(i) + '0'))
            self.assertTrue(re.match('\\x%02xz' % i, chr(i) + 'z'))
        if i < 65536:
            self.assertTrue(re.match('\\u%04x' % i, chr(i)))
            self.assertTrue(re.match('\\u%04x0' % i, chr(i) + '0'))
            self.assertTrue(re.match('\\u%04xz' % i, chr(i) + 'z'))
        self.assertTrue(re.match('\\U%08x' % i, chr(i)))
        self.assertTrue(re.match('\\U%08x0' % i, chr(i) + '0'))
        self.assertTrue(re.match('\\U%08xz' % i, chr(i) + 'z'))
    self.assertTrue(re.match('\\0', '\x00'))
    self.assertTrue(re.match('\\08', '\x008'))
    self.assertTrue(re.match('\\01', '\x01'))
    self.assertTrue(re.match('\\018', '\x018'))
    self.checkPatternError('\\567', 'octal escape value \\567 outside of range 0-0o377', 0)
    self.checkPatternError('\\911', 'invalid group reference 91', 1)
    self.checkPatternError('\\x1', 'incomplete escape \\x1', 0)
    self.checkPatternError('\\x1z', 'incomplete escape \\x1', 0)
    self.checkPatternError('\\u123', 'incomplete escape \\u123', 0)
    self.checkPatternError('\\u123z', 'incomplete escape \\u123', 0)
    self.checkPatternError('\\U0001234', 'incomplete escape \\U0001234', 0)
    self.checkPatternError('\\U0001234z', 'incomplete escape \\U0001234', 0)
    self.checkPatternError('\\U00110000', 'bad escape \\U00110000', 0)
