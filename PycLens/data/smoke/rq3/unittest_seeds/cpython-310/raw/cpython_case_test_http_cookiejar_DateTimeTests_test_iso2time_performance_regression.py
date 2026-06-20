# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_iso2time_performance_regression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iso2time('1994-02-03{}14:15:29 -0100!'.format(' ' * 10 ** 6))
    iso2time('1994-02-03 14:15:29{}-0100!'.format(' ' * 10 ** 6))
