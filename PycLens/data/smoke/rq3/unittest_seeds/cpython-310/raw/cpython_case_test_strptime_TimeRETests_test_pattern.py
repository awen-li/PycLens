# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: TimeRETests_test_pattern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern_string = self.time_re.pattern('%a %A %d')
    self.assertTrue(pattern_string.find(self.locale_time.a_weekday[2]) != -1, "did not find abbreviated weekday in pattern string '%s'" % pattern_string)
    self.assertTrue(pattern_string.find(self.locale_time.f_weekday[4]) != -1, "did not find full weekday in pattern string '%s'" % pattern_string)
    self.assertTrue(pattern_string.find(self.time_re['d']) != -1, "did not find 'd' directive pattern string '%s'" % pattern_string)
