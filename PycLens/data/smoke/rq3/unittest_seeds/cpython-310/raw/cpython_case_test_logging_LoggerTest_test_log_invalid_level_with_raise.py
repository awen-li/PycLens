# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_log_invalid_level_with_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.swap_attr(logging, 'raiseExceptions', True):
        self.assertRaises(TypeError, self.logger.log, '10', 'test message')
