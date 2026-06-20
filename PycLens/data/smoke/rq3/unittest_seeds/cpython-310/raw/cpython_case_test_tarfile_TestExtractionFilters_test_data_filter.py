# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: TestExtractionFilters_test_data_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.TarFile.open(tarname) as tar:
        for tarinfo in tar.getmembers():
            try:
                filtered = tarfile.data_filter(tarinfo, '')
            except tarfile.FilterError:
                continue
            self.assertIs(filtered.name, tarinfo.name)
            self.assertIs(filtered.type, tarinfo.type)
