# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestCPyTime_test_FromSecondsObject

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import PyTime_FromSecondsObject
    self.check_int_rounding(PyTime_FromSecondsObject, lambda secs: secs * SEC_TO_NS)
    self.check_float_rounding(PyTime_FromSecondsObject, lambda ns: self.decimal_round(ns * SEC_TO_NS))
    for (time_rnd, _) in ROUNDING_MODES:
        with self.assertRaises(ValueError):
            PyTime_FromSecondsObject(float('nan'), time_rnd)
