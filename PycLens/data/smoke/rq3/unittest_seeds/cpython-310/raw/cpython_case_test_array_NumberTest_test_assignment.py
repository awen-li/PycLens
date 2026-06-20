# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: NumberTest_test_assignment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, range(10))
    a[::2] = array.array(self.typecode, [42] * 5)
    self.assertEqual(a, array.array(self.typecode, [42, 1, 42, 3, 42, 5, 42, 7, 42, 9]))
    a = array.array(self.typecode, range(10))
    a[::-4] = array.array(self.typecode, [10] * 3)
    self.assertEqual(a, array.array(self.typecode, [0, 10, 2, 3, 4, 10, 6, 7, 8, 10]))
    a = array.array(self.typecode, range(4))
    a[::-1] = a
    self.assertEqual(a, array.array(self.typecode, [3, 2, 1, 0]))
    a = array.array(self.typecode, range(10))
    b = a[:]
    c = a[:]
    ins = array.array(self.typecode, range(2))
    a[2:3] = ins
    b[slice(2, 3)] = ins
    c[2:3] = ins
