# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_sort

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [1, 2, 3, 4, 5] * size
    l.sort()
    self.assertEqual(len(l), size * 5)
    self.assertEqual(l.count(1), size)
    self.assertEqual(l[:10], [1] * 10)
    self.assertEqual(l[-10:], [5] * 10)
