# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_popitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('\n            [section1]\n            name1 {0[0]} value1\n            [section2]\n            name2 {0[0]} value2\n            [section3]\n            name3 {0[0]} value3\n        '.format(self.delimiters), defaults={'default': '<default>'})
    self.assertEqual(cf.popitem()[0], 'section1')
    self.assertEqual(cf.popitem()[0], 'section2')
    self.assertEqual(cf.popitem()[0], 'section3')
    with self.assertRaises(KeyError):
        cf.popitem()
