# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ExceptionTest_test_formatting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.root_logger
    h = RecordingHandler()
    r.addHandler(h)
    try:
        raise RuntimeError('deliberate mistake')
    except:
        logging.exception('failed', stack_info=True)
    r.removeHandler(h)
    h.close()
    r = h.records[0]
    self.assertTrue(r.exc_text.startswith('Traceback (most recent call last):\n'))
    self.assertTrue(r.exc_text.endswith('\nRuntimeError: deliberate mistake'))
    self.assertTrue(r.stack_info.startswith('Stack (most recent call last):\n'))
    self.assertTrue(r.stack_info.endswith("logging.exception('failed', stack_info=True)"))
