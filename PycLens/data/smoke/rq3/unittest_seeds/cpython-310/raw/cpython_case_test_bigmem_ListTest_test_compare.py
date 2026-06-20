# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l1 = [''] * size
    l2 = [''] * size
    self.assertTrue(l1 == l2)
    del l2
    l2 = [''] * (size + 1)
    self.assertFalse(l1 == l2)
    del l2
    l2 = [2] * size
    self.assertFalse(l1 == l2)
