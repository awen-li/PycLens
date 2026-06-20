# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_write_default_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w') as zipfp:
        zipfp.write(TESTFN)
        with open(TESTFN, 'rb') as f:
            self.assertEqual(zipfp.read(TESTFN), f.read())
