# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_tofrombytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, 2 * self.example)
    b = array.array(self.typecode)
    self.assertRaises(TypeError, a.tobytes, 42)
    self.assertRaises(TypeError, b.frombytes)
    self.assertRaises(TypeError, b.frombytes, 42)
    b.frombytes(a.tobytes())
    c = array.array(self.typecode, bytearray(a.tobytes()))
    self.assertEqual(a, b)
    self.assertEqual(a, c)
    if a.itemsize > 1:
        self.assertRaises(ValueError, b.frombytes, b'x')
