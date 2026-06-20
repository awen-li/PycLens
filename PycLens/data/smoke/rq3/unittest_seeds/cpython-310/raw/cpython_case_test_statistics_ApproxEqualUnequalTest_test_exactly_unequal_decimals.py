# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualUnequalTest_test_exactly_unequal_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for d in map(Decimal, '3.1415 298.12 3.47 18.996 0.00245'.split()):
        self.do_exactly_unequal_test(d)
