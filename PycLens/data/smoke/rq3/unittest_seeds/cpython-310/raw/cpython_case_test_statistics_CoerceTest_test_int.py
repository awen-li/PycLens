# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: CoerceTest_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_type_coercions(int)
    for typ in (float, Fraction, Decimal):
        self.check_coerce_to(int, typ)
