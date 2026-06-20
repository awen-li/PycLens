# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_hour

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.helper('H', 3)
    strf_output = time.strftime('%I %p', self.time_tuple)
    strp_output = _strptime._strptime_time(strf_output, '%I %p')
    self.assertTrue(strp_output[3] == self.time_tuple[3], "testing of '%%I %%p' directive failed; '%s' -> %s != %s" % (strf_output, strp_output[3], self.time_tuple[3]))
