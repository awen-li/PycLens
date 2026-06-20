# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    self.assertNotIn('a', d)
    self.assertFalse('a' in d)
    self.assertTrue('a' not in d)
    d = {'a': 1, 'b': 2}
    self.assertIn('a', d)
    self.assertIn('b', d)
    self.assertNotIn('c', d)
    self.assertRaises(TypeError, d.__contains__)
