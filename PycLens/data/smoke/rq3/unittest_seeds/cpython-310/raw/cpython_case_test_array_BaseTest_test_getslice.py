# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_getslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    self.assertEqual(a[:], a)
    self.assertEqual(a[1:], array.array(self.typecode, self.example[1:]))
    self.assertEqual(a[:1], array.array(self.typecode, self.example[:1]))
    self.assertEqual(a[:-1], array.array(self.typecode, self.example[:-1]))
    self.assertEqual(a[-1:], array.array(self.typecode, self.example[-1:]))
    self.assertEqual(a[-1:-1], array.array(self.typecode))
    self.assertEqual(a[2:1], array.array(self.typecode))
    self.assertEqual(a[1000:], array.array(self.typecode))
    self.assertEqual(a[-1000:], a)
    self.assertEqual(a[:1000], a)
    self.assertEqual(a[:-1000], array.array(self.typecode))
    self.assertEqual(a[-1000:1000], a)
    self.assertEqual(a[2000:1000], array.array(self.typecode))
