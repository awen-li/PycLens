# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_file.py
# case: TestUnicodeFiles_test_directories

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ext = '.dir'
    self._do_directory(TESTFN_UNICODE + ext, TESTFN_UNICODE + ext)
    if TESTFN_UNENCODABLE is not None:
        self._do_directory(TESTFN_UNENCODABLE + ext, TESTFN_UNENCODABLE + ext)
