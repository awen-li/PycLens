# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_fdopen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_CREAT | os.O_RDWR)
    os.close(fd)
    self.fdopen_helper()
    self.fdopen_helper('r')
    self.fdopen_helper('r', 100)
