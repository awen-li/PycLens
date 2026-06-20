# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_fs_holes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'r+b') as fp:
        fp.write(b'hello')
        fp.flush()
        size = fp.tell()
        fno = fp.fileno()
        try:
            for i in range(size):
                self.assertEqual(i, os.lseek(fno, i, os.SEEK_DATA))
                self.assertLessEqual(size, os.lseek(fno, i, os.SEEK_HOLE))
            self.assertRaises(OSError, os.lseek, fno, size, os.SEEK_DATA)
            self.assertRaises(OSError, os.lseek, fno, size, os.SEEK_HOLE)
        except OSError:
            raise unittest.SkipTest('OSError raised!')
