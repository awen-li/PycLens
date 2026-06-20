# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_filecmp.py
# case: FileCompareTestCase_test_cache_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    first_compare = filecmp.cmp(self.name, self.name_same, shallow=False)
    second_compare = filecmp.cmp(self.name, self.name_diff, shallow=False)
    filecmp.clear_cache()
    self.assertTrue(len(filecmp._cache) == 0, 'Cache not cleared after calling clear_cache')
