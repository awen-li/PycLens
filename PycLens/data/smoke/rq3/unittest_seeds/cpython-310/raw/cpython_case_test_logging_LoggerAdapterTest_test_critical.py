# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerAdapterTest_test_critical

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'critical test! %r'
    self.adapter.critical(msg, self.recording)
    self.assertEqual(len(self.recording.records), 1)
    record = self.recording.records[0]
    self.assertEqual(record.levelno, logging.CRITICAL)
    self.assertEqual(record.msg, msg)
    self.assertEqual(record.args, (self.recording,))
