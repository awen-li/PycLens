# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_index_and_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [None] * size
    self.assertEqual(len(l), size)
    self.assertEqual(l[-1], None)
    self.assertEqual(l[5], None)
    self.assertEqual(l[size - 1], None)
    self.assertRaises(IndexError, operator.getitem, l, size)
    self.assertEqual(l[:5], [None] * 5)
    self.assertEqual(l[-5:], [None] * 5)
    self.assertEqual(l[20:25], [None] * 5)
    self.assertEqual(l[-25:-20], [None] * 5)
    self.assertEqual(l[size - 5:], [None] * 5)
    self.assertEqual(l[size - 5:size], [None] * 5)
    self.assertEqual(l[size - 6:size - 2], [None] * 4)
    self.assertEqual(l[size:size], [])
    self.assertEqual(l[size:size + 5], [])
    l[size - 2] = 5
    self.assertEqual(len(l), size)
    self.assertEqual(l[-3:], [None, 5, None])
    self.assertEqual(l.count(5), 1)
    self.assertRaises(IndexError, operator.setitem, l, size, 6)
    self.assertEqual(len(l), size)
    l[size - 7:] = [1, 2, 3, 4, 5]
    size -= 2
    self.assertEqual(len(l), size)
    self.assertEqual(l[-7:], [None, None, 1, 2, 3, 4, 5])
    l[:7] = [1, 2, 3, 4, 5]
    size -= 2
    self.assertEqual(len(l), size)
    self.assertEqual(l[:7], [1, 2, 3, 4, 5, None, None])
    del l[size - 1]
    size -= 1
    self.assertEqual(len(l), size)
    self.assertEqual(l[-1], 4)
    del l[-2:]
    size -= 2
    self.assertEqual(len(l), size)
    self.assertEqual(l[-1], 2)
    del l[0]
    size -= 1
    self.assertEqual(len(l), size)
    self.assertEqual(l[0], 2)
    del l[:2]
    size -= 2
    self.assertEqual(len(l), size)
    self.assertEqual(l[0], 4)
