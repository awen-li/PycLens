# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_caseinsensitive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    strf_output = time.strftime('%B', self.time_tuple)
    self.assertTrue(_strptime._strptime_time(strf_output.upper(), '%B'), 'strptime does not handle ALL-CAPS names properly')
    self.assertTrue(_strptime._strptime_time(strf_output.lower(), '%B'), 'strptime does not handle lowercase names properly')
    self.assertTrue(_strptime._strptime_time(strf_output.capitalize(), '%B'), 'strptime does not handle capword names properly')
