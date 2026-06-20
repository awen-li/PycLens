# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_stat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(posix.stat(os_helper.TESTFN))
    self.assertTrue(posix.stat(os.fsencode(os_helper.TESTFN)))
    self.assertWarnsRegex(DeprecationWarning, 'should be string, bytes, os.PathLike or integer, not', posix.stat, bytearray(os.fsencode(os_helper.TESTFN)))
    self.assertRaisesRegex(TypeError, 'should be string, bytes, os.PathLike or integer, not', posix.stat, None)
    self.assertRaisesRegex(TypeError, 'should be string, bytes, os.PathLike or integer, not', posix.stat, list(os_helper.TESTFN))
    self.assertRaisesRegex(TypeError, 'should be string, bytes, os.PathLike or integer, not', posix.stat, list(os.fsencode(os_helper.TESTFN)))
