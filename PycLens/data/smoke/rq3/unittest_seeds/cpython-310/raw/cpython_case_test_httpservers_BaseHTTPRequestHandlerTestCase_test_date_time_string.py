# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_date_time_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    now = time.time()
    (year, month, day, hh, mm, ss, wd, y, z) = time.gmtime(now)
    expected = '%s, %02d %3s %4d %02d:%02d:%02d GMT' % (self.handler.weekdayname[wd], day, self.handler.monthname[month], year, hh, mm, ss)
    self.assertEqual(self.handler.date_time_string(timestamp=now), expected)
