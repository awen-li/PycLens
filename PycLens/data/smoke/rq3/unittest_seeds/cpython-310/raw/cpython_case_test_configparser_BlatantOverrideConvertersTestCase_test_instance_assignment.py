# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BlatantOverrideConvertersTestCase_test_instance_assignment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cfg = configparser.ConfigParser()
    cfg.getboolean = lambda section, option: True
    cfg.getlen = lambda section, option: len(cfg[section][option])
    cfg.read_string(self.config)
    self.assertEqual(len(cfg.converters), 3)
    self.assertIn('boolean', cfg.converters)
    self.assertNotIn('len', cfg.converters)
    self.assertIsNone(cfg.converters['int'])
    self.assertIsNone(cfg.converters['float'])
    self.assertIsNone(cfg.converters['boolean'])
    self.assertTrue(cfg.getboolean('one', 'one'))
    self.assertTrue(cfg.getboolean('two', 'two'))
    self.assertTrue(cfg.getboolean('one', 'two'))
    self.assertTrue(cfg.getboolean('two', 'one'))
    cfg.converters['boolean'] = cfg._convert_to_boolean
    self.assertFalse(cfg.getboolean('one', 'one'))
    self.assertFalse(cfg.getboolean('two', 'two'))
    self.assertFalse(cfg.getboolean('one', 'two'))
    self.assertFalse(cfg.getboolean('two', 'one'))
    self.assertEqual(cfg.getlen('one', 'one'), 5)
    self.assertEqual(cfg.getlen('one', 'two'), 5)
    self.assertEqual(cfg.getlen('one', 'three'), 16)
    self.assertEqual(cfg.getlen('two', 'one'), 5)
    self.assertEqual(cfg.getlen('two', 'two'), 5)
    self.assertEqual(cfg.getlen('two', 'three'), 4)
    with self.assertRaises(AttributeError):
        self.assertEqual(cfg['one'].getlen('one'), 5)
    with self.assertRaises(AttributeError):
        self.assertEqual(cfg['two'].getlen('one'), 5)
