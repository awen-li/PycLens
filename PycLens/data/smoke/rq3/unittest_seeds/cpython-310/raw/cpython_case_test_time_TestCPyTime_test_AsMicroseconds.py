# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestCPyTime_test_AsMicroseconds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import PyTime_AsMicroseconds
    self.check_int_rounding(PyTime_AsMicroseconds, self.create_decimal_converter(US_TO_NS), NS_TO_SEC)
