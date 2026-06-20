# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_stem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:').stem, '')
    self.assertEqual(P('c:.').stem, '')
    self.assertEqual(P('c:..').stem, '..')
    self.assertEqual(P('c:/').stem, '')
    self.assertEqual(P('c:a/b').stem, 'b')
    self.assertEqual(P('c:a/b.py').stem, 'b')
    self.assertEqual(P('c:a/.hgrc').stem, '.hgrc')
    self.assertEqual(P('c:a/.hg.rc').stem, '.hg')
    self.assertEqual(P('c:a/b.tar.gz').stem, 'b.tar')
    self.assertEqual(P('c:a/Some name. Ending with a dot.').stem, 'Some name. Ending with a dot.')
