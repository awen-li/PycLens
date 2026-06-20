# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_iso2time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def parse_date(text):
        return time.gmtime(iso2time(text))[:6]
    self.assertEqual(parse_date('19940203T141529Z'), (1994, 2, 3, 14, 15, 29))
    self.assertEqual(parse_date('1994-02-03 07:15:29 -0700'), (1994, 2, 3, 14, 15, 29))
    self.assertEqual(parse_date('1994-02-03 19:45:29 +0530'), (1994, 2, 3, 14, 15, 29))
