# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestFormatPatternArg_test_onlyOnePattern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with check_warnings(('', DeprecationWarning)):
        self.assertRaises(ValueError, locale.format, '%f\n', 'foo')
        self.assertRaises(ValueError, locale.format, '%f\r', 'foo')
        self.assertRaises(ValueError, locale.format, '%f\r\n', 'foo')
        self.assertRaises(ValueError, locale.format, ' %f', 'foo')
        self.assertRaises(ValueError, locale.format, '%fg', 'foo')
        self.assertRaises(ValueError, locale.format, '%^g', 'foo')
        self.assertRaises(ValueError, locale.format, '%f%%', 'foo')
