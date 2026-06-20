# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConvertersTestCase_test_converters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cfg = self.newconfig()
    self.assertIn('boolean', cfg.converters)
    self.assertIn('list', cfg.converters)
    self.assertIsNone(cfg.converters['int'])
    self.assertIsNone(cfg.converters['float'])
    self.assertIsNone(cfg.converters['boolean'])
    self.assertIsNotNone(cfg.converters['list'])
    self.assertEqual(len(cfg.converters), 4)
    with self.assertRaises(ValueError):
        cfg.converters[''] = lambda v: v
    with self.assertRaises(ValueError):
        cfg.converters[None] = lambda v: v
    cfg.read_string('\n        [s]\n        str = string\n        int = 1\n        float = 0.5\n        list = a b c d e f g\n        bool = yes\n        ')
    s = cfg['s']
    self.assertEqual(s['str'], 'string')
    self.assertEqual(s['int'], '1')
    self.assertEqual(s['float'], '0.5')
    self.assertEqual(s['list'], 'a b c d e f g')
    self.assertEqual(s['bool'], 'yes')
    self.assertEqual(cfg.get('s', 'str'), 'string')
    self.assertEqual(cfg.get('s', 'int'), '1')
    self.assertEqual(cfg.get('s', 'float'), '0.5')
    self.assertEqual(cfg.get('s', 'list'), 'a b c d e f g')
    self.assertEqual(cfg.get('s', 'bool'), 'yes')
    self.assertEqual(cfg.get('s', 'str'), 'string')
    self.assertEqual(cfg.getint('s', 'int'), 1)
    self.assertEqual(cfg.getfloat('s', 'float'), 0.5)
    self.assertEqual(cfg.getlist('s', 'list'), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    self.assertEqual(cfg.getboolean('s', 'bool'), True)
    self.assertEqual(s.get('str'), 'string')
    self.assertEqual(s.getint('int'), 1)
    self.assertEqual(s.getfloat('float'), 0.5)
    self.assertEqual(s.getlist('list'), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    self.assertEqual(s.getboolean('bool'), True)
    with self.assertRaises(AttributeError):
        cfg.getdecimal('s', 'float')
    with self.assertRaises(AttributeError):
        s.getdecimal('float')
    import decimal
    cfg.converters['decimal'] = decimal.Decimal
    self.assertIn('decimal', cfg.converters)
    self.assertIsNotNone(cfg.converters['decimal'])
    self.assertEqual(len(cfg.converters), 5)
    dec0_5 = decimal.Decimal('0.5')
    self.assertEqual(cfg.getdecimal('s', 'float'), dec0_5)
    self.assertEqual(s.getdecimal('float'), dec0_5)
    del cfg.converters['decimal']
    self.assertNotIn('decimal', cfg.converters)
    self.assertEqual(len(cfg.converters), 4)
    with self.assertRaises(AttributeError):
        cfg.getdecimal('s', 'float')
    with self.assertRaises(AttributeError):
        s.getdecimal('float')
    with self.assertRaises(KeyError):
        del cfg.converters['decimal']
    with self.assertRaises(KeyError):
        del cfg.converters['']
    with self.assertRaises(KeyError):
        del cfg.converters[None]
