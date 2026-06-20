# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_nested_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertSequencesEqual_noorder
    if os.path.normcase('abCD') == 'abCD':
        eq(self.glob('a', 'bcd', 'E*'), [self.norm('a', 'bcd', 'EF')])
    else:
        eq(self.glob('a', 'bcd', 'E*'), [self.norm('a', 'bcd', 'EF'), self.norm('a', 'bcd', 'efg')])
    eq(self.glob('a', 'bcd', '*g'), [self.norm('a', 'bcd', 'efg')])
