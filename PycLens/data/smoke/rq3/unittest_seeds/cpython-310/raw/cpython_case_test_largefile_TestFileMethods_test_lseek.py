# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_largefile.py
# case: TestFileMethods_test_lseek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(TESTFN, 'rb') as f:
        self.assertEqual(os.lseek(f.fileno(), 0, 0), 0)
        self.assertEqual(os.lseek(f.fileno(), 42, 0), 42)
        self.assertEqual(os.lseek(f.fileno(), 42, 1), 84)
        self.assertEqual(os.lseek(f.fileno(), 0, 1), 84)
        self.assertEqual(os.lseek(f.fileno(), 0, 2), size + 1 + 0)
        self.assertEqual(os.lseek(f.fileno(), -10, 2), size + 1 - 10)
        self.assertEqual(os.lseek(f.fileno(), -size - 1, 2), 0)
        self.assertEqual(os.lseek(f.fileno(), size, 0), size)
        self.assertEqual(f.read(1), b'a')
