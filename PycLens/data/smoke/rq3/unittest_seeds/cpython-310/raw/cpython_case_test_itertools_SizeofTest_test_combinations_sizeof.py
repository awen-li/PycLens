# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: SizeofTest_test_combinations_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    basesize = support.calcobjsize('3Pni')
    check = self.check_sizeof
    check(combinations('abcd', 3), basesize + 3 * self.ssize_t)
    check(combinations(range(10), 4), basesize + 4 * self.ssize_t)
