# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_other_escapes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkPatternError('\\', 'bad escape (end of pattern)', 0)
    self.assertEqual(re.match('\\(', '(').group(), '(')
    self.assertIsNone(re.match('\\(', ')'))
    self.assertEqual(re.match('\\\\', '\\').group(), '\\')
    self.assertEqual(re.match('[\\]]', ']').group(), ']')
    self.assertIsNone(re.match('[\\]]', '['))
    self.assertEqual(re.match('[a\\-c]', '-').group(), '-')
    self.assertIsNone(re.match('[a\\-c]', 'b'))
    self.assertEqual(re.match('[\\^a]+', 'a^').group(), 'a^')
    self.assertIsNone(re.match('[\\^a]+', 'b'))
    re.purge()
    for c in 'ceghijklmopqyzCEFGHIJKLMNOPQRTVXY':
        with self.subTest(c):
            self.assertRaises(re.error, re.compile, '\\%c' % c)
    for c in 'ceghijklmopqyzABCEFGHIJKLMNOPQRTVXYZ':
        with self.subTest(c):
            self.assertRaises(re.error, re.compile, '[\\%c]' % c)
