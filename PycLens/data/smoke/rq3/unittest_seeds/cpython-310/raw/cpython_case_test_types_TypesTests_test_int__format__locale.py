# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_int__format__locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 123456789012345678901234567890
    for i in range(0, 30):
        self.assertEqual(locale.format_string('%d', x, grouping=True), format(x, 'n'))
        x = x // 10
    rfmt = '>20n'
    lfmt = '<20n'
    cfmt = '^20n'
    for x in (1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890, 12345678900):
        self.assertEqual(len(format(0, rfmt)), len(format(x, rfmt)))
        self.assertEqual(len(format(0, lfmt)), len(format(x, lfmt)))
        self.assertEqual(len(format(0, cfmt)), len(format(x, cfmt)))
