# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: StreamHandlerTest_test_error_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = TestStreamHandler(BadStream())
    r = logging.makeLogRecord({})
    old_raise = logging.raiseExceptions
    try:
        h.handle(r)
        self.assertIs(h.error_record, r)
        h = logging.StreamHandler(BadStream())
        with support.captured_stderr() as stderr:
            h.handle(r)
            msg = '\nRuntimeError: deliberate mistake\n'
            self.assertIn(msg, stderr.getvalue())
        logging.raiseExceptions = False
        with support.captured_stderr() as stderr:
            h.handle(r)
            self.assertEqual('', stderr.getvalue())
    finally:
        logging.raiseExceptions = old_raise
