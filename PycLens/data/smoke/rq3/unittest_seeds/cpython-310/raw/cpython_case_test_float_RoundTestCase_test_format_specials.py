# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_format_specials

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(fmt, value, expected):
        self.assertEqual(fmt % value, expected, fmt)
        fmt = fmt[1:]
        self.assertEqual(format(value, fmt), expected, fmt)
    for fmt in ['%e', '%f', '%g', '%.0e', '%.6f', '%.20g', '%#e', '%#f', '%#g', '%#.20e', '%#.15f', '%#.3g']:
        pfmt = '%+' + fmt[1:]
        sfmt = '% ' + fmt[1:]
        test(fmt, INF, 'inf')
        test(fmt, -INF, '-inf')
        test(fmt, NAN, 'nan')
        test(fmt, -NAN, 'nan')
        test(pfmt, INF, '+inf')
        test(pfmt, -INF, '-inf')
        test(pfmt, NAN, '+nan')
        test(pfmt, -NAN, '+nan')
        test(sfmt, INF, ' inf')
        test(sfmt, -INF, '-inf')
        test(sfmt, NAN, ' nan')
        test(sfmt, -NAN, ' nan')
