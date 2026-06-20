# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_one_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertSequencesEqual_noorder
    eq(self.glob('a*'), map(self.norm, ['a', 'aab', 'aaa']))
    eq(self.glob('*a'), map(self.norm, ['a', 'aaa']))
    eq(self.glob('.*'), map(self.norm, ['.aa', '.bb']))
    eq(self.glob('?aa'), map(self.norm, ['aaa']))
    eq(self.glob('aa?'), map(self.norm, ['aaa', 'aab']))
    eq(self.glob('aa[ab]'), map(self.norm, ['aaa', 'aab']))
    eq(self.glob('*q'), [])
