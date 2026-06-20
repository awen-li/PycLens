# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: LocaleTime_Tests_test_am_pm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    strftime_output = time.strftime('%p', self.time_tuple).lower()
    self.assertIn(strftime_output, self.LT_ins.am_pm, 'AM/PM representation not in tuple')
    if self.time_tuple[3] < 12:
        position = 0
    else:
        position = 1
    self.assertEqual(self.LT_ins.am_pm[position], strftime_output, 'AM/PM representation in the wrong position within the tuple')
