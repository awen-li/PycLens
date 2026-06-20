# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: ListTestCase_test_setdelitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = -2
    self.n.ind = 2
    lst = list('ab!cdefghi!j')
    del lst[self.o]
    del lst[self.n]
    lst[self.o] = 'X'
    lst[self.n] = 'Y'
    self.assertEqual(lst, list('abYdefghXj'))
    lst = [5, 6, 7, 8, 9, 10, 11]
    lst.__setitem__(self.n, 'here')
    self.assertEqual(lst, [5, 6, 'here', 8, 9, 10, 11])
    lst.__delitem__(self.n)
    self.assertEqual(lst, [5, 6, 8, 9, 10, 11])
