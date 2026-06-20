# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_open_empty_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = open(TESTFN, 'w', encoding='utf-8')
    f.close()
    self.assertRaises(zipfile.BadZipFile, zipfile.ZipFile, TESTFN, 'r')
