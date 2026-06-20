# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_fchown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.unlink(os_helper.TESTFN)
    test_file = open(os_helper.TESTFN, 'w')
    try:
        fd = test_file.fileno()
        self._test_all_chown_common(posix.fchown, fd, getattr(posix, 'fstat', None))
    finally:
        test_file.close()
