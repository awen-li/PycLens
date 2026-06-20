# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_repeat_minmax_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string = 'x' * 100000
    self.assertEqual(re.match('.{65535}', string).span(), (0, 65535))
    self.assertEqual(re.match('.{,65535}', string).span(), (0, 65535))
    self.assertEqual(re.match('.{65535,}?', string).span(), (0, 65535))
    self.assertEqual(re.match('.{65536}', string).span(), (0, 65536))
    self.assertEqual(re.match('.{,65536}', string).span(), (0, 65536))
    self.assertEqual(re.match('.{65536,}?', string).span(), (0, 65536))
    self.assertRaises(OverflowError, re.compile, '.{%d}' % 2 ** 128)
    self.assertRaises(OverflowError, re.compile, '.{,%d}' % 2 ** 128)
    self.assertRaises(OverflowError, re.compile, '.{%d,}?' % 2 ** 128)
    self.assertRaises(OverflowError, re.compile, '.{%d,%d}' % (2 ** 129, 2 ** 128))
