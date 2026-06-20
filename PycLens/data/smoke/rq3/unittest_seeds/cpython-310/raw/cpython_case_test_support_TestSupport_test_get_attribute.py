# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_get_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(support.get_attribute(self, 'test_get_attribute'), self.test_get_attribute)
    self.assertRaises(unittest.SkipTest, support.get_attribute, self, 'foo')
