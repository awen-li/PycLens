# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: FormatterTest_test_default_msec_format_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NoMsecFormatter(logging.Formatter):
        default_msec_format = None
        default_time_format = '%d/%m/%Y %H:%M:%S'
    r = self.get_record()
    dt = datetime.datetime(1993, 4, 21, 8, 3, 0, 123, utc)
    r.created = time.mktime(dt.astimezone(None).timetuple())
    f = NoMsecFormatter()
    f.converter = time.gmtime
    self.assertEqual(f.formatTime(r), '21/04/1993 08:03:00')
