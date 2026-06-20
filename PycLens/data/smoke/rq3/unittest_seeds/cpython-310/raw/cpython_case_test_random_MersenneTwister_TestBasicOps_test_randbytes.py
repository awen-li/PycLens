# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_randbytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_randbytes()
    seed = 8675309
    expected = b'3\xa8\xf9f\xf4\xa4\xd06\x19\x8f\x9f\x82\x02oe\xf0'
    self.gen.seed(seed)
    self.assertEqual(self.gen.randbytes(16), expected)
    self.gen.seed(seed)
    self.assertEqual(self.gen.randbytes(0), b'')
    self.assertEqual(self.gen.randbytes(16), expected)
    self.gen.seed(seed)
    self.assertEqual(b''.join([self.gen.randbytes(4) for _ in range(4)]), expected)
    self.gen.seed(seed)
    expected1 = expected[3::4]
    self.assertEqual(b''.join((self.gen.randbytes(1) for _ in range(4))), expected1)
    self.gen.seed(seed)
    expected2 = b''.join((expected[i + 2:i + 4] for i in range(0, len(expected), 4)))
    self.assertEqual(b''.join((self.gen.randbytes(2) for _ in range(4))), expected2)
    self.gen.seed(seed)
    expected3 = b''.join((expected[i + 1:i + 4] for i in range(0, len(expected), 4)))
    self.assertEqual(b''.join((self.gen.randbytes(3) for _ in range(4))), expected3)
