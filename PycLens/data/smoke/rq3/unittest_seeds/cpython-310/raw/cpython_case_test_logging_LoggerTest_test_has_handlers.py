# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_has_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.logger.hasHandlers())
    for handler in self.logger.handlers:
        self.logger.removeHandler(handler)
    self.assertFalse(self.logger.hasHandlers())
