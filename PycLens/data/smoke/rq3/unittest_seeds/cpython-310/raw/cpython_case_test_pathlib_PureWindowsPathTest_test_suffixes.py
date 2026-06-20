# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_suffixes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:').suffixes, [])
    self.assertEqual(P('c:/').suffixes, [])
    self.assertEqual(P('c:a/b').suffixes, [])
    self.assertEqual(P('c:/a/b').suffixes, [])
    self.assertEqual(P('c:a/b.py').suffixes, ['.py'])
    self.assertEqual(P('c:/a/b.py').suffixes, ['.py'])
    self.assertEqual(P('c:a/.hgrc').suffixes, [])
    self.assertEqual(P('c:/a/.hgrc').suffixes, [])
    self.assertEqual(P('c:a/.hg.rc').suffixes, ['.rc'])
    self.assertEqual(P('c:/a/.hg.rc').suffixes, ['.rc'])
    self.assertEqual(P('c:a/b.tar.gz').suffixes, ['.tar', '.gz'])
    self.assertEqual(P('c:/a/b.tar.gz').suffixes, ['.tar', '.gz'])
    self.assertEqual(P('//My.py/Share.php').suffixes, [])
    self.assertEqual(P('//My.py/Share.php/a/b').suffixes, [])
    self.assertEqual(P('c:a/Some name. Ending with a dot.').suffixes, [])
    self.assertEqual(P('c:/a/Some name. Ending with a dot.').suffixes, [])
