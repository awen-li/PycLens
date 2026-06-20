# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_http2time_redos_regression_actually_completes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    http2time('01 Jan 1970{}00:00:00 GMT!'.format(' ' * 10 ** 5))
    http2time('01 Jan 1970 00:00:00{}GMT!'.format(' ' * 10 ** 5))
