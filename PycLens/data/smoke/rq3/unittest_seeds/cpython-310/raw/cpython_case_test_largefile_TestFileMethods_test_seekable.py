# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_largefile.py
# case: TestFileMethods_test_seekable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for pos in (2 ** 31 - 1, 2 ** 31, 2 ** 31 + 1):
        with self.open(TESTFN, 'rb') as f:
            f.seek(pos)
            self.assertTrue(f.seekable())
