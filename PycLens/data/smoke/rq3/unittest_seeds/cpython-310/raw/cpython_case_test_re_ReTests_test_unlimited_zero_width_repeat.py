# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_unlimited_zero_width_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNone(re.match('(?:a?)*y', 'z'))
    self.assertIsNone(re.match('(?:a?)+y', 'z'))
    self.assertIsNone(re.match('(?:a?){2,}y', 'z'))
    self.assertIsNone(re.match('(?:a?)*?y', 'z'))
    self.assertIsNone(re.match('(?:a?)+?y', 'z'))
    self.assertIsNone(re.match('(?:a?){2,}?y', 'z'))
