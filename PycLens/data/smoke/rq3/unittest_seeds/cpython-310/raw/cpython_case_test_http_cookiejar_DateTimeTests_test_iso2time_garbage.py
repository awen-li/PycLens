# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_iso2time_garbage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for test in ['', 'Garbage', 'Thursday, 03-Feb-94 00:00:00 GMT', '1980-00-01', '1980-13-01', '1980-01-00', '1980-01-32', '1980-01-01 25:00:00', '1980-01-01 00:61:00', '01-01-1980 00:00:62', '01-01-1980T00:00:62', '19800101T250000Z']:
        self.assertIsNone(iso2time(test), 'iso2time(%r)' % test)
