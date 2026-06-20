# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_input_restriction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    InvalidOperation = C.InvalidOperation
    Context = C.Context
    localcontext = C.localcontext
    with localcontext(Context()):
        self.assertRaises(InvalidOperation, Decimal, '1e9999999999999999999')
