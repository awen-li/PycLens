# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_g_format_has_no_trailing_zeros

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('%.3g' % 1505.0, '1.5e+03')
    self.assertEqual('%#.3g' % 1505.0, '1.50e+03')
    self.assertEqual(format(1505.0, '.3g'), '1.5e+03')
    self.assertEqual(format(1505.0, '#.3g'), '1.50e+03')
    self.assertEqual(format(12300050.0, '.6g'), '1.23e+07')
    self.assertEqual(format(12300050.0, '#.6g'), '1.23000e+07')
