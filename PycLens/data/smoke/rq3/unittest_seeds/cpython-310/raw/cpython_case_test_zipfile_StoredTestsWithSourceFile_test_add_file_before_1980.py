# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestsWithSourceFile_test_add_file_before_1980

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.utime(TESTFN, (0, 0))
    with zipfile.ZipFile(TESTFN2, 'w') as zipfp:
        self.assertRaises(ValueError, zipfp.write, TESTFN)
    with zipfile.ZipFile(TESTFN2, 'w', strict_timestamps=False) as zipfp:
        zipfp.write(TESTFN)
        zinfo = zipfp.getinfo(TESTFN)
        self.assertEqual(zinfo.date_time, (1980, 1, 1, 0, 0, 0))
