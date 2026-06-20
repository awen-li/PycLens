# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_write_to_readonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, mode='w') as zipfp:
        zipfp.writestr('somefile.txt', 'bogus')
    with zipfile.ZipFile(TESTFN2, mode='r') as zipfp:
        self.assertRaises(ValueError, zipfp.write, TESTFN)
    with zipfile.ZipFile(TESTFN2, mode='r') as zipfp:
        with self.assertRaises(ValueError):
            zipfp.open(TESTFN, mode='w')
