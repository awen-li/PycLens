# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_make_record_with_extra_overwrite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'my record'
    level = 13
    fn = lno = msg = args = exc_info = func = sinfo = None
    rv = logging._logRecordFactory(name, level, fn, lno, msg, args, exc_info, func, sinfo)
    for key in ('message', 'asctime') + tuple(rv.__dict__.keys()):
        extra = {key: 'some value'}
        self.assertRaises(KeyError, self.logger.makeRecord, name, level, fn, lno, msg, args, exc_info, extra=extra, sinfo=sinfo)
