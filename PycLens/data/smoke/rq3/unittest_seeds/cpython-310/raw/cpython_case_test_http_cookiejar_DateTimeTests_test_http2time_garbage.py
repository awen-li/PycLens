# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_http2time_garbage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for test in ['', 'Garbage', 'Mandag 16. September 1996', '01-00-1980', '01-13-1980', '00-01-1980', '32-01-1980', '01-01-1980 25:00:00', '01-01-1980 00:61:00', '01-01-1980 00:00:62', '08-Oct-3697739', '08-01-3697739', '09 Feb 19942632 22:23:32 GMT', 'Wed, 09 Feb 1994834 22:23:32 GMT']:
        self.assertIsNone(http2time(test), 'http2time(%s) is not None\nhttp2time(test) %s' % (test, http2time(test)))
