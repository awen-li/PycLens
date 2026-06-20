# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_msilib.py
# case: Test_make_id_test_invalid_first_char

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(msilib.make_id('9.short'), '_9.short')
    self.assertEqual(msilib.make_id('.short'), '_.short')
