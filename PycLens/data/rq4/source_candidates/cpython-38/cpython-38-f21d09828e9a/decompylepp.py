# Source Generated with Decompyle++
# File: cpython-38-f21d09828e9a.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vals = [
        0,
        0,
        1e-315,
        1e-200,
        0.0123,
        3.1415,
        1e+50,
        INF,
        NAN]
    vals += (lambda .0: [ -v for v in .0 ])(vals)
    for x in vals:
        for y in vals:
            z = complex(x, y)
            roundtrip = complex(repr(z))
            self.assertFloatsAreIdentical(z.real, roundtrip.real)
            self.assertFloatsAreIdentical(z.imag, roundtrip.imag)
    inf = float('inf')
    nan = float('nan')
    infj = complex(0, inf)
    nanj = complex(0, nan)
    for x in vals:
        for y in vals:
            z = complex(x, y)
            roundtrip = eval(repr(z))
            self.assertFloatsAreIdentical(0 + z.real, 0 + roundtrip.real)
            self.assertFloatsAreIdentical(0 + z.imag, 0 + roundtrip.imag)

# WARNING: Decompyle incomplete
