# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_is_enabled_for

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_disable = self.logger.manager.disable
    self.logger.manager.disable = 23
    self.addCleanup(setattr, self.logger.manager, 'disable', old_disable)
    self.assertFalse(self.logger.isEnabledFor(22))
