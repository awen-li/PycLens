# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_posix_fadvise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    try:
        posix.posix_fadvise(fd, 0, 0, posix.POSIX_FADV_WILLNEED)
    finally:
        os.close(fd)
