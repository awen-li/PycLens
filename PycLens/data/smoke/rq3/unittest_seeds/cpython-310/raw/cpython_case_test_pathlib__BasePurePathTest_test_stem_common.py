# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_stem_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('').stem, '')
    self.assertEqual(P('.').stem, '')
    self.assertEqual(P('..').stem, '..')
    self.assertEqual(P('/').stem, '')
    self.assertEqual(P('a/b').stem, 'b')
    self.assertEqual(P('a/b.py').stem, 'b')
    self.assertEqual(P('a/.hgrc').stem, '.hgrc')
    self.assertEqual(P('a/.hg.rc').stem, '.hg')
    self.assertEqual(P('a/b.tar.gz').stem, 'b.tar')
    self.assertEqual(P('a/Some name. Ending with a dot.').stem, 'Some name. Ending with a dot.')
