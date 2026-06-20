# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_insert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [1.0] * size
    l.insert(size - 1, 'A')
    size += 1
    self.assertEqual(len(l), size)
    self.assertEqual(l[-3:], [1.0, 'A', 1.0])
    l.insert(size + 1, 'B')
    size += 1
    self.assertEqual(len(l), size)
    self.assertEqual(l[-3:], ['A', 1.0, 'B'])
    l.insert(1, 'C')
    size += 1
    self.assertEqual(len(l), size)
    self.assertEqual(l[:3], [1.0, 'C', 1.0])
    self.assertEqual(l[size - 3:], ['A', 1.0, 'B'])
