# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_getrandbits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for k in range(1, 1000):
        self.assertTrue(0 <= self.gen.getrandbits(k) < 2 ** k)
    self.assertEqual(self.gen.getrandbits(0), 0)
    getbits = self.gen.getrandbits
    for span in [1, 2, 3, 4, 31, 32, 32, 52, 53, 54, 119, 127, 128, 129]:
        all_bits = 2 ** span - 1
        cum = 0
        cpl_cum = 0
        for i in range(100):
            v = getbits(span)
            cum |= v
            cpl_cum |= all_bits ^ v
        self.assertEqual(cum, all_bits)
        self.assertEqual(cpl_cum, all_bits)
    self.assertRaises(TypeError, self.gen.getrandbits)
    self.assertRaises(TypeError, self.gen.getrandbits, 1, 2)
    self.assertRaises(ValueError, self.gen.getrandbits, -1)
    self.assertRaises(TypeError, self.gen.getrandbits, 10.1)
