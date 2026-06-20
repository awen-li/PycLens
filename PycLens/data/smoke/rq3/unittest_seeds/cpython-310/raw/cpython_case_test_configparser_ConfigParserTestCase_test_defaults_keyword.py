# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCase_test_defaults_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig(defaults={1: 2.4})
    self.assertEqual(cf[self.default_section]['1'], '2.4')
    self.assertAlmostEqual(cf[self.default_section].getfloat('1'), 2.4)
    cf = self.newconfig(defaults={'A': 5.2})
    self.assertEqual(cf[self.default_section]['a'], '5.2')
    self.assertAlmostEqual(cf[self.default_section].getfloat('a'), 5.2)
