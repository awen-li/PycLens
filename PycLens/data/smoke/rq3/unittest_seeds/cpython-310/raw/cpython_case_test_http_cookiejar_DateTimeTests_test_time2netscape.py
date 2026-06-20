# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_time2netscape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = 1019227000
    day = 24 * 3600
    self.assertEqual(time2netscape(base), 'Fri, 19-Apr-2002 14:36:40 GMT')
    self.assertEqual(time2netscape(base + day), 'Sat, 20-Apr-2002 14:36:40 GMT')
    self.assertEqual(time2netscape(base + 2 * day), 'Sun, 21-Apr-2002 14:36:40 GMT')
    self.assertEqual(time2netscape(base + 3 * day), 'Mon, 22-Apr-2002 14:36:40 GMT')
    az = time2netscape()
    bz = time2netscape(500000)
    for text in (az, bz):
        self.assertRegex(text, '[a-zA-Z]{3}, \\d{2}-[a-zA-Z]{3}-\\d{4} \\d{2}:\\d{2}:\\d{2} GMT$', 'bad time2netscape format: %s %s' % (az, bz))
