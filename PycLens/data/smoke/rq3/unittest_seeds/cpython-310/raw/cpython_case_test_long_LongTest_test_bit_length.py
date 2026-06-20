# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_bit_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tiny = 1e-10
    for x in range(-65000, 65000):
        k = x.bit_length()
        self.assertEqual(k, len(bin(x).lstrip('-0b')))
        if x != 0:
            self.assertTrue(2 ** (k - 1) <= abs(x) < 2 ** k)
        else:
            self.assertEqual(k, 0)
        if x != 0:
            self.assertEqual(k, 1 + math.floor(math.log(abs(x)) / math.log(2) + tiny))
    self.assertEqual(0 .bit_length(), 0)
    self.assertEqual(1 .bit_length(), 1)
    self.assertEqual((-1).bit_length(), 1)
    self.assertEqual(2 .bit_length(), 2)
    self.assertEqual((-2).bit_length(), 2)
    for i in [2, 3, 15, 16, 17, 31, 32, 33, 63, 64, 234]:
        a = 2 ** i
        self.assertEqual((a - 1).bit_length(), i)
        self.assertEqual((1 - a).bit_length(), i)
        self.assertEqual(a.bit_length(), i + 1)
        self.assertEqual((-a).bit_length(), i + 1)
        self.assertEqual((a + 1).bit_length(), i + 1)
        self.assertEqual((-a - 1).bit_length(), i + 1)
