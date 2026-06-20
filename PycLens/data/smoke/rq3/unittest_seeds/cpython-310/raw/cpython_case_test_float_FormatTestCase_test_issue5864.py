# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: FormatTestCase_test_issue5864

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(format(123.456, '.4'), '123.5')
    self.assertEqual(format(1234.56, '.4'), '1.235e+03')
    self.assertEqual(format(12345.6, '.4'), '1.235e+04')
