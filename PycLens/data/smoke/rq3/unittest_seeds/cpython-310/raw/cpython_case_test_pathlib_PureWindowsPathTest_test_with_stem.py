# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PureWindowsPathTest_test_with_stem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertEqual(P('c:a/b').with_stem('d'), P('c:a/d'))
    self.assertEqual(P('c:/a/b').with_stem('d'), P('c:/a/d'))
    self.assertEqual(P('c:a/Dot ending.').with_stem('d'), P('c:a/d'))
    self.assertEqual(P('c:/a/Dot ending.').with_stem('d'), P('c:/a/d'))
    self.assertRaises(ValueError, P('c:').with_stem, 'd')
    self.assertRaises(ValueError, P('c:/').with_stem, 'd')
    self.assertRaises(ValueError, P('//My/Share').with_stem, 'd')
    self.assertRaises(ValueError, P('c:a/b').with_stem, 'd:')
    self.assertRaises(ValueError, P('c:a/b').with_stem, 'd:e')
    self.assertRaises(ValueError, P('c:a/b').with_stem, 'd:/e')
    self.assertRaises(ValueError, P('c:a/b').with_stem, '//My/Share')
