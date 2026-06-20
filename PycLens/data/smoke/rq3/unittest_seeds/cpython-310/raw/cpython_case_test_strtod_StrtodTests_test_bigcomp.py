# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_bigcomp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for ndigs in (5, 10, 14, 15, 16, 17, 18, 19, 20, 40, 41, 50):
        dig10 = 10 ** ndigs
        for i in range(10 * TEST_SIZE):
            digits = random.randrange(dig10)
            exponent = random.randrange(-400, 400)
            s = '{}e{}'.format(digits, exponent)
            self.check_strtod(s)
