# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig({'foo': 'Bar'})
    self.assertEqual(cf.get(self.default_section, 'Foo'), 'Bar', 'could not locate option, expecting case-insensitive option names')
    cf['zing'] = {'option1': 'value1', 'option2': 'value2'}
    self.assertEqual(cf.sections(), ['zing'])
    self.assertEqual(set(cf['zing'].keys()), {'option1', 'option2', 'foo'})
    cf.clear()
    self.assertEqual(set(cf.sections()), set())
    self.assertEqual(set(cf[self.default_section].keys()), {'foo'})
