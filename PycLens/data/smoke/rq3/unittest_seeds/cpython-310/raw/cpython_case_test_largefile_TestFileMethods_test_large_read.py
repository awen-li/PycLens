# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_largefile.py
# case: TestFileMethods_test_large_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(TESTFN, 'rb') as f:
        self.assertEqual(len(f.read()), size + 1)
        self.assertEqual(f.tell(), size + 1)
