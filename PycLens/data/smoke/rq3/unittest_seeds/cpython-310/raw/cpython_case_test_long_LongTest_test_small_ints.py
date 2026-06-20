# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_small_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(-5, 257):
        self.assertIs(i, i + 0)
        self.assertIs(i, i * 1)
        self.assertIs(i, i - 0)
        self.assertIs(i, i // 1)
        self.assertIs(i, i & -1)
        self.assertIs(i, i | 0)
        self.assertIs(i, i ^ 0)
        self.assertIs(i, ~~i)
        self.assertIs(i, i ** 1)
        self.assertIs(i, int(str(i)))
        self.assertIs(i, i << 2 >> 2, str(i))
    i = 1 << 70
    self.assertIs(i - i, 0)
    self.assertIs(0 * i, 0)
