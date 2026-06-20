# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'testing exception: %r'
    exc = None
    try:
        1 / 0
    except ZeroDivisionError as e:
        exc = e
        self.logger.exception(msg, self.recording)
    self.assertEqual(len(self.recording.records), 1)
    record = self.recording.records[0]
    self.assertEqual(record.levelno, logging.ERROR)
    self.assertEqual(record.msg, msg)
    self.assertEqual(record.args, (self.recording,))
    self.assertEqual(record.exc_info, (exc.__class__, exc, exc.__traceback__))
