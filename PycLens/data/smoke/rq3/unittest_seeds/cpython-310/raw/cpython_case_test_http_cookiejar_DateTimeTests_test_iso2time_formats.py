# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_iso2time_formats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = ['1994-02-03 00:00:00 -0000', '1994-02-03 00:00:00 +0000', '1994-02-03 00:00:00', '1994-02-03', '1994-02-03T00:00:00', '19940203', '1994-02-02 24:00:00', '19940203T000000Z', '  1994-02-03 ', '  1994-02-03T00:00:00  ']
    test_t = 760233600
    for s in tests:
        self.assertEqual(iso2time(s), test_t, s)
        self.assertEqual(iso2time(s.lower()), test_t, s.lower())
        self.assertEqual(iso2time(s.upper()), test_t, s.upper())
