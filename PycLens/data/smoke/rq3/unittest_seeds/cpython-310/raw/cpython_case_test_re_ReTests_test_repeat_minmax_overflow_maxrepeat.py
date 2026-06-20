# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_repeat_minmax_overflow_maxrepeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        from _sre import MAXREPEAT
    except ImportError:
        self.skipTest('requires _sre.MAXREPEAT constant')
    string = 'x' * 100000
    self.assertIsNone(re.match('.{%d}' % (MAXREPEAT - 1), string))
    self.assertEqual(re.match('.{,%d}' % (MAXREPEAT - 1), string).span(), (0, 100000))
    self.assertIsNone(re.match('.{%d,}?' % (MAXREPEAT - 1), string))
    self.assertRaises(OverflowError, re.compile, '.{%d}' % MAXREPEAT)
    self.assertRaises(OverflowError, re.compile, '.{,%d}' % MAXREPEAT)
    self.assertRaises(OverflowError, re.compile, '.{%d,}?' % MAXREPEAT)
