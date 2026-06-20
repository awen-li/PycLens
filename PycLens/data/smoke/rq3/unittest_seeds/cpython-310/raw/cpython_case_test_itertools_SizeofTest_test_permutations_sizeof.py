# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: SizeofTest_test_permutations_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    basesize = support.calcobjsize('4Pni')
    check = self.check_sizeof
    check(permutations('abcd'), basesize + 4 * self.ssize_t + 4 * self.ssize_t)
    check(permutations('abcd', 3), basesize + 4 * self.ssize_t + 3 * self.ssize_t)
    check(permutations('abcde', 3), basesize + 5 * self.ssize_t + 3 * self.ssize_t)
    check(permutations(range(10), 4), basesize + 10 * self.ssize_t + 4 * self.ssize_t)
