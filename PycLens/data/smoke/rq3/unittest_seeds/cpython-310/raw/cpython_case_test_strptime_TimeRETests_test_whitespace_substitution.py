# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: TimeRETests_test_whitespace_substitution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern = self.time_re.pattern('%j %H')
    self.assertFalse(re.match(pattern, '180'))
    self.assertTrue(re.match(pattern, '18 0'))
