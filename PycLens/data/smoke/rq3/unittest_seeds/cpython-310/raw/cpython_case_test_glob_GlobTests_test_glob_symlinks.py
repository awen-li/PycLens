# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertSequencesEqual_noorder
    eq(self.glob('sym3'), [self.norm('sym3')])
    eq(self.glob('sym3', '*'), [self.norm('sym3', 'EF'), self.norm('sym3', 'efg')])
    self.assertIn(self.glob('sym3' + os.sep), [[self.norm('sym3')], [self.norm('sym3') + os.sep]])
    eq(self.glob('*', '*F'), [self.norm('aaa', 'zzzF'), self.norm('aab', 'F'), self.norm('sym3', 'EF')])
