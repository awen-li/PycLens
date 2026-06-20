# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_errno.py
# case: ErrnoAttributeTests_test_using_errorcode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for value in errno.errorcode.values():
        self.assertTrue(hasattr(errno, value), 'no %s attr in errno' % value)
