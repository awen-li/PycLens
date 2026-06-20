# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: CoverageOneHundredTestCase_test_inconsistent_converters_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = configparser.ConfigParser()
    import decimal
    parser.converters['decimal'] = decimal.Decimal
    parser.read_string('\n            [s1]\n            one = 1\n            [s2]\n            two = 2\n        ')
    self.assertIn('decimal', parser.converters)
    self.assertEqual(parser.getdecimal('s1', 'one'), 1)
    self.assertEqual(parser.getdecimal('s2', 'two'), 2)
    self.assertEqual(parser['s1'].getdecimal('one'), 1)
    self.assertEqual(parser['s2'].getdecimal('two'), 2)
    del parser.getdecimal
    with self.assertRaises(AttributeError):
        parser.getdecimal('s1', 'one')
    self.assertIn('decimal', parser.converters)
    del parser.converters['decimal']
    self.assertNotIn('decimal', parser.converters)
    with self.assertRaises(AttributeError):
        parser.getdecimal('s1', 'one')
    with self.assertRaises(AttributeError):
        parser['s1'].getdecimal('one')
    with self.assertRaises(AttributeError):
        parser['s2'].getdecimal('two')
