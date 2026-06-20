# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: JulianTests_test_all_julian_days

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    for i in range(1, 367):
        eq(_strptime._strptime_time('%d 2004' % i, '%j %Y')[7], i)
