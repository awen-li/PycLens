# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: LocaleTime_Tests_test_date_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    magic_date = (1999, 3, 17, 22, 44, 55, 2, 76, 0)
    strftime_output = time.strftime('%c', magic_date)
    self.assertEqual(time.strftime(self.LT_ins.LC_date_time, magic_date), strftime_output, 'LC_date_time incorrect')
    strftime_output = time.strftime('%x', magic_date)
    self.assertEqual(time.strftime(self.LT_ins.LC_date, magic_date), strftime_output, 'LC_date incorrect')
    strftime_output = time.strftime('%X', magic_date)
    self.assertEqual(time.strftime(self.LT_ins.LC_time, magic_date), strftime_output, 'LC_time incorrect')
    LT = _strptime.LocaleTime()
    LT.am_pm = ('', '')
    self.assertTrue(LT.LC_time, "LocaleTime's LC directives cannot handle empty strings")
