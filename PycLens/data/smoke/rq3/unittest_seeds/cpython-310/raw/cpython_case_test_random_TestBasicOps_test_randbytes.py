# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_randbytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in range(1, 10):
        data = self.gen.randbytes(n)
        self.assertEqual(type(data), bytes)
        self.assertEqual(len(data), n)
    self.assertEqual(self.gen.randbytes(0), b'')
    self.assertRaises(TypeError, self.gen.randbytes)
    self.assertRaises(TypeError, self.gen.randbytes, 1, 2)
    self.assertRaises(ValueError, self.gen.randbytes, -1)
    self.assertRaises(TypeError, self.gen.randbytes, 1.0)
