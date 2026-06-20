# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_fcntl_64_bit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        cmd = fcntl.F_NOTIFY
        flags = fcntl.DN_MULTISHOT
    except AttributeError:
        self.skipTest('F_NOTIFY or DN_MULTISHOT unavailable')
    fd = os.open(os.path.dirname(os.path.abspath(TESTFN)), os.O_RDONLY)
    try:
        fcntl.fcntl(fd, cmd, flags)
    finally:
        os.close(fd)
