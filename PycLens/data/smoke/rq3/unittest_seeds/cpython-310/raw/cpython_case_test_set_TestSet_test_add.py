# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.s.add('Q')
    self.assertIn('Q', self.s)
    dup = self.s.copy()
    self.s.add('Q')
    self.assertEqual(self.s, dup)
    self.assertRaises(TypeError, self.s.add, [])
