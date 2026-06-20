# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestCPyTime_test_AsTimespec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import PyTime_AsTimespec

    def timespec_converter(ns):
        return divmod(ns, SEC_TO_NS)
    self.check_int_rounding(lambda ns, rnd: PyTime_AsTimespec(ns), timespec_converter, NS_TO_SEC, value_filter=self.time_t_filter)
