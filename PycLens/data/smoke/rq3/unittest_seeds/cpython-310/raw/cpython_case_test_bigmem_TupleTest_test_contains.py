# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: TupleTest_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = (1, 2, 3, 4, 5) * size
    self.assertEqual(len(t), size * 5)
    self.assertTrue(5 in t)
    self.assertFalse((1, 2, 3, 4, 5) in t)
    self.assertFalse(0 in t)
