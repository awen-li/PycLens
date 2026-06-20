# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestCPyTime_test_FromSeconds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import PyTime_FromSeconds

    def c_int_filter(secs):
        return _testcapi.INT_MIN <= secs <= _testcapi.INT_MAX
    self.check_int_rounding(lambda secs, rnd: PyTime_FromSeconds(secs), lambda secs: secs * SEC_TO_NS, value_filter=c_int_filter)
    for (time_rnd, _) in ROUNDING_MODES:
        with self.assertRaises(TypeError):
            PyTime_FromSeconds(float('nan'))
