# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: _Test4dYear_test_negative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.yearstr(-1), self._format % -1)
    self.assertEqual(self.yearstr(-1234), '-1234')
    self.assertEqual(self.yearstr(-123456), '-123456')
    self.assertEqual(self.yearstr(-123456789), str(-123456789))
    self.assertEqual(self.yearstr(-1234567890), str(-1234567890))
    self.assertEqual(self.yearstr(TIME_MINYEAR), str(TIME_MINYEAR))
    self.assertRaises(OverflowError, self.yearstr, TIME_MINYEAR - 1)
    with self.assertRaises(OverflowError):
        self.yearstr(-TIME_MAXYEAR - 1)
