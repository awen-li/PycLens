# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: NullImporterTests_test_unencodeable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = os_helper.TESTFN_UNENCODABLE
    os.mkdir(name)
    try:
        self.assertRaises(ImportError, imp.NullImporter, name)
    finally:
        os.rmdir(name)
