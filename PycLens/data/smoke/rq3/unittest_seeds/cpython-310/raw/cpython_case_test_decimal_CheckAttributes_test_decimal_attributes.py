# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CheckAttributes_test_decimal_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = [s for s in dir(C.Decimal(9)) if '__' in s or not s.startswith('_')]
    y = [s for s in dir(C.Decimal(9)) if '__' in s or not s.startswith('_')]
    self.assertEqual(set(x) - set(y), set())
