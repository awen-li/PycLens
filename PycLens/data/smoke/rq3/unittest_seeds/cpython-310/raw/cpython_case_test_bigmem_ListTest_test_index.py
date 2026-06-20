# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [1, 2, 3, 4, 5] * size
    size *= 5
    self.assertEqual(l.index(1), 0)
    self.assertEqual(l.index(5, size - 5), size - 1)
    self.assertEqual(l.index(5, size - 5, size), size - 1)
    self.assertRaises(ValueError, l.index, 1, size - 4, size)
    self.assertRaises(ValueError, l.index, 6)
