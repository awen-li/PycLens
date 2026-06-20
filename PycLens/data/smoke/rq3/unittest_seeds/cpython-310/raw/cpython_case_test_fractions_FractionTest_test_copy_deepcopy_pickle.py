# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fractions.py
# case: FractionTest_test_copy_deepcopy_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = F(13, 7)
    dr = DummyFraction(13, 7)
    self.assertEqual(r, loads(dumps(r)))
    self.assertEqual(id(r), id(copy(r)))
    self.assertEqual(id(r), id(deepcopy(r)))
    self.assertNotEqual(id(dr), id(copy(dr)))
    self.assertNotEqual(id(dr), id(deepcopy(dr)))
    self.assertTypedEquals(dr, copy(dr))
    self.assertTypedEquals(dr, deepcopy(dr))
