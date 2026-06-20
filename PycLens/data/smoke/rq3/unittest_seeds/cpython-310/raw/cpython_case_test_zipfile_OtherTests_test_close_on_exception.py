# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_close_on_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w') as zipfp:
        for (fpath, fdata) in SMALL_TEST_DATA:
            zipfp.writestr(fpath, fdata)
    try:
        with zipfile.ZipFile(TESTFN2, 'r') as zipfp2:
            raise zipfile.BadZipFile()
    except zipfile.BadZipFile:
        self.assertIsNone(zipfp2.fp, 'zipfp is not closed')
