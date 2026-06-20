# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_largefile.py
# case: TestFileMethods_test_truncate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(TESTFN, 'r+b') as f:
        if not hasattr(f, 'truncate'):
            raise unittest.SkipTest('open().truncate() not available on this system')
        f.seek(0, 2)
        self.assertEqual(f.tell(), size + 1)
        newsize = size - 10
        f.seek(newsize)
        f.truncate()
        self.assertEqual(f.tell(), newsize)
        f.seek(0, 2)
        self.assertEqual(f.tell(), newsize)
        newsize -= 1
        f.seek(42)
        f.truncate(newsize)
        self.assertEqual(f.tell(), 42)
        f.seek(0, 2)
        self.assertEqual(f.tell(), newsize)
        f.seek(0)
        f.truncate(1)
        self.assertEqual(f.tell(), 0)
        f.seek(0)
        self.assertEqual(len(f.read()), 1)
