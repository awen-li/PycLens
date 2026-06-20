# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_polar_errno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import set_errno

    def polar_with_errno_set(z):
        set_errno(11)
        try:
            return polar(z)
        finally:
            set_errno(0)
    self.check_polar(polar_with_errno_set)
