# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_with_suffix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:a/b').with_suffix('.gz'), P('c:a/b.gz'))
    self.assertEqual(P('c:/a/b').with_suffix('.gz'), P('c:/a/b.gz'))
    self.assertEqual(P('c:a/b.py').with_suffix('.gz'), P('c:a/b.gz'))
    self.assertEqual(P('c:/a/b.py').with_suffix('.gz'), P('c:/a/b.gz'))
    self.assertRaises(ValueError, P('').with_suffix, '.gz')
    self.assertRaises(ValueError, P('.').with_suffix, '.gz')
    self.assertRaises(ValueError, P('/').with_suffix, '.gz')
    self.assertRaises(ValueError, P('//My/Share').with_suffix, '.gz')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, 'gz')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, '/')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, '\\')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, 'c:')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, '/.gz')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, '\\.gz')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, 'c:.gz')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, 'c/d')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, 'c\\d')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, '.c/d')
    self.assertRaises(ValueError, P('c:a/b').with_suffix, '.c\\d')
