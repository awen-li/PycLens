# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: Strptime12AMPMTests_test_twelve_noon_midnight

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(time.strptime('12 PM', '%I %p')[3], 12)
    eq(time.strptime('12 AM', '%I %p')[3], 0)
    eq(_strptime._strptime_time('12 PM', '%I %p')[3], 12)
    eq(_strptime._strptime_time('12 AM', '%I %p')[3], 0)
