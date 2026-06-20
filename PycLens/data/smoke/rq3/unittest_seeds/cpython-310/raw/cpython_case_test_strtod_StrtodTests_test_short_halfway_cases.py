# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_short_halfway_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for k in (0, 5, 10, 15, 20):
        upper = -(-2 ** 54 // 5 ** k)
        lower = -(-2 ** 53 // 5 ** k)
        if lower % 2 == 0:
            lower += 1
        for i in range(TEST_SIZE):
            (n, e) = (random.randrange(lower, upper, 2), k)
            while n % 5 == 0:
                (n, e) = (n // 5, e + 1)
            assert n % 10 in (1, 3, 7, 9)
            (digits, exponent) = (n, e)
            while digits < 10 ** 20:
                s = '{}e{}'.format(digits, exponent)
                self.check_strtod(s)
                s = '{}e{}'.format(digits * 10 ** 40, exponent - 40)
                self.check_strtod(s)
                digits *= 2
            (digits, exponent) = (n, e)
            while digits < 10 ** 20:
                s = '{}e{}'.format(digits, exponent)
                self.check_strtod(s)
                s = '{}e{}'.format(digits * 10 ** 40, exponent - 40)
                self.check_strtod(s)
                digits *= 5
                exponent -= 1
