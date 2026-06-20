# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: FormatTestCase_test_issue35560

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(format(123.0, '00'), '123.0')
    self.assertEqual(format(123.34, '00f'), '123.340000')
    self.assertEqual(format(123.34, '00e'), '1.233400e+02')
    self.assertEqual(format(123.34, '00g'), '123.34')
    self.assertEqual(format(123.34, '00.10f'), '123.3400000000')
    self.assertEqual(format(123.34, '00.10e'), '1.2334000000e+02')
    self.assertEqual(format(123.34, '00.10g'), '123.34')
    self.assertEqual(format(123.34, '01f'), '123.340000')
    self.assertEqual(format(-123.0, '00'), '-123.0')
    self.assertEqual(format(-123.34, '00f'), '-123.340000')
    self.assertEqual(format(-123.34, '00e'), '-1.233400e+02')
    self.assertEqual(format(-123.34, '00g'), '-123.34')
    self.assertEqual(format(-123.34, '00.10f'), '-123.3400000000')
    self.assertEqual(format(-123.34, '00.10f'), '-123.3400000000')
    self.assertEqual(format(-123.34, '00.10e'), '-1.2334000000e+02')
    self.assertEqual(format(-123.34, '00.10g'), '-123.34')
