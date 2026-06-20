# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_buffer_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    self.assertRaises(TypeError, a.buffer_info, 42)
    bi = a.buffer_info()
    self.assertIsInstance(bi, tuple)
    self.assertEqual(len(bi), 2)
    self.assertIsInstance(bi[0], int)
    self.assertIsInstance(bi[1], int)
    self.assertEqual(bi[1], len(a))
