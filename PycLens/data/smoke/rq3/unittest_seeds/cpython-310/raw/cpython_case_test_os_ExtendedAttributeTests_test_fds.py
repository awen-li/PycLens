# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ExtendedAttributeTests_test_fds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def getxattr(path, *args):
        with open(path, 'rb') as fp:
            return os.getxattr(fp.fileno(), *args)

    def setxattr(path, *args):
        with open(path, 'wb', 0) as fp:
            os.setxattr(fp.fileno(), *args)

    def removexattr(path, *args):
        with open(path, 'wb', 0) as fp:
            os.removexattr(fp.fileno(), *args)

    def listxattr(path, *args):
        with open(path, 'rb') as fp:
            return os.listxattr(fp.fileno(), *args)
    self._check_xattrs(getxattr, setxattr, removexattr, listxattr)
