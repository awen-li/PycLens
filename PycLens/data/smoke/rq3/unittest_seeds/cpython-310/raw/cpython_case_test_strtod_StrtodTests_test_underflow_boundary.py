# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_underflow_boundary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for exponent in range(-400, -320):
        base = 10 ** (-exponent) // 2 ** 1075
        for j in range(TEST_SIZE):
            digits = base + random.randrange(-1000, 1000)
            s = '{}e{}'.format(digits, exponent)
            self.check_strtod(s)
