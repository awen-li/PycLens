# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_is_enabled_for_disabled_logger

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_disabled = self.logger.disabled
    old_disable = self.logger.manager.disable
    self.logger.disabled = True
    self.logger.manager.disable = 21
    self.addCleanup(setattr, self.logger, 'disabled', old_disabled)
    self.addCleanup(setattr, self.logger.manager, 'disable', old_disable)
    self.assertFalse(self.logger.isEnabledFor(22))
