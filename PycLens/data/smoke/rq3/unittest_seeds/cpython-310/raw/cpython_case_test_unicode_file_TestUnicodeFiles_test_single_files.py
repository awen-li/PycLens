# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_file.py
# case: TestUnicodeFiles_test_single_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_single(TESTFN_UNICODE)
    if TESTFN_UNENCODABLE is not None:
        self._test_single(TESTFN_UNENCODABLE)
