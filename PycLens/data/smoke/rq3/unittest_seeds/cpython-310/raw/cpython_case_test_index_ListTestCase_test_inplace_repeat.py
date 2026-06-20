# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: ListTestCase_test_inplace_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = 2
    self.n.ind = 3
    lst = [6, 4]
    lst *= self.o
    self.assertEqual(lst, [6, 4, 6, 4])
    lst *= self.n
    self.assertEqual(lst, [6, 4, 6, 4] * 3)
    lst = [5, 6, 7, 8, 9, 11]
    l2 = lst.__imul__(self.n)
    self.assertIs(l2, lst)
    self.assertEqual(lst, [5, 6, 7, 8, 9, 11] * 3)
