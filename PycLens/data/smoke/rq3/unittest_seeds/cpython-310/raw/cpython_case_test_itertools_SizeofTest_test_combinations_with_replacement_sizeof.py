# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: SizeofTest_test_combinations_with_replacement_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cwr = combinations_with_replacement
    basesize = support.calcobjsize('3Pni')
    check = self.check_sizeof
    check(cwr('abcd', 3), basesize + 3 * self.ssize_t)
    check(cwr(range(10), 4), basesize + 4 * self.ssize_t)
