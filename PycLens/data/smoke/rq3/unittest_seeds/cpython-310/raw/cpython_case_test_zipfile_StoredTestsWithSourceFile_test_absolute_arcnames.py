# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_absolute_arcnames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', zipfile.ZIP_STORED) as zipfp:
        zipfp.write(TESTFN, '/absolute')
    with zipfile.ZipFile(TESTFN2, 'r', zipfile.ZIP_STORED) as zipfp:
        self.assertEqual(zipfp.namelist(), ['absolute'])
