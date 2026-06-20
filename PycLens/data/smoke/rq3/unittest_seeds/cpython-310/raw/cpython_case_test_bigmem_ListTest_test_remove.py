# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: ListTest_test_remove

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = [10] * size
    self.assertEqual(len(l), size)
    l.remove(10)
    size -= 1
    self.assertEqual(len(l), size)
    l.append(5)
    size += 1
    self.assertEqual(len(l), size)
    self.assertEqual(l[-2:], [10, 5])
    l.remove(5)
    size -= 1
    self.assertEqual(len(l), size)
    self.assertEqual(l[-2:], [10, 10])
