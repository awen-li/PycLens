# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_truediv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    simple_real = [float(i) for i in range(-5, 6)]
    simple_complex = [complex(x, y) for x in simple_real for y in simple_real]
    for x in simple_complex:
        for y in simple_complex:
            self.check_div(x, y)
    self.check_div(complex(1e+200, 1e+200), 1 + 0j)
    self.check_div(complex(1e-200, 1e-200), 1 + 0j)
    for i in range(100):
        self.check_div(complex(random(), random()), complex(random(), random()))
    self.assertAlmostEqual(complex.__truediv__(2 + 0j, 1 + 1j), 1 - 1j)
    for (denom_real, denom_imag) in [(0, NAN), (NAN, 0), (NAN, NAN)]:
        z = complex(0, 0) / complex(denom_real, denom_imag)
        self.assertTrue(isnan(z.real))
        self.assertTrue(isnan(z.imag))
