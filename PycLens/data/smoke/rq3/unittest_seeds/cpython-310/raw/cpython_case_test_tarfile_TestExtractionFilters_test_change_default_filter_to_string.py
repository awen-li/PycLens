# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_change_default_filter_to_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.TarFile(tarname, 'r')
    tar.extraction_filter = 'data'
    with self.check_context(tar, None):
        self.expect_exception(TypeError)
