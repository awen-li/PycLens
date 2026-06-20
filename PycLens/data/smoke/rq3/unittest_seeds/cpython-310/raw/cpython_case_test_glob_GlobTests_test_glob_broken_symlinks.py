# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_broken_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertSequencesEqual_noorder
    eq(self.glob('sym*'), [self.norm('sym1'), self.norm('sym2'), self.norm('sym3')])
    eq(self.glob('sym1'), [self.norm('sym1')])
    eq(self.glob('sym2'), [self.norm('sym2')])
