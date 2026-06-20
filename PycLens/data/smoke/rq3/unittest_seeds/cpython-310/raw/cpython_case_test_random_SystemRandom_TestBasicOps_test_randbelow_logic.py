# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_randbelow_logic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(1, 1000):
        n = 1 << i
        numbits = i + 1
        k = int(1.00001 + _log(n, 2))
        self.assertEqual(k, numbits)
        self.assertEqual(n, 2 ** (k - 1))
        n += n - 1
        k = int(1.00001 + _log(n, 2))
        self.assertIn(k, [numbits, numbits + 1])
        self.assertTrue(2 ** k > n > 2 ** (k - 2))
        n -= n >> 15
        k = int(1.00001 + _log(n, 2))
        self.assertEqual(k, numbits)
        self.assertTrue(2 ** k > n > 2 ** (k - 1))
