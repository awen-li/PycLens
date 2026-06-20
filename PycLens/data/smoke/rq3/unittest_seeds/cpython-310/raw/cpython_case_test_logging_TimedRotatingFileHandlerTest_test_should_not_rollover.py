# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: TimedRotatingFileHandlerTest_test_should_not_rollover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fh = logging.handlers.TimedRotatingFileHandler(os.devnull, 'S', encoding='utf-8', backupCount=1)
    time.sleep(1.1)
    r = logging.makeLogRecord({'msg': 'testing - device file'})
    self.assertFalse(fh.shouldRollover(r))
    fh.close()
