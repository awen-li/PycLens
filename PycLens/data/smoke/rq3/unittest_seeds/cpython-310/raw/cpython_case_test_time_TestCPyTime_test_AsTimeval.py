# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestCPyTime_test_AsTimeval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import PyTime_AsTimeval
    us_converter = self.create_decimal_converter(US_TO_NS)

    def timeval_converter(ns):
        us = us_converter(ns)
        return divmod(us, SEC_TO_US)
    if sys.platform == 'win32':
        from _testcapi import LONG_MIN, LONG_MAX

        def seconds_filter(secs):
            return LONG_MIN <= secs <= LONG_MAX
    else:
        seconds_filter = self.time_t_filter
    self.check_int_rounding(PyTime_AsTimeval, timeval_converter, NS_TO_SEC, value_filter=seconds_filter)
