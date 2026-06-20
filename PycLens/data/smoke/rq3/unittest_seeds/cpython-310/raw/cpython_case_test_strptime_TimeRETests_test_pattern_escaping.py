# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: TimeRETests_test_pattern_escaping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern_string = self.time_re.pattern('\\d+')
    self.assertIn('\\\\d\\+', pattern_string, '%s does not have re characters escaped properly' % pattern_string)
