# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCase_test_set_malformatted_interpolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('[sect]\noption1{eq}foo\n'.format(eq=self.delimiters[0]))
    self.assertEqual(cf.get('sect', 'option1'), 'foo')
    self.assertRaises(ValueError, cf.set, 'sect', 'option1', '%foo')
    self.assertRaises(ValueError, cf.set, 'sect', 'option1', 'foo%')
    self.assertRaises(ValueError, cf.set, 'sect', 'option1', 'f%oo')
    self.assertEqual(cf.get('sect', 'option1'), 'foo')
    cf.set('sect', 'option2', 'foo%%bar')
    self.assertEqual(cf.get('sect', 'option2'), 'foo%bar')
