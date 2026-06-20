# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: TimeRETests_test_compile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    found = self.time_re.compile('%A').match(self.locale_time.f_weekday[6])
    self.assertTrue(found and found.group('A') == self.locale_time.f_weekday[6], "re object for '%A' failed")
    compiled = self.time_re.compile('%a %b')
    found = compiled.match('%s %s' % (self.locale_time.a_weekday[4], self.locale_time.a_month[4]))
    self.assertTrue(found, "Match failed with '%s' regex and '%s' string" % (compiled.pattern, '%s %s' % (self.locale_time.a_weekday[4], self.locale_time.a_month[4])))
    self.assertTrue(found.group('a') == self.locale_time.a_weekday[4] and found.group('b') == self.locale_time.a_month[4], "re object couldn't find the abbreviated weekday month in '%s' using '%s'; group 'a' = '%s', group 'b' = %s'" % (found.string, found.re.pattern, found.group('a'), found.group('b')))
    for directive in ('a', 'A', 'b', 'B', 'c', 'd', 'G', 'H', 'I', 'j', 'm', 'M', 'p', 'S', 'u', 'U', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'Z', '%'):
        compiled = self.time_re.compile('%' + directive)
        found = compiled.match(time.strftime('%' + directive))
        self.assertTrue(found, "Matching failed on '%s' using '%s' regex" % (time.strftime('%' + directive), compiled.pattern))
