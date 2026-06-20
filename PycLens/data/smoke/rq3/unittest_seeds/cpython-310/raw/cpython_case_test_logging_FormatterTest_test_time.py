# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: FormatterTest_test_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.get_record()
    dt = datetime.datetime(1993, 4, 21, 8, 3, 0, 0, utc)
    r.created = time.mktime(dt.astimezone(None).timetuple())
    r.msecs = 123
    f = logging.Formatter('%(asctime)s %(message)s')
    f.converter = time.gmtime
    self.assertEqual(f.formatTime(r), '1993-04-21 08:03:00,123')
    self.assertEqual(f.formatTime(r, '%Y:%d'), '1993:21')
    f.format(r)
    self.assertEqual(r.asctime, '1993-04-21 08:03:00,123')
