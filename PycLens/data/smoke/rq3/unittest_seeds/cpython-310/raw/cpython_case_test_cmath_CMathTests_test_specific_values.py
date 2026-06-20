# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_specific_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    SKIP_ON_TIGER = {'tan0064'}
    osx_version = None
    if sys.platform == 'darwin':
        version_txt = platform.mac_ver()[0]
        try:
            osx_version = tuple(map(int, version_txt.split('.')))
        except ValueError:
            pass

    def rect_complex(z):
        """Wrapped version of rect that accepts a complex number instead of
            two float arguments."""
        return cmath.rect(z.real, z.imag)

    def polar_complex(z):
        """Wrapped version of polar that returns a complex number instead of
            two floats."""
        return complex(*polar(z))
    for (id, fn, ar, ai, er, ei, flags) in parse_testfile(test_file):
        arg = complex(ar, ai)
        expected = complex(er, ei)
        if osx_version is not None and osx_version < (10, 5):
            if id in SKIP_ON_TIGER:
                continue
        if fn == 'rect':
            function = rect_complex
        elif fn == 'polar':
            function = polar_complex
        else:
            function = getattr(cmath, fn)
        if 'divide-by-zero' in flags or 'invalid' in flags:
            try:
                actual = function(arg)
            except ValueError:
                continue
            else:
                self.fail('ValueError not raised in test {}: {}(complex({!r}, {!r}))'.format(id, fn, ar, ai))
        if 'overflow' in flags:
            try:
                actual = function(arg)
            except OverflowError:
                continue
            else:
                self.fail('OverflowError not raised in test {}: {}(complex({!r}, {!r}))'.format(id, fn, ar, ai))
        actual = function(arg)
        if 'ignore-real-sign' in flags:
            actual = complex(abs(actual.real), actual.imag)
            expected = complex(abs(expected.real), expected.imag)
        if 'ignore-imag-sign' in flags:
            actual = complex(actual.real, abs(actual.imag))
            expected = complex(expected.real, abs(expected.imag))
        if fn in ('log', 'log10'):
            real_abs_err = 2e-15
        else:
            real_abs_err = 5e-323
        error_message = '{}: {}(complex({!r}, {!r}))\nExpected: complex({!r}, {!r})\nReceived: complex({!r}, {!r})\nReceived value insufficiently close to expected value.'.format(id, fn, ar, ai, expected.real, expected.imag, actual.real, actual.imag)
        self.rAssertAlmostEqual(expected.real, actual.real, abs_err=real_abs_err, msg=error_message)
        self.rAssertAlmostEqual(expected.imag, actual.imag, msg=error_message)
