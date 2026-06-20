# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_bit_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for a in range(-1000, 1000):
        self.assertEqual(a.bit_count(), bin(a).count('1'))
    for exp in [10, 17, 63, 64, 65, 1009, 70234, 1234567]:
        a = 2 ** exp
        self.assertEqual(a.bit_count(), 1)
        self.assertEqual((a - 1).bit_count(), exp)
        self.assertEqual((a ^ 63).bit_count(), 7)
        self.assertEqual((a - 1 ^ 510).bit_count(), exp - 8)
