# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_90195

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = {'version': 1, 'disable_existing_loggers': False, 'handlers': {'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler'}}, 'loggers': {'a': {'level': 'DEBUG', 'handlers': ['console']}}}
    logger = logging.getLogger('a')
    self.assertFalse(logger.disabled)
    self.apply_config(config)
    self.assertFalse(logger.disabled)
    self.apply_config({'version': 1})
    self.assertTrue(logger.disabled)
    del config['disable_existing_loggers']
    self.apply_config(config)
    self.assertFalse(logger.disabled)
