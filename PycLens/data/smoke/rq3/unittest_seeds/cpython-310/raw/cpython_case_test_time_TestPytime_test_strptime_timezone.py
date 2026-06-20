# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestPytime_test_strptime_timezone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = time.strptime('UTC', '%Z')
    self.assertEqual(t.tm_zone, 'UTC')
    t = time.strptime('+0500', '%z')
    self.assertEqual(t.tm_gmtoff, 5 * 3600)
