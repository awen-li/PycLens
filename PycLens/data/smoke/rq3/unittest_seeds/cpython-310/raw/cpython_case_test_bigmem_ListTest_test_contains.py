# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [1, 2, 3, 4, 5] * size
    self.assertEqual(len(l), size * 5)
    self.assertTrue(5 in l)
    self.assertFalse([1, 2, 3, 4, 5] in l)
    self.assertFalse(0 in l)
