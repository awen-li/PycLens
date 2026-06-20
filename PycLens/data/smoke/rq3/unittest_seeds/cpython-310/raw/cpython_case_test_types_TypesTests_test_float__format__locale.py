# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_float__format__locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(-10, 10):
        x = 1234567890.0 * 10.0 ** i
        self.assertEqual(locale.format_string('%g', x, grouping=True), format(x, 'n'))
        self.assertEqual(locale.format_string('%.10g', x, grouping=True), format(x, '.10n'))
