# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: SizeofTest_test_product_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    basesize = support.calcobjsize('3Pi')
    check = self.check_sizeof
    check(product('ab', '12'), basesize + 2 * self.ssize_t)
    check(product(*('abc',) * 10), basesize + 10 * self.ssize_t)
