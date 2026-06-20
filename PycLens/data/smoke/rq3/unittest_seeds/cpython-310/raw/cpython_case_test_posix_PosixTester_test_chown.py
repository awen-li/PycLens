# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_chown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.unlink(os_helper.TESTFN)
    self.assertRaises(OSError, posix.chown, os_helper.TESTFN, -1, -1)
    os_helper.create_empty_file(os_helper.TESTFN)
    self._test_all_chown_common(posix.chown, os_helper.TESTFN, posix.stat)
