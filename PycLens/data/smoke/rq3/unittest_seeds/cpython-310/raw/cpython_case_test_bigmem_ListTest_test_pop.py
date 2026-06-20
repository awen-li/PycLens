# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = ['a', 'b', 'c', 'd', 'e'] * size
    size *= 5
    self.assertEqual(len(l), size)
    item = l.pop()
    size -= 1
    self.assertEqual(len(l), size)
    self.assertEqual(item, 'e')
    self.assertEqual(l[-2:], ['c', 'd'])
    item = l.pop(0)
    size -= 1
    self.assertEqual(len(l), size)
    self.assertEqual(item, 'a')
    self.assertEqual(l[:2], ['b', 'c'])
    item = l.pop(size - 2)
    size -= 1
    self.assertEqual(len(l), size)
    self.assertEqual(item, 'c')
    self.assertEqual(l[-2:], ['b', 'd'])
