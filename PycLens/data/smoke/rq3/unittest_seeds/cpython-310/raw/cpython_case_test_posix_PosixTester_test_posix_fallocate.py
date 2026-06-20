# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_posix_fallocate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_CREAT)
    try:
        posix.posix_fallocate(fd, 0, 10)
    except OSError as inst:
        if inst.errno == errno.EINVAL and sys.platform.startswith(('sunos', 'freebsd', 'netbsd', 'openbsd', 'gnukfreebsd')):
            raise unittest.SkipTest('test may fail on ZFS filesystems')
        else:
            raise
    finally:
        os.close(fd)
