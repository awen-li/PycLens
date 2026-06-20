# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_change_default_filter_on_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def strict_filter(tarinfo, path):
        if tarinfo.name == 'ustar/regtype':
            return tarinfo
        else:
            return None
    tar = tarfile.TarFile(tarname, 'r')
    with support.swap_attr(tarfile.TarFile, 'extraction_filter', staticmethod(strict_filter)):
        with self.check_context(tar, None):
            self.expect_file('ustar/regtype')
