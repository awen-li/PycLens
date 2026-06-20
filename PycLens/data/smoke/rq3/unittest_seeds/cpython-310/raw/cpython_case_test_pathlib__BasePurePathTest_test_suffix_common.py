# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_suffix_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('').suffix, '')
    self.assertEqual(P('.').suffix, '')
    self.assertEqual(P('..').suffix, '')
    self.assertEqual(P('/').suffix, '')
    self.assertEqual(P('a/b').suffix, '')
    self.assertEqual(P('/a/b').suffix, '')
    self.assertEqual(P('/a/b/.').suffix, '')
    self.assertEqual(P('a/b.py').suffix, '.py')
    self.assertEqual(P('/a/b.py').suffix, '.py')
    self.assertEqual(P('a/.hgrc').suffix, '')
    self.assertEqual(P('/a/.hgrc').suffix, '')
    self.assertEqual(P('a/.hg.rc').suffix, '.rc')
    self.assertEqual(P('/a/.hg.rc').suffix, '.rc')
    self.assertEqual(P('a/b.tar.gz').suffix, '.gz')
    self.assertEqual(P('/a/b.tar.gz').suffix, '.gz')
    self.assertEqual(P('a/Some name. Ending with a dot.').suffix, '')
    self.assertEqual(P('/a/Some name. Ending with a dot.').suffix, '')
