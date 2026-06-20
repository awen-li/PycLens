# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_empty_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipf = zipfile.ZipFile(TESTFN, mode='w')
    zipf.close()
    try:
        zipf = zipfile.ZipFile(TESTFN, mode='r')
    except zipfile.BadZipFile:
        self.fail("Unable to create empty ZIP file in 'w' mode")
    zipf = zipfile.ZipFile(TESTFN, mode='a')
    zipf.close()
    try:
        zipf = zipfile.ZipFile(TESTFN, mode='r')
    except:
        self.fail("Unable to create empty ZIP file in 'a' mode")
