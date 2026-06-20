# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestOldPyTime_test_object_to_time_t

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import pytime_object_to_time_t
    self.check_int_rounding(pytime_object_to_time_t, lambda secs: secs, value_filter=self.time_t_filter)
    self.check_float_rounding(pytime_object_to_time_t, self.decimal_round, value_filter=self.time_t_filter)
