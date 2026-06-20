# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_largefile.py
# case: TestCopyfile_test_it

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = os.path.getsize(TESTFN)
    shutil.copyfile(TESTFN, TESTFN2)
    self.assertEqual(os.path.getsize(TESTFN2), size)
    with open(TESTFN2, 'rb') as f:
        self.assertEqual(f.read(5), b'z\x00\x00\x00\x00')
        f.seek(size - 5)
        self.assertEqual(f.read(), b'\x00\x00\x00\x00a')
