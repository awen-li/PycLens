# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: LocaleTime_Tests_test_month

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.compare_against_time(self.LT_ins.f_month, '%B', 1, 'Testing against full month name failed')
    self.compare_against_time(self.LT_ins.a_month, '%b', 1, 'Testing against abbreviated month name failed')
