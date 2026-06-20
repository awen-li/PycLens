# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: HexFloatTestCase_test_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def roundtrip(x):
        return fromHex(toHex(x))
    for x in [NAN, INF, self.MAX, self.MIN, self.MIN - self.TINY, self.TINY, 0.0]:
        self.identical(x, roundtrip(x))
        self.identical(-x, roundtrip(-x))
    import random
    for i in range(10000):
        e = random.randrange(-1200, 1200)
        m = random.random()
        s = random.choice([1.0, -1.0])
        try:
            x = s * ldexp(m, e)
        except OverflowError:
            pass
        else:
            self.identical(x, fromHex(toHex(x)))
