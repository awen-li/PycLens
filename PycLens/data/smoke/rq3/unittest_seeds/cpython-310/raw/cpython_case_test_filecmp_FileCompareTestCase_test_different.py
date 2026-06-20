# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_filecmp.py
# case: FileCompareTestCase_test_different

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(filecmp.cmp(self.name, self.name_diff), 'Mismatched files compare as equal')
    self.assertFalse(filecmp.cmp(self.name, self.dir), 'File and directory compare as equal')
