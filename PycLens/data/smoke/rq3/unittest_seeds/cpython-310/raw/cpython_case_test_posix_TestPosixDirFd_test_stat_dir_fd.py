# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_stat_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare() as (dir_fd, name, fullname):
        with open(fullname, 'w') as outfile:
            outfile.write('testline\n')
        self.addCleanup(posix.unlink, fullname)
        s1 = posix.stat(fullname)
        s2 = posix.stat(name, dir_fd=dir_fd)
        self.assertEqual(s1, s2)
        s2 = posix.stat(fullname, dir_fd=None)
        self.assertEqual(s1, s2)
        self.assertRaisesRegex(TypeError, 'should be integer or None, not', posix.stat, name, dir_fd=posix.getcwd())
        self.assertRaisesRegex(TypeError, 'should be integer or None, not', posix.stat, name, dir_fd=float(dir_fd))
        self.assertRaises(OverflowError, posix.stat, name, dir_fd=10 ** 20)
