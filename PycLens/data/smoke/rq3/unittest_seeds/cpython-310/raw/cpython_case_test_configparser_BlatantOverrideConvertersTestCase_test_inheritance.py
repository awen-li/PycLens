# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BlatantOverrideConvertersTestCase_test_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class StrangeConfigParser(configparser.ConfigParser):
        gettysburg = 'a historic borough in south central Pennsylvania'

        def getboolean(self, section, option, *, raw=False, vars=None, fallback=configparser._UNSET):
            if section == option:
                return True
            return super().getboolean(section, option, raw=raw, vars=vars, fallback=fallback)

        def getlen(self, section, option, *, raw=False, vars=None, fallback=configparser._UNSET):
            return self._get_conv(section, option, len, raw=raw, vars=vars, fallback=fallback)
    cfg = StrangeConfigParser()
    cfg.read_string(self.config)
    self._test_len(cfg)
    self.assertIsNone(cfg.converters['len'])
    self.assertTrue(cfg.getboolean('one', 'one'))
    self.assertTrue(cfg.getboolean('two', 'two'))
    self.assertFalse(cfg.getboolean('one', 'two'))
    self.assertFalse(cfg.getboolean('two', 'one'))
    cfg.converters['boolean'] = cfg._convert_to_boolean
    self.assertFalse(cfg.getboolean('one', 'one'))
    self.assertFalse(cfg.getboolean('two', 'two'))
    self.assertFalse(cfg.getboolean('one', 'two'))
    self.assertFalse(cfg.getboolean('two', 'one'))
