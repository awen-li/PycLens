# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualUnequalTest_test_exactly_unequal_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [9.51, 5723.05, 47.8, 9.17, 17.24]:
        self.do_exactly_unequal_test(x)
