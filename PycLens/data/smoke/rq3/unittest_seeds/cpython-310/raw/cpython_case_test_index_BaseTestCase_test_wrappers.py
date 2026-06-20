# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: BaseTestCase_test_wrappers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = 4
    self.n.ind = 5
    self.assertEqual(6 .__index__(), 6)
    self.assertEqual(-7 .__index__(), -7)
    self.assertEqual(self.o.__index__(), 4)
    self.assertEqual(self.n.__index__(), 5)
    self.assertEqual(True .__index__(), 1)
    self.assertEqual(False .__index__(), 0)
