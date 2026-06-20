# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_errno.py
# case: ErrnoAttributeTests_test_for_improper_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for error_code in std_c_errors:
        self.assertTrue(hasattr(errno, error_code), 'errno is missing %s' % error_code)
