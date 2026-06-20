# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_http2time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def parse_date(text):
        return time.gmtime(http2time(text))[:6]
    self.assertEqual(parse_date('01 Jan 2001'), (2001, 1, 1, 0, 0, 0.0))
    self.assertEqual(parse_date('03-Feb-20'), (2020, 2, 3, 0, 0, 0.0))
    self.assertEqual(parse_date('03-Feb-98'), (1998, 2, 3, 0, 0, 0.0))
