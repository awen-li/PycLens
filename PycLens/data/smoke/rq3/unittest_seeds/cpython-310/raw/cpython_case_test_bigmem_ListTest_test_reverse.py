# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_reverse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [1, 2, 3, 4, 5] * size
    l.reverse()
    self.assertEqual(len(l), size * 5)
    self.assertEqual(l[-5:], [5, 4, 3, 2, 1])
    self.assertEqual(l[:5], [5, 4, 3, 2, 1])
