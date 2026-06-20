# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_directory_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertSequencesEqual_noorder
    eq(self.glob('*', 'D'), [self.norm('a', 'D')])
    eq(self.glob('*', '*a'), [])
    eq(self.glob('a', '*', '*', '*a'), [self.norm('a', 'bcd', 'efg', 'ha')])
    eq(self.glob('?a?', '*F'), [self.norm('aaa', 'zzzF'), self.norm('aab', 'F')])
