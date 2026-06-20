# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: SumSpecialValues_test_decimal_snan_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sNAN = Decimal('sNAN')
    data = [1, sNAN, 2]
    self.assertRaises(decimal.InvalidOperation, statistics._sum, data)
