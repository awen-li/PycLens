# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_largefile.py
# case: TestFileMethods_test_seek_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(TESTFN, 'rb') as f:
        self.assertEqual(f.tell(), 0)
        self.assertEqual(f.read(1), b'z')
        self.assertEqual(f.tell(), 1)
        f.seek(0)
        self.assertEqual(f.tell(), 0)
        f.seek(0, 0)
        self.assertEqual(f.tell(), 0)
        f.seek(42)
        self.assertEqual(f.tell(), 42)
        f.seek(42, 0)
        self.assertEqual(f.tell(), 42)
        f.seek(42, 1)
        self.assertEqual(f.tell(), 84)
        f.seek(0, 1)
        self.assertEqual(f.tell(), 84)
        f.seek(0, 2)
        self.assertEqual(f.tell(), size + 1 + 0)
        f.seek(-10, 2)
        self.assertEqual(f.tell(), size + 1 - 10)
        f.seek(-size - 1, 2)
        self.assertEqual(f.tell(), 0)
        f.seek(size)
        self.assertEqual(f.tell(), size)
        self.assertEqual(f.read(1), b'a')
        f.seek(-size - 1, 1)
        self.assertEqual(f.read(1), b'z')
        self.assertEqual(f.tell(), 1)
