# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestZip64InSmallFiles_test_large_file_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in get_files(self):
        self.large_file_exception_test(f, zipfile.ZIP_STORED)
        self.large_file_exception_test2(f, zipfile.ZIP_STORED)
