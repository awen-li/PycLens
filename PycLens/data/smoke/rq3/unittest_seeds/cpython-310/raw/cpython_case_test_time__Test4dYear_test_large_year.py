# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: _Test4dYear_test_large_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.yearstr(12345).lstrip('+'), '12345')
    self.assertEqual(self.yearstr(123456789).lstrip('+'), '123456789')
    self.assertEqual(self.yearstr(TIME_MAXYEAR).lstrip('+'), str(TIME_MAXYEAR))
    self.assertRaises(OverflowError, self.yearstr, TIME_MAXYEAR + 1)
