# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestOldPyTime_test_object_to_timespec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import pytime_object_to_timespec
    self.check_int_rounding(pytime_object_to_timespec, lambda secs: (secs, 0), value_filter=self.time_t_filter)
    self.check_float_rounding(pytime_object_to_timespec, self.create_converter(SEC_TO_NS), value_filter=self.time_t_filter)
    for (time_rnd, _) in ROUNDING_MODES:
        with self.assertRaises(ValueError):
            pytime_object_to_timespec(float('nan'), time_rnd)
