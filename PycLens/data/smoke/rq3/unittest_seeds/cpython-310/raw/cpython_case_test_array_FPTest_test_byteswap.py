# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: FPTest_test_byteswap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    self.assertRaises(TypeError, a.byteswap, 42)
    if a.itemsize in (1, 2, 4, 8):
        b = array.array(self.typecode, self.example)
        b.byteswap()
        if a.itemsize == 1:
            self.assertEqual(a, b)
        else:
            self.assertNotEqual(a.tobytes(), b.tobytes())
        b.byteswap()
        self.assertEqual(a, b)
