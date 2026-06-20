# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_listdir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = posix.open(posix.getcwd(), posix.O_RDONLY)
    self.addCleanup(posix.close, f)
    self.assertEqual(sorted(posix.listdir('.')), sorted(posix.listdir(f)))
    self.assertEqual(sorted(posix.listdir('.')), sorted(posix.listdir(f)))
