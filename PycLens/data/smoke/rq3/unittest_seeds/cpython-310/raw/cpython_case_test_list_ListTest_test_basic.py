# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list([]), [])
    l0_3 = [0, 1, 2, 3]
    l0_3_bis = list(l0_3)
    self.assertEqual(l0_3, l0_3_bis)
    self.assertTrue(l0_3 is not l0_3_bis)
    self.assertEqual(list(()), [])
    self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])
    self.assertEqual(list(''), [])
    self.assertEqual(list('spam'), ['s', 'p', 'a', 'm'])
    self.assertEqual(list((x for x in range(10) if x % 2)), [1, 3, 5, 7, 9])
    if sys.maxsize == 2147483647:
        self.assertRaises(MemoryError, list, range(sys.maxsize // 2))
    x = []
    x.extend((-y for y in x))
    self.assertEqual(x, [])
