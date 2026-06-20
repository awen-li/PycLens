# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_suffix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:').suffix, '')
    self.assertEqual(P('c:/').suffix, '')
    self.assertEqual(P('c:a/b').suffix, '')
    self.assertEqual(P('c:/a/b').suffix, '')
    self.assertEqual(P('c:a/b.py').suffix, '.py')
    self.assertEqual(P('c:/a/b.py').suffix, '.py')
    self.assertEqual(P('c:a/.hgrc').suffix, '')
    self.assertEqual(P('c:/a/.hgrc').suffix, '')
    self.assertEqual(P('c:a/.hg.rc').suffix, '.rc')
    self.assertEqual(P('c:/a/.hg.rc').suffix, '.rc')
    self.assertEqual(P('c:a/b.tar.gz').suffix, '.gz')
    self.assertEqual(P('c:/a/b.tar.gz').suffix, '.gz')
    self.assertEqual(P('c:a/Some name. Ending with a dot.').suffix, '')
    self.assertEqual(P('c:/a/Some name. Ending with a dot.').suffix, '')
    self.assertEqual(P('//My.py/Share.php').suffix, '')
    self.assertEqual(P('//My.py/Share.php/a/b').suffix, '')
