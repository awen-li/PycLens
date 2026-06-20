# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_set_invalid_level

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assert_error_message(TypeError, 'Level not an integer or a valid string: None', self.logger.setLevel, None)
    self.assert_error_message(TypeError, 'Level not an integer or a valid string: (0, 0)', self.logger.setLevel, (0, 0))
