# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_asctime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    time.asctime(time.gmtime(self.t))
    for bigyear in (TIME_MAXYEAR, TIME_MINYEAR):
        asc = time.asctime((bigyear, 6, 1) + (0,) * 6)
        self.assertEqual(asc[-len(str(bigyear)):], str(bigyear))
    self.assertRaises(OverflowError, time.asctime, (TIME_MAXYEAR + 1,) + (0,) * 8)
    self.assertRaises(OverflowError, time.asctime, (TIME_MINYEAR - 1,) + (0,) * 8)
    self.assertRaises(TypeError, time.asctime, 0)
    self.assertRaises(TypeError, time.asctime, ())
    self.assertRaises(TypeError, time.asctime, (0,) * 10)
