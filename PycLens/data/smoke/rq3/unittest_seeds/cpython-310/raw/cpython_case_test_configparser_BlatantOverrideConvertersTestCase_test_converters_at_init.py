# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BlatantOverrideConvertersTestCase_test_converters_at_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cfg = configparser.ConfigParser(converters={'len': len})
    cfg.read_string(self.config)
    self._test_len(cfg)
    self.assertIsNotNone(cfg.converters['len'])
