# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerAdapterTest_test_exception_excinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        1 / 0
    except ZeroDivisionError as e:
        exc = e
    self.adapter.exception('exc_info test', exc_info=exc)
    self.assertEqual(len(self.recording.records), 1)
    record = self.recording.records[0]
    self.assertEqual(record.exc_info, (exc.__class__, exc, exc.__traceback__))
