# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_rop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    for attr in ('__radd__', '__rsub__', '__rmul__', '__rtruediv__', '__rdivmod__', '__rmod__', '__rfloordiv__', '__rpow__'):
        self.assertIs(getattr(Decimal('1'), attr)('xyz'), NotImplemented)
