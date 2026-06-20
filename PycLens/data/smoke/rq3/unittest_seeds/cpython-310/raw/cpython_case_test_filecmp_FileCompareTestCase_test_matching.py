# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_filecmp.py
# case: FileCompareTestCase_test_matching

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(filecmp.cmp(self.name, self.name), 'Comparing file to itself fails')
    self.assertTrue(filecmp.cmp(self.name, self.name, shallow=False), 'Comparing file to itself fails')
    self.assertTrue(filecmp.cmp(self.name, self.name_same), 'Comparing file to identical file fails')
    self.assertTrue(filecmp.cmp(self.name, self.name_same, shallow=False), 'Comparing file to identical file fails')
