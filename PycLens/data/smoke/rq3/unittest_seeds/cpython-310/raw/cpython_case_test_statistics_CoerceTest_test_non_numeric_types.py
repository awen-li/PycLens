# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: CoerceTest_test_non_numeric_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for bad_type in (str, list, type(None), tuple, dict):
        for good_type in (int, float, Fraction, Decimal):
            self.assertCoerceRaises(good_type, bad_type)
