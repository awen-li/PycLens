# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_mar1_comes_after_feb29_even_when_omitting_the_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertLess(time.strptime('Feb 29', '%b %d'), time.strptime('Mar 1', '%b %d'))
