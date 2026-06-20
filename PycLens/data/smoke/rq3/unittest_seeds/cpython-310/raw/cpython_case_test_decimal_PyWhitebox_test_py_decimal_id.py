# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PyWhitebox_test_py_decimal_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = P.Decimal
    d = Decimal(45)
    e = Decimal(d)
    self.assertEqual(str(e), '45')
    self.assertNotEqual(id(d), id(e))
