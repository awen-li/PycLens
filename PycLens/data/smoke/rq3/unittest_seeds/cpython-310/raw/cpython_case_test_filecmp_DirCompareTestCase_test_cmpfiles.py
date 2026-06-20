# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_filecmp.py
# case: DirCompareTestCase_test_cmpfiles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(filecmp.cmpfiles(self.dir, self.dir, ['file']) == (['file'], [], []), 'Comparing directory to itself fails')
    self.assertTrue(filecmp.cmpfiles(self.dir, self.dir_same, ['file']) == (['file'], [], []), 'Comparing directory to same fails')
    self.assertTrue(filecmp.cmpfiles(self.dir, self.dir, ['file'], shallow=False) == (['file'], [], []), 'Comparing directory to itself fails')
    self.assertTrue(filecmp.cmpfiles(self.dir, self.dir_same, ['file'], shallow=False), 'Comparing directory to same fails')
    with open(os.path.join(self.dir, 'file2'), 'w', encoding='utf-8') as output:
        output.write('Different contents.\n')
    self.assertFalse(filecmp.cmpfiles(self.dir, self.dir_same, ['file', 'file2']) == (['file'], ['file2'], []), 'Comparing mismatched directories fails')
