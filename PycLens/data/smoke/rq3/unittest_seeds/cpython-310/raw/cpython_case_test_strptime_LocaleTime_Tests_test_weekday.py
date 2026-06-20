# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: LocaleTime_Tests_test_weekday

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.compare_against_time(self.LT_ins.f_weekday, '%A', 6, 'Testing of full weekday name failed')
    self.compare_against_time(self.LT_ins.a_weekday, '%a', 6, 'Testing of abbreviated weekday name failed')
