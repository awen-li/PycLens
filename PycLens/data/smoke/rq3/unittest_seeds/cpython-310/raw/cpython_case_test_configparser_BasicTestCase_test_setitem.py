# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('\n            [section1]\n            name1 {0[0]} value1\n            [section2]\n            name2 {0[0]} value2\n            [section3]\n            name3 {0[0]} value3\n        '.format(self.delimiters), defaults={'nameD': 'valueD'})
    self.assertEqual(set(cf['section1'].keys()), {'name1', 'named'})
    self.assertEqual(set(cf['section2'].keys()), {'name2', 'named'})
    self.assertEqual(set(cf['section3'].keys()), {'name3', 'named'})
    self.assertEqual(cf['section1']['name1'], 'value1')
    self.assertEqual(cf['section2']['name2'], 'value2')
    self.assertEqual(cf['section3']['name3'], 'value3')
    self.assertEqual(cf.sections(), ['section1', 'section2', 'section3'])
    cf['section2'] = {'name22': 'value22'}
    self.assertEqual(set(cf['section2'].keys()), {'name22', 'named'})
    self.assertEqual(cf['section2']['name22'], 'value22')
    self.assertNotIn('name2', cf['section2'])
    self.assertEqual(cf.sections(), ['section1', 'section2', 'section3'])
    cf['section3'] = {}
    self.assertEqual(set(cf['section3'].keys()), {'named'})
    self.assertNotIn('name3', cf['section3'])
    self.assertEqual(cf.sections(), ['section1', 'section2', 'section3'])
    cf[self.default_section] = cf[self.default_section]
    self.assertNotEqual(set(cf[self.default_section].keys()), set())
    cf[self.default_section] = {}
    self.assertEqual(set(cf[self.default_section].keys()), set())
    self.assertEqual(set(cf['section1'].keys()), {'name1'})
    self.assertEqual(set(cf['section2'].keys()), {'name22'})
    self.assertEqual(set(cf['section3'].keys()), set())
    self.assertEqual(cf.sections(), ['section1', 'section2', 'section3'])
    cf['section2'] = cf['section2']
    self.assertEqual(set(cf['section2'].keys()), {'name22'})
