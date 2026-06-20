# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestOnlySetsInBinaryOps_test_eq_ne

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.other == self.set, False)
    self.assertEqual(self.set == self.other, False)
    self.assertEqual(self.other != self.set, True)
    self.assertEqual(self.set != self.other, True)
