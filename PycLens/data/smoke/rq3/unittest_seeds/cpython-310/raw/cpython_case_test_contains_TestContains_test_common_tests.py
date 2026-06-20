# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contains.py
# case: TestContains_test_common_tests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = base_set(1)
    b = myset(1)
    c = seq(1)
    self.assertIn(1, b)
    self.assertNotIn(0, b)
    self.assertIn(1, c)
    self.assertNotIn(0, c)
    self.assertRaises(TypeError, lambda : 1 in a)
    self.assertRaises(TypeError, lambda : 1 not in a)
    self.assertIn('c', 'abc')
    self.assertNotIn('d', 'abc')
    self.assertIn('', '')
    self.assertIn('', 'abc')
    self.assertRaises(TypeError, lambda : None in 'abc')
