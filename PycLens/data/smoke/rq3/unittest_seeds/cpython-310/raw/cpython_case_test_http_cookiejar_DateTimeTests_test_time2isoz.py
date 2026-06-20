# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: DateTimeTests_test_time2isoz

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = 1019227000
    day = 24 * 3600
    self.assertEqual(time2isoz(base), '2002-04-19 14:36:40Z')
    self.assertEqual(time2isoz(base + day), '2002-04-20 14:36:40Z')
    self.assertEqual(time2isoz(base + 2 * day), '2002-04-21 14:36:40Z')
    self.assertEqual(time2isoz(base + 3 * day), '2002-04-22 14:36:40Z')
    az = time2isoz()
    bz = time2isoz(500000)
    for text in (az, bz):
        self.assertRegex(text, '^\\d{4}-\\d\\d-\\d\\d \\d\\d:\\d\\d:\\d\\dZ$', 'bad time2isoz format: %s %s' % (az, bz))
