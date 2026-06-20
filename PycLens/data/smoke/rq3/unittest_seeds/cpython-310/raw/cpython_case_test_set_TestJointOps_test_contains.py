# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for c in self.letters:
        self.assertEqual(c in self.s, c in self.d)
    self.assertRaises(TypeError, self.s.__contains__, [[]])
    s = self.thetype([frozenset(self.letters)])
    self.assertIn(self.thetype(self.letters), s)
