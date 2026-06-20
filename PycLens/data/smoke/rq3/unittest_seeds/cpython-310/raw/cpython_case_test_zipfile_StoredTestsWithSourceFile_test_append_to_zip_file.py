# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_append_to_zip_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', zipfile.ZIP_STORED) as zipfp:
        zipfp.write(TESTFN, TESTFN)
    with zipfile.ZipFile(TESTFN2, 'a', zipfile.ZIP_STORED) as zipfp:
        zipfp.writestr('strfile', self.data)
        self.assertEqual(zipfp.namelist(), [TESTFN, 'strfile'])
