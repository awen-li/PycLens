# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.s, set(self.word))
    self.assertEqual(self.s, frozenset(self.word))
    self.assertEqual(self.s == self.word, False)
    self.assertNotEqual(self.s, set(self.otherword))
    self.assertNotEqual(self.s, frozenset(self.otherword))
    self.assertEqual(self.s != self.word, True)
