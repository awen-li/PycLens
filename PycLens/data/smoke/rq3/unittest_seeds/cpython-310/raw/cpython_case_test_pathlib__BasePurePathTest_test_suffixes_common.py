# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_suffixes_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('').suffixes, [])
    self.assertEqual(P('.').suffixes, [])
    self.assertEqual(P('/').suffixes, [])
    self.assertEqual(P('a/b').suffixes, [])
    self.assertEqual(P('/a/b').suffixes, [])
    self.assertEqual(P('/a/b/.').suffixes, [])
    self.assertEqual(P('a/b.py').suffixes, ['.py'])
    self.assertEqual(P('/a/b.py').suffixes, ['.py'])
    self.assertEqual(P('a/.hgrc').suffixes, [])
    self.assertEqual(P('/a/.hgrc').suffixes, [])
    self.assertEqual(P('a/.hg.rc').suffixes, ['.rc'])
    self.assertEqual(P('/a/.hg.rc').suffixes, ['.rc'])
    self.assertEqual(P('a/b.tar.gz').suffixes, ['.tar', '.gz'])
    self.assertEqual(P('/a/b.tar.gz').suffixes, ['.tar', '.gz'])
    self.assertEqual(P('a/Some name. Ending with a dot.').suffixes, [])
    self.assertEqual(P('/a/Some name. Ending with a dot.').suffixes, [])
