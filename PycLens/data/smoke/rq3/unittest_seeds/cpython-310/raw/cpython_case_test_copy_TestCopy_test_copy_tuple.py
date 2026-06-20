# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = (1, 2, 3)
    self.assertIs(copy.copy(x), x)
    x = ()
    self.assertIs(copy.copy(x), x)
    x = (1, 2, 3, [])
    self.assertIs(copy.copy(x), x)
