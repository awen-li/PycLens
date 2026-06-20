# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_boundaries

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    boundaries = [(10000000000000000000, -19, 1110), (17976931348623159077, 289, 1995), (22250738585072013831, -327, 4941), (0, -327, 4941)]
    for (n, e, u) in boundaries:
        for j in range(1000):
            digits = n + random.randrange(-3 * u, 3 * u)
            exponent = e
            s = '{}e{}'.format(digits, exponent)
            self.check_strtod(s)
            n *= 10
            u *= 10
            e -= 1
