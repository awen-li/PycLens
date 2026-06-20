# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: TimedRotatingFileHandlerTest_test_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assertRaises = self.assertRaises
    assertRaises(ValueError, logging.handlers.TimedRotatingFileHandler, self.fn, 'X', encoding='utf-8', delay=True)
    assertRaises(ValueError, logging.handlers.TimedRotatingFileHandler, self.fn, 'W', encoding='utf-8', delay=True)
    assertRaises(ValueError, logging.handlers.TimedRotatingFileHandler, self.fn, 'W7', encoding='utf-8', delay=True)
