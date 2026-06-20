# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_percent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    strf_output = time.strftime('%m %% %Y', self.time_tuple)
    strp_output = _strptime._strptime_time(strf_output, '%m %% %Y')
    self.assertTrue(strp_output[0] == self.time_tuple[0] and strp_output[1] == self.time_tuple[1], 'handling of percent sign failed')
