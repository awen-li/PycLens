# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PyWhitebox_test_py_rescale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = P.Decimal
    localcontext = P.localcontext
    with localcontext() as c:
        x = Decimal('NaN')._rescale(3, ROUND_UP)
        self.assertTrue(x.is_nan())
