# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: _TestAsctimeYear_test_large_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.yearstr(12345), '12345')
    self.assertEqual(self.yearstr(123456789), '123456789')
