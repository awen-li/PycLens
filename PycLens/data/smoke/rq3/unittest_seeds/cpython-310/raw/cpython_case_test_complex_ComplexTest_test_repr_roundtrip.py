# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_repr_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vals = [0.0, 0.0, 1e-315, 1e-200, 0.0123, 3.1415, 1e+50, INF, NAN]
    vals += [-v for v in vals]
    for x in vals:
        for y in vals:
            z = complex(x, y)
            roundtrip = complex(repr(z))
            self.assertFloatsAreIdentical(z.real, roundtrip.real)
            self.assertFloatsAreIdentical(z.imag, roundtrip.imag)
    (inf, nan) = (float('inf'), float('nan'))
    (infj, nanj) = (complex(0.0, inf), complex(0.0, nan))
    for x in vals:
        for y in vals:
            z = complex(x, y)
            roundtrip = eval(repr(z))
            self.assertFloatsAreIdentical(0.0 + z.real, 0.0 + roundtrip.real)
            self.assertFloatsAreIdentical(0.0 + z.imag, 0.0 + roundtrip.imag)
