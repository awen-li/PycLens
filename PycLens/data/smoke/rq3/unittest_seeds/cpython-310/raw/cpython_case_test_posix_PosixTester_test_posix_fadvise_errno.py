# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_posix_fadvise_errno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        posix.posix_fadvise(-42, 0, 0, posix.POSIX_FADV_WILLNEED)
    except OSError as inst:
        if inst.errno != errno.EBADF:
            raise
