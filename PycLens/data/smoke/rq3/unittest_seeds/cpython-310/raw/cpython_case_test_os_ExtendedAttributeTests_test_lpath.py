# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ExtendedAttributeTests_test_lpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_xattrs(os.getxattr, os.setxattr, os.removexattr, os.listxattr, follow_symlinks=False)
