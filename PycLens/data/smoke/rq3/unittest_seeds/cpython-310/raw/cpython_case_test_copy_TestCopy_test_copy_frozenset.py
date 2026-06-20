# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_frozenset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = frozenset({1, 2, 3})
    self.assertIs(copy.copy(x), x)
    x = frozenset()
    self.assertIs(copy.copy(x), x)
