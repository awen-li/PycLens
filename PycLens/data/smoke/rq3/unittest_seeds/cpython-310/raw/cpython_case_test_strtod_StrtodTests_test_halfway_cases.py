# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_halfway_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(100 * TEST_SIZE):
        bits = random.randrange(2047 * 2 ** 52)
        (e, m) = divmod(bits, 2 ** 52)
        if e:
            (m, e) = (m + 2 ** 52, e - 1)
        e -= 1074
        (m, e) = (2 * m + 1, e - 1)
        if e >= 0:
            digits = m << e
            exponent = 0
        else:
            digits = m * 5 ** (-e)
            exponent = e
        s = '{}e{}'.format(digits, exponent)
        self.check_strtod(s)
