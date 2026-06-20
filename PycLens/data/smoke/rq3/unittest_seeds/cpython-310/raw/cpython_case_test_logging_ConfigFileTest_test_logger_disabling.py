# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigFileTest_test_logger_disabling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.apply_config(self.disable_test)
    logger = logging.getLogger('some_pristine_logger')
    self.assertFalse(logger.disabled)
    self.apply_config(self.disable_test)
    self.assertTrue(logger.disabled)
    self.apply_config(self.disable_test, disable_existing_loggers=False)
    self.assertFalse(logger.disabled)
