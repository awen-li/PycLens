# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_fstat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = open(os_helper.TESTFN)
    try:
        self.assertTrue(posix.fstat(fp.fileno()))
        self.assertTrue(posix.stat(fp.fileno()))
        self.assertRaisesRegex(TypeError, 'should be string, bytes, os.PathLike or integer, not', posix.stat, float(fp.fileno()))
    finally:
        fp.close()
