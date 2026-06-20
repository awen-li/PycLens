# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: NumberTest_test_extslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, range(5))
    self.assertEqual(a[:], a)
    self.assertEqual(a[::2], array.array(self.typecode, [0, 2, 4]))
    self.assertEqual(a[1::2], array.array(self.typecode, [1, 3]))
    self.assertEqual(a[::-1], array.array(self.typecode, [4, 3, 2, 1, 0]))
    self.assertEqual(a[::-2], array.array(self.typecode, [4, 2, 0]))
    self.assertEqual(a[3::-2], array.array(self.typecode, [3, 1]))
    self.assertEqual(a[-100:100], a)
    self.assertEqual(a[100:-100:-1], a[::-1])
    self.assertEqual(a[-100:100:2], array.array(self.typecode, [0, 2, 4]))
    self.assertEqual(a[1000:2000:2], array.array(self.typecode, []))
    self.assertEqual(a[-1000:-2000:-2], array.array(self.typecode, []))
