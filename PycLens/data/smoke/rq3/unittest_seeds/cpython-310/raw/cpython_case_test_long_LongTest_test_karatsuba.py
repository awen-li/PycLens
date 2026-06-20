# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_karatsuba

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    digits = list(range(1, 5)) + list(range(KARATSUBA_CUTOFF, KARATSUBA_CUTOFF + 10))
    digits.extend([KARATSUBA_CUTOFF * 10, KARATSUBA_CUTOFF * 100])
    bits = [digit * SHIFT for digit in digits]
    for abits in bits:
        a = (1 << abits) - 1
        for bbits in bits:
            if bbits < abits:
                continue
            with self.subTest(abits=abits, bbits=bbits):
                b = (1 << bbits) - 1
                x = a * b
                y = (1 << abits + bbits) - (1 << abits) - (1 << bbits) + 1
                self.assertEqual(x, y)
