# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCase_test_set_nonstring_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('[sect]\noption1{eq}foo\n'.format(eq=self.delimiters[0]))
    self.assertRaises(TypeError, cf.set, 'sect', 'option1', 1)
    self.assertRaises(TypeError, cf.set, 'sect', 'option1', 1.0)
    self.assertRaises(TypeError, cf.set, 'sect', 'option1', object())
    self.assertRaises(TypeError, cf.set, 'sect', 'option2', 1)
    self.assertRaises(TypeError, cf.set, 'sect', 'option2', 1.0)
    self.assertRaises(TypeError, cf.set, 'sect', 'option2', object())
    self.assertRaises(TypeError, cf.set, 'sect', 123, 'invalid opt name!')
    self.assertRaises(TypeError, cf.add_section, 123)
