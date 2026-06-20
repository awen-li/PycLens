# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_ctime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.mktime((1973, 9, 16, 1, 3, 52, 0, 0, -1))
    self.assertEqual(time.ctime(t), 'Sun Sep 16 01:03:52 1973')
    t = time.mktime((2000, 1, 1, 0, 0, 0, 0, 0, -1))
    self.assertEqual(time.ctime(t), 'Sat Jan  1 00:00:00 2000')
    for year in [-100, 100, 1000, 2000, 2050, 10000]:
        try:
            testval = time.mktime((year, 1, 10) + (0,) * 6)
        except (ValueError, OverflowError):
            pass
        else:
            self.assertEqual(time.ctime(testval)[20:], str(year))
