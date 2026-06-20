# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_literal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertSequencesEqual_noorder
    eq(self.glob('a'), [self.norm('a')])
    eq(self.glob('a', 'D'), [self.norm('a', 'D')])
    eq(self.glob('aab'), [self.norm('aab')])
    eq(self.glob('zymurgy'), [])
    res = glob.glob('*')
    self.assertEqual({type(r) for r in res}, {str})
    res = glob.glob(os.path.join(os.curdir, '*'))
    self.assertEqual({type(r) for r in res}, {str})
    res = glob.glob(b'*')
    self.assertEqual({type(r) for r in res}, {bytes})
    res = glob.glob(os.path.join(os.fsencode(os.curdir), b'*'))
    self.assertEqual({type(r) for r in res}, {bytes})
