# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    digits = '000000123456789'
    signs = ('+', '-', '')
    for i in range(1000):
        for j in range(TEST_SIZE):
            s = random.choice(signs)
            intpart_len = random.randrange(5)
            s += ''.join((random.choice(digits) for _ in range(intpart_len)))
            if random.choice([True, False]):
                s += '.'
                fracpart_len = random.randrange(5)
                s += ''.join((random.choice(digits) for _ in range(fracpart_len)))
            else:
                fracpart_len = 0
            if random.choice([True, False]):
                s += random.choice(['e', 'E'])
                s += random.choice(signs)
                exponent_len = random.randrange(1, 4)
                s += ''.join((random.choice(digits) for _ in range(exponent_len)))
            if intpart_len + fracpart_len:
                self.check_strtod(s)
            else:
                try:
                    float(s)
                except ValueError:
                    pass
                else:
                    assert False, 'expected ValueError'
