# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_correctly_rounded_true_division

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_truediv(123, 0)
    self.check_truediv(-456, 0)
    self.check_truediv(0, 3)
    self.check_truediv(0, -3)
    self.check_truediv(0, 0)
    self.check_truediv(671 * 12345 * 2 ** DBL_MAX_EXP, 12345)
    self.check_truediv(12345, 345678 * 2 ** (DBL_MANT_DIG - DBL_MIN_EXP))
    self.check_truediv(12345 * 2 ** 100, 98765)
    self.check_truediv(12345 * 2 ** 30, 98765 * 7 ** 81)
    bases = (0, DBL_MANT_DIG, DBL_MIN_EXP, DBL_MAX_EXP, DBL_MIN_EXP - DBL_MANT_DIG)
    for base in bases:
        for exp in range(base - 15, base + 15):
            self.check_truediv(75312 * 2 ** max(exp, 0), 69187 * 2 ** max(-exp, 0))
            self.check_truediv(69187 * 2 ** max(exp, 0), 75312 * 2 ** max(-exp, 0))
    for m in [1, 2, 7, 17, 12345, 7 ** 100, -1, -2, -5, -23, -67891, -41 ** 50]:
        for n in range(-10, 10):
            self.check_truediv(m * DBL_MIN_OVERFLOW + n, m)
            self.check_truediv(m * DBL_MIN_OVERFLOW + n, -m)
    for n in range(250):
        self.check_truediv((2 ** DBL_MANT_DIG + 1) * 12345 * 2 ** 200 + 2 ** n, 2 ** DBL_MANT_DIG * 12345)
    self.check_truediv(1, 2731)
    self.check_truediv(295147931372582273023, 295147932265116303360)
    for i in range(1000):
        self.check_truediv(10 ** (i + 1), 10 ** i)
        self.check_truediv(10 ** i, 10 ** (i + 1))
    for m in [1, 2, 4, 7, 8, 16, 17, 32, 12345, 7 ** 100, -1, -2, -5, -23, -67891, -41 ** 50]:
        for n in range(-10, 10):
            self.check_truediv(2 ** DBL_MANT_DIG * m + n, m)
    for n in range(-20, 20):
        self.check_truediv(n, 2 ** 1076)
    for M in [10 ** 10, 10 ** 100, 10 ** 1000]:
        for i in range(1000):
            a = random.randrange(1, M)
            b = random.randrange(a, 2 * a + 1)
            self.check_truediv(a, b)
            self.check_truediv(-a, b)
            self.check_truediv(a, -b)
            self.check_truediv(-a, -b)
    for _ in range(10000):
        a_bits = random.randrange(1000)
        b_bits = random.randrange(1, 1000)
        x = random.randrange(2 ** a_bits)
        y = random.randrange(1, 2 ** b_bits)
        self.check_truediv(x, y)
        self.check_truediv(x, -y)
        self.check_truediv(-x, y)
        self.check_truediv(-x, -y)
