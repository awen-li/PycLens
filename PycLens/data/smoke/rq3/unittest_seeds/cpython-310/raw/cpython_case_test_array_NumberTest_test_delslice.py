# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: NumberTest_test_delslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, range(5))
    del a[::2]
    self.assertEqual(a, array.array(self.typecode, [1, 3]))
    a = array.array(self.typecode, range(5))
    del a[1::2]
    self.assertEqual(a, array.array(self.typecode, [0, 2, 4]))
    a = array.array(self.typecode, range(5))
    del a[1::-2]
    self.assertEqual(a, array.array(self.typecode, [0, 2, 3, 4]))
    a = array.array(self.typecode, range(10))
    del a[::1000]
    self.assertEqual(a, array.array(self.typecode, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    a = array.array(self.typecode, range(10))
    del a[9::1 << 333]
